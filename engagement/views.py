from django.core.mail import send_mail
from engagement_project import settings
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EngagementPost, EngagementPostProduct, EngagementPostProductMapping
from .serialization import EngagementPostSerializer, EngagementPostProductSerializer, CollectionSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from django.db.models import Sum, Count

def index(request):
    return render(request, 'index.html')


class EngagementPostListView(APIView):
    @swagger_auto_schema(tags=['EngagementPostCollection APIs'])
    def get(self, request, tenant_id):
        posts = EngagementPost.objects.filter(tenant_id=tenant_id).prefetch_related(
            'inflencer',
            'engagementpostcontent_set',
            'engagementpostproductmapping_set'
        )
        serializer = EngagementPostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateProductView(APIView):
    """
    API endpoint to create a new product with an image upload.
    """
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        request_body=EngagementPostProductSerializer,
        responses={
            201: EngagementPostProductSerializer,
            400: "Bad Request - Invalid Data"
        },
        operation_description="Create a new product with a unique SKU, name, and optional image."
    )
    def post(self, request):
        serializer = EngagementPostProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the product to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCollectionView(APIView):
    """
    API endpoint to create a new collection and associate engagement posts.
    """
    @swagger_auto_schema(
        request_body=CollectionSerializer,
        responses={
            201: openapi.Response("Collection created", CollectionSerializer),
            400: "Bad Request - Invalid Data"
        },
        operation_description="Create a new collection with a name and a list of engagement post IDs."
    )
    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            collection = serializer.save()  # Save the collection and associated posts
            return Response({"id": collection.id, "name": collection.name}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TopViewedEngagementPostsView(APIView):
    """
    API endpoint to list the top 5 viewed engagement posts for a given tenant_id.
    """
    @swagger_auto_schema(tags=['Top viewed post APIs'])
    def get(self, request, tenant_id):
        # Fetch the top 5 engagement posts based on views (number of likes or shares)
        top_posts = (
            EngagementPost.objects.filter(tenant_id=tenant_id)
            .order_by('-number_of_likes')[:5]  # Assuming views are counted by likes
            .values('thumbnail_title', 'cta_url')  # Adjust according to your requirement
        )

        if not top_posts:
            return Response({"message": "No posts found."}, status=status.HTTP_404_NOT_FOUND)

        return Response(top_posts, status=status.HTTP_200_OK)

class TopViewedProductsView(APIView):
    """
    API endpoint to list the top 5 most frequently viewed products for a given tenant_id.
    """

    @swagger_auto_schema(tags=['Top 5 Products APIs'])
    def get(self, request, tenant_id):
        # Fetch the top 5 products based on views
        top_products = (
            EngagementPostProductMapping.objects
            .filter(engagement_post__tenant_id=tenant_id)
            .values('engagement_post__thumbnail_title', 'engagement_post__cta_url')  # Assuming these fields for URL
            # .annotate(
            #     total_views=Count('engagement_post'),
            #     total_duration=Sum('engagement_postcollection__duration_in_seconds')  # Correctly access duration from EngagementPostCollection
            # )
            .order_by('-product_id')[:5]  # Get top 5 products by views
        )

        # Prepare the response data
        # result = []
        # for product in top_products:
        #     print(product)
        #     result.append({
        #         'product_name': product['engagement_post__thumbnail_title'],
        #         'post_content_url': product['engagement_post__cta_url'],
        #         'duration_watched_in_hours': product['total_duration'] / 3600  # Convert seconds to hours
        #     })

        return Response(top_products, status=status.HTTP_200_OK)



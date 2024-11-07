
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import action
# from drf_yasg.utils import swagger_auto_schema
# from .models import (User, EngagementPost, EngagementPostContent, 
#                      EngagementPostProduct, Collection, EngagementPostCollection)
# from .serialization import (EngagementPostSerializer, EngagementPostContentSerializer, 
#                           EngagementPostProductSerializer, CollectionSerializer, 
#                           EngagementPostCollectionSerializer)


# class EngagementPostView(viewsets.ModelViewSet):
#     queryset = EngagementPost.objects.all()
#     serializer_class = EngagementPostSerializer

#     @swagger_auto_schema(tags=['EngagementPost APIs'])
#     @action(detail=False, methods=['get'], url_path='top-viewed/(?P<tenant_id>[^/.]+)')
#     def list_top_viewed(self, request, tenant_id=None):
#         top_posts = EngagementPost.objects.filter(tenant_id=tenant_id).order_by('-view_count')[:5]
#         data = [{"thumbnail": post.thumbnail, "title": post.title, "url": post.content_url} for post in top_posts]
#         return Response(data, status=status.HTTP_200_OK)
    

#     # Create a new EngagementPost
#     @swagger_auto_schema(tags=['EngagementPost APIs'])
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     # Retrieve a single EngagementPost
#     @swagger_auto_schema(tags=['EngagementPost APIs'])
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     # Update an existing EngagementPost
#     @swagger_auto_schema(tags=['EngagementPost APIs'])
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

#     # Partially update an EngagementPost
#     @swagger_auto_schema(tags=['EngagementPost APIs'])
#     def partial_update(self, request, *args, **kwargs):
#         return self.update(request, *args, partial=True)

#     # Delete an EngagementPost
#     @swagger_auto_schema(tags=['EngagementPost APIs'])
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     # List all EngagementPosts
#     @swagger_auto_schema(tags=['EngagementPost APIs'])
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
    
#  # Custom action to fetch posts by tenant_id, including all content and products attached
#     @swagger_auto_schema(tags=['EngagementPost APIs'])
#     @action(detail=False, methods=['get'], url_path='tenant/(?P<tenant_id>[^/.]+)')
#     def list_posts_by_tenant(self, request, tenant_id=None):
#         # Filter posts by tenant_id
#         posts = EngagementPost.objects.filter(tenant_id=tenant_id)
#         post_data = []

#         for post in posts:
#             # Fetch related content and products for each post
#             post_content = EngagementPostContent.objects.filter(post=post)
#             post_products = EngagementPostProduct.objects.filter(post=post)
            
#             # Serialize the data
#             post_data.append({
#                 'post': EngagementPostSerializer(post).data,
#                 'content': EngagementPostContentSerializer(post_content, many=True).data,
#                 'products': EngagementPostProductSerializer(post_products, many=True).data,
#             })

#         # Return the serialized data
#         return Response(post_data, status=status.HTTP_200_OK)

# class EngagementPostContent(viewsets.ModelViewSet):
#     queryset = EngagementPostContent.objects.all()
#     serializer_class = EngagementPostContentSerializer

#     # Create a new EngagementPostContent
#     @swagger_auto_schema(tags=['EngagementPostContent APIs'])
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     # Retrieve a single EngagementPostContent
#     @swagger_auto_schema(tags=['EngagementPostContent APIs'])
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     # Update an existing EngagementPostContent
#     @swagger_auto_schema(tags=['EngagementPostContent APIs'])
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

#     # Partially update an EngagementPostContent
#     @swagger_auto_schema(tags=['EngagementPostContent APIs'])
#     def partial_update(self, request, *args, **kwargs):
#         return self.update(request, *args, partial=True)

#     # Delete an EngagementPostContent
#     @swagger_auto_schema(tags=['EngagementPostContent APIs'])
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     # List all EngagementPostContents
#     @swagger_auto_schema(tags=['EngagementPostContent APIs'])
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
    

# class EngagementPostProduct(viewsets.ModelViewSet):
#     queryset = EngagementPostProduct.objects.all()
#     serializer_class = EngagementPostProductSerializer

#     @swagger_auto_schema(tags=['EngagementPostProduct APIs'])
#     @action(detail=False, methods=['get'], url_path='top-viewed/(?P<tenant_id>[^/.]+)')
#     def list_top_viewed_products(self, request, tenant_id=None):
#         top_products = EngagementPostProduct.objects.filter(post__tenant_id=tenant_id).order_by('-view_count')[:5]
#         data = [{"name": product.name, "url": product.post.content_url, "duration_watched": product.duration_watched} for product in top_products]
#         return Response(data, status=status.HTTP_200_OK)

#     # Create a new EngagementPostProduct
#     @swagger_auto_schema(tags=['EngagementPostProduct APIs'])
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     # Retrieve a single EngagementPostProduct
#     @swagger_auto_schema(tags=['EngagementPostProduct APIs'])
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     # Update an existing EngagementPostProduct
#     @swagger_auto_schema(tags=['EngagementPostProduct APIs'])
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

#     # Partially update an EngagementPostProduct
#     @swagger_auto_schema(tags=['EngagementPostProduct APIs'])
#     def partial_update(self, request, *args, **kwargs):
#         return self.update(request, *args, partial=True)

#     # Delete an EngagementPostProduct
#     @swagger_auto_schema(tags=['EngagementPostProduct APIs'])
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     # List all EngagementPostProducts
#     @swagger_auto_schema(tags=['EngagementPostProduct APIs'])
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
    
    

# class Collection(viewsets.ModelViewSet):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer

#     @swagger_auto_schema(tags=['Collection APIs'])
#     @action(detail=False, methods=['post'], url_path='create-with-posts')
#     def create_with_posts(self, request):
#         post_ids = request.data.get('post_ids', [])
#         collection_name = request.data.get('name', '')

#         collection = Collection.objects.create(name=collection_name)
#         collection.post_ids.set(post_ids)  # Assuming you have a ManyToMany relationship

#         return Response(CollectionSerializer(collection).data, status=status.HTTP_201_CREATED)

#     # Create a new Collection
#     @swagger_auto_schema(tags=['Collection APIs'])
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     # Retrieve a single Collection
#     @swagger_auto_schema(tags=['Collection APIs'])
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     # Update an existing Collection
#     @swagger_auto_schema(tags=['Collection APIs'])
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

#     # Partially update a Collection
#     @swagger_auto_schema(tags=['Collection APIs'])
#     def partial_update(self, request, *args, **kwargs):
#         return self.update(request, *args, partial=True)

#     # Delete a Collection
#     @swagger_auto_schema(tags=['Collection APIs'])
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     # List all Collections
#     @swagger_auto_schema(tags=['Collection APIs'])
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# class EngagementPostCollection(viewsets.ModelViewSet):
#     queryset = EngagementPostCollection.objects.all()
#     serializer_class = EngagementPostCollectionSerializer

#     # Create a new EngagementPostCollection
#     @swagger_auto_schema(tags=['EngagementPostCollection APIs'])
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     # Retrieve a single EngagementPostCollection
#     @swagger_auto_schema(tags=['EngagementPostCollection APIs'])
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     # Update an existing EngagementPostCollection
#     @swagger_auto_schema(tags=['EngagementPostCollection APIs'])
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

#     # Partially update an EngagementPostCollection
#     @swagger_auto_schema(tags=['EngagementPostCollection APIs'])
#     def partial_update(self, request, *args, **kwargs):
#         return self.update(request, *args, partial=True)

#     # Delete an EngagementPostCollection
#     @swagger_auto_schema(tags=['EngagementPostCollection APIs'])
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     # List all EngagementPostCollections
#     @swagger_auto_schema(tags=['EngagementPostCollection APIs'])
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

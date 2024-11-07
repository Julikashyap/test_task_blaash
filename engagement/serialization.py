from rest_framework import serializers
from .models import *
import decimal

class InfluencerMasterSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    class Meta:
        model = InfluencerMaster
        fields = '__all__'
    def get_price(self, obj):
        try:
            return float(obj.price) if obj.price is not None else None
        except decimal.InvalidOperation:
            return None  # Handle or log error as needed

class EngagementPostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostContent
        fields = '__all__'

class EngagementPostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostProduct
        fields = '__all__'

class EngagementPostProductMappingSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = EngagementPostProductMapping
        fields = ['engagement_post_product_mapping_id', 'product_id', 'product']

    def get_product(self, obj):
        product = EngagementPostProduct.objects.filter(sku=obj.product_id).first()
        return EngagementPostProductSerializer(product).data if product else None

class EngagementPostSerializer(serializers.ModelSerializer):
    influencer = InfluencerMasterSerializer(source='inflencer', read_only=True)
    contents = EngagementPostContentSerializer(source='engagementpostcontent_set', many=True, read_only=True)
    products = EngagementPostProductMappingSerializer(source='engagementpostproductmapping_set', many=True, read_only=True)

    class Meta:
        model = EngagementPost
        fields = '__all__'

class EngagementPostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementPostProduct
        fields = ['product_name', 'product_image', 'sku']

    def validate_sku(self, value):
        """Check that the SKU is unique."""
        if EngagementPostProduct.objects.filter(sku=value).exists():
            raise serializers.ValidationError("A product with this SKU already exists.")
        return value

class CollectionSerializer(serializers.ModelSerializer):
    engagement_posts = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        help_text="List of Engagement Post IDs to associate with this collection."
    )

    class Meta:
        model = Collection
        fields = ['name', 'engagement_posts']

    def create(self, validated_data):
        engagement_post_ids = validated_data.pop('engagement_posts', [])
        collection = Collection.objects.create(**validated_data)

        # Create mappings for the associated engagement posts
        for post_id in engagement_post_ids:
            EngagementPostCollection.objects.create(
                engagement_post_id=post_id,
                collection=collection
            )

        return collection

from django.db import models

# Create your models here.

class InfluencerMaster(models.Model):
    influencer_master_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_pic_url = models.CharField(max_length=200, blank=True, null=True)
    sample_video_url = models.CharField(max_length=200, blank=True, null=True)
    sample_video1_url = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    is_active = models.BooleanField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    highlight_text = models.CharField(blank=True, null=True)
    hash_tags = models.CharField(max_length=300, blank=True, null=True)
    sample_video2_url = models.CharField(max_length=200, blank=True, null=True)
    email_id = models.CharField(blank=True, null=True)
    folder_name = models.CharField(max_length=24, blank=True, null=True)
    is_master_account = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'influencer_master'

class EngagementPost(models.Model):
    enagement_post_id = models.BigAutoField(primary_key=True)
    tenant_id = models.BigIntegerField()
    number_of_likes = models.BigIntegerField(blank=True, null=True)
    number_of_shares = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_by = models.TextField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    customer_interaction_date = models.DateTimeField(blank=True, null=True)
    shopping_url = models.CharField(max_length=100, blank=True, null=True)
    customers_who_liked = models.TextField(blank=True, null=True)
    content_type = models.IntegerField()
    inflencer = models.ForeignKey('InfluencerMaster', models.DO_NOTHING, db_column='Inflencer_id', blank=True, null=True)  # Field name made lowercase.
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    thumbnail_url = models.CharField(max_length=200, blank=True, null=True)
    thumbnail_title = models.CharField(max_length=100, blank=True, null=True)
    is_cancelled = models.BooleanField()
    schedule_code = models.CharField(max_length=50, blank=True, null=True)
    button_cta = models.CharField(max_length=20, blank=True, null=True)
    is_new_collection = models.BooleanField(blank=True, null=True)
    video_duration = models.IntegerField(blank=True, null=True)
    is_multihost = models.BooleanField(blank=True, null=True)
    disabled_product = models.BooleanField(blank=True, null=True)
    cta_url = models.TextField(blank=True, null=True)
    product_thumbnail_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engagement_post'

class EngagementPostContent(models.Model):
    engagement_post_content_id = models.BigAutoField(primary_key=True)
    file_type = models.CharField(max_length=10)
    story = models.ForeignKey(EngagementPost, models.DO_NOTHING)
    url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engagement_post_content'
        db_table_comment = 'The URL for Content'

class EngagementPostProductMapping(models.Model):
    engagement_post_product_mapping_id = models.BigAutoField(primary_key=True)
    engagement_post = models.ForeignKey(EngagementPost, models.DO_NOTHING)
    product_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'engagement_post_product_mapping'

class EngagementPostProduct(models.Model):
    product_name = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to='products/')
    sku = models.CharField(max_length=50, unique=True)

    class Meta:
        managed = True
        db_table = 'engagement_post_product'

class Collection(models.Model):
    name = models.CharField(max_length=255)  # Collection Name

    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'collection'

class EngagementPostCollection(models.Model):
    engagement_post = models.ForeignKey(EngagementPostProduct, on_delete=models.DO_NOTHING, blank=True, null=True)  # Map to engagement posts
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING, blank=True, null=True)  # Map to collections
    duration_in_seconds = models.IntegerField(default=1)  # Duration in seconds

    def __str__(self):
        return f"{self.engagement_post} in {self.collection} for {self.duration_in_seconds} seconds"

    class Meta:
        managed = True
        db_table = 'engagement_post_collection'
from django.contrib import admin
from .models import *

admin.site.register(InfluencerMaster)
admin.site.register(EngagementPost)
admin.site.register(EngagementPostContent)
admin.site.register(EngagementPostProductMapping)
admin.site.register(EngagementPostProduct)
admin.site.register(Collection)
admin.site.register(EngagementPostCollection)
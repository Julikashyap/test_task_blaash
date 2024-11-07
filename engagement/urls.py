from .views import *
from django.urls import path, include, re_path


urlpatterns = [
    path('', index, name='welcome'),
    path('api/posts/<int:tenant_id>/', EngagementPostListView.as_view(), name='engagement-post-list'),
    path('api/products/', CreateProductView.as_view(), name='create-product'),
    path('api/collections/', CreateCollectionView.as_view(), name='create-collection'),
    path('api/posts/top-viewed/<int:tenant_id>/', TopViewedEngagementPostsView.as_view(), name='top-viewed-posts'),
    path('api/products/top-viewed/<int:tenant_id>/', TopViewedProductsView.as_view(), name='top-viewed-products'),
]
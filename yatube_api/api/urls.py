from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views

from .views import (
    CommentViewSet,
    GroupViewSet,
    PostViewSet,
)

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('groups', GroupViewSet, basename='group')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)

urlpatterns = [
    path('v1/api-token-auth/', auth_views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views

from .views import (
    CommentDetailView,
    CommentListCreateView,
    GroupViewSet,
    PostViewSet,
)

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('', include(v1_router.urls)),
    path(
        'posts/<int:post_id>/comments/',
        CommentListCreateView.as_view(),
        name='comment-list',
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        CommentDetailView.as_view(),
        name='comment-detail',
    ),
]

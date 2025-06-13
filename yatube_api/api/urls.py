from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('groups', views.GroupViewSet, basename='groups')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'posts/<int:post_id>/comments/',
        views.CommentViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='comment-list'
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        views.CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
        name='comment-detail'
    ),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
router = DefaultRouter()

router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='all_comments')
router.register(r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>)',
                CommentViewSet, basename='single_comment')
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='following')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]

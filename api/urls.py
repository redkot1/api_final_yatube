from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<id>[0-9]+)/comments',
                CommentViewSet,
                basename='comments')
router.register(r'group', GroupViewSet, 'Group')
router.register(r'follow', FollowViewSet, 'Follow')

api_versions = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]

urlpatterns = [
    path('', include(api_versions))
]

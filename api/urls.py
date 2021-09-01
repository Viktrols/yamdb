from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from . import views

router = DefaultRouter()

router.register('categories', views.CategoryViewSet, basename='category')
router.register('genres', views.GenreViewSet, basename='genre')
router.register('titles', views.TitleViewSet, basename='title')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)

v1_patterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(router.urls)),

]

urlpatterns = [
    path('v1/', include(v1_patterns)),
]

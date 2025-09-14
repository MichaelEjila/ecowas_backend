# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"members", MemberViewSet)
router.register(r"didyouknow", DidYouKnowViewSet)
router.register(r"gallery/sections", GallerySectionViewSet)
router.register(r"gallery/images", GalleryImageViewSet)
router.register(r"gallery/videos", GalleryVideoViewSet)
router.register(r"memberstates", MemberStateViewSet)
router.register(r"contactinfo", ContactInfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("stats/", StatsView.as_view(), name="stats"),
]

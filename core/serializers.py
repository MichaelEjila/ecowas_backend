# core/serializers.py
from rest_framework import serializers
from .models import Member, DidYouKnow, GallerySection, GalleryImage, GalleryVideo, MemberState, ContactInfo
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "role", "is_active")
        read_only_fields = ("id",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "role", "is_active")
        read_only_fields = ("id",)

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"

class DidYouKnowSerializer(serializers.ModelSerializer):
    class Meta:
        model = DidYouKnow
        fields = "__all__"

class GallerySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GallerySection
        fields = "__all__"

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"

class GalleryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryVideo
        fields = "__all__"

class MemberStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberState
        fields = "__all__"

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"

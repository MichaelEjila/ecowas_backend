# core/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import (
    User,
    Member,
    DidYouKnow,
    GallerySection,
    GalleryImage,
    GalleryVideo,
    MemberState,
    ContactInfo,
)

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions", "role")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "role", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser", "is_active", "groups")


# -------- Members --------
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role_type", "position", "country", "years_of_service", "email")
    list_filter = ("role_type", "country")
    search_fields = ("name", "position", "country", "email")

# -------- DidYouKnow --------
@admin.register(DidYouKnow)
class DidYouKnowAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "content")

# -------- Gallery --------
@admin.register(GallerySection)
class GallerySectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "date_taken", "location")
    list_filter = ("section", "date_taken")
    search_fields = ("title", "description", "location")

@admin.register(GalleryVideo)
class GalleryVideoAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "date_taken")
    list_filter = ("section", "date_taken")
    search_fields = ("title", "description")

# -------- MemberState --------
@admin.register(MemberState)
class MemberStateAdmin(admin.ModelAdmin):
    list_display = ("name", "currency", "language")
    search_fields = ("name", "currency", "language")

# -------- ContactInfo --------
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("address", "phone", "email")
    search_fields = ("address", "phone", "email")
# core/models.py
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

class User(AbstractUser):
    ROLE_ADMIN = "ADMIN"
    ROLE_EDITOR = "EDITOR"
    ROLE_VIEWER = "VIEWER"

    ROLE_CHOICES = [
        (ROLE_ADMIN, "Admin"),
        (ROLE_EDITOR, "Editor"),
        (ROLE_VIEWER, "Viewer"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ROLE_VIEWER)

    def is_admin(self):
        return self.role == self.ROLE_ADMIN or self.is_superuser

    def is_editor(self):
        return self.role == self.ROLE_EDITOR

    def is_viewer(self):
        return self.role == self.ROLE_VIEWER


class Member(models.Model):
    ROLE_CHOICES = [
        ("SPEAKER", "Speaker"),
        ("DEPUTY", "Deputy Speaker"),
        ("CHAIR", "Committee Chair"),
        ("MP", "Regular MP"),
    ]

    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    role_type = models.CharField(max_length=10, choices=ROLE_CHOICES)
    country = models.CharField(max_length=100)
    countryCode = models.CharField(max_length=10)
    isEditable = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    years_of_service = models.IntegerField(default=0)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.role_type})"

class DidYouKnow(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="didyouknow/")

    def __str__(self):
        return self.title

class GallerySection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    section = models.ForeignKey(GallerySection, related_name="images", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_taken = models.DateField(default=timezone.now)
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="gallery/images/")

    def __str__(self):
        return self.title

class GalleryVideo(models.Model):
    section = models.ForeignKey(GallerySection, related_name="videos", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_taken = models.DateField(default=timezone.now)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class MemberState(models.Model):
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email
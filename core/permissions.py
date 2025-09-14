from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_superuser or user.role == "ADMIN" or user.groups.filter(name="Admin").exists())

class IsEditorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return user.is_authenticated and (
            user.is_superuser or user.role == "ADMIN" or
            user.role == "EDITOR" or user.groups.filter(name="Editor").exists()
        )

class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class IsEditorOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admins can do anything
        if request.user.is_admin():
            return True
        # Editors can edit any object
        if request.user.is_editor():
            return True
        # Viewers can only read
        if request.method in SAFE_METHODS:
            return True
        return False

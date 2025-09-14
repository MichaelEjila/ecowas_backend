# core/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import IsEditorOrReadOnly, IsAdmin
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

# -------- Members --------
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsEditorOrReadOnly]
    filterset_fields = ["role_type", "country"]
    search_fields = ["name", "position", "country"]

# -------- DidYouKnow --------
class DidYouKnowViewSet(viewsets.ModelViewSet):
    queryset = DidYouKnow.objects.all()
    serializer_class = DidYouKnowSerializer
    permission_classes = [IsEditorOrReadOnly]

# -------- Gallery --------
class GallerySectionViewSet(viewsets.ModelViewSet):
    queryset = GallerySection.objects.all()
    serializer_class = GallerySectionSerializer
    permission_classes = [IsEditorOrReadOnly]

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsEditorOrReadOnly]

class GalleryVideoViewSet(viewsets.ModelViewSet):
    queryset = GalleryVideo.objects.all()
    serializer_class = GalleryVideoSerializer
    permission_classes = [IsEditorOrReadOnly]

# -------- MemberState --------
class MemberStateViewSet(viewsets.ModelViewSet):
    queryset = MemberState.objects.all()
    serializer_class = MemberStateSerializer
    permission_classes = [IsEditorOrReadOnly]

# -------- ContactInfo --------
class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [IsEditorOrReadOnly]


class StatsView(APIView):
    permission_classes = [IsEditorOrReadOnly]

    def get(self, request):
        data = {
            "total_members": Member.objects.count(),
            "speakers": Member.objects.filter(role_type="SPEAKER").count(),
            "deputy_speakers": Member.objects.filter(role_type="DEPUTY").count(),
            "committee_chairs": Member.objects.filter(role_type="CHAIR").count(),
            "regular_mps": Member.objects.filter(role_type="MP").count(),
        }
        return Response(data)

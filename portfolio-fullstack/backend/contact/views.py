from rest_framework import generics, permissions
from .models import ContactMessage
from .serializers import ContactMessageSerializer


class ContactMessageCreateView(generics.CreateAPIView):
    """POST /api/contact/ — used by the portfolio's contact form. Open to anyone."""
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]


class ContactMessageListView(generics.ListAPIView):
    """GET /api/messages/ — lists submissions. Admin login required.

    (You can also just browse them at /admin/, which is simpler.)
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.IsAdminUser]

from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Bisa dibaca semua, tapi hanya user login yang bisa buat

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:  # Hanya admin yang bisa hapus semua post
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        
        BlogPost.objects.all().delete()
        return Response({"message": "All blog posts deleted"}, status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # User biasa bisa lihat, tapi harus login untuk edit/hapus

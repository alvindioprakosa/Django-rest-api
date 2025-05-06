from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    """
    API endpoint untuk menampilkan daftar blog post dan membuat blog post baru.
    - GET: Terbuka untuk semua pengguna (read-only).
    - POST: Hanya untuk pengguna yang terautentikasi.
    - DELETE: Hanya admin yang dapat menghapus semua post.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {"error": "Permission denied"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        deleted_count, _ = BlogPost.objects.all().delete()
        return Response(
            {"message": f"{deleted_count} blog post(s) deleted."},
            status=status.HTTP_204_NO_CONTENT
        )

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint untuk retrieve, update, dan delete satu blog post.
    - GET: Terbuka untuk semua pengguna.
    - PUT/PATCH/DELETE: Hanya untuk user terautentikasi.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

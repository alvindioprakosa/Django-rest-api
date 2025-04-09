from django.urls import path
from . import views

urlpatterns = [
    path("api/blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-list-create"),
    path("api/blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="blogpost-retrieve-update-destroy"),
]

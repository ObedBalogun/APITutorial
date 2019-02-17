from rest_framework import generics
from .serializers import BlogPostSerializer
from Blogg.models import BlogPost
from django.db.models import Q

class BlogPostCreateView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs


class BlogPostRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'



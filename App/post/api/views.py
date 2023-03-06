# Create your views here.

from rest_framework.viewsets import ModelViewSet
from App.post.models import Post
from App.post.api.serializers import PostSerialzer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerialzer
    queryset = Post.objects.all()
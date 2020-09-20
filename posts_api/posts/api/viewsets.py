from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from ..models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=["post"], detail=True)
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvote()
        return Response(post.upvotes_number, status=status.HTTP_200_OK)


class CommentViewset(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["post_id"] = self.kwargs["parent_lookup_post"]
        return context

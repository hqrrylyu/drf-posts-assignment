from rest_framework import serializers
from rest_framework.fields import empty

from ..models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "author_name", "title", "link", "upvotes_number", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author_name", "content", "created_at", "parent", "post"]

    def __init__(self, instance=None, data=empty, **kwargs):
        context = kwargs["context"]
        if data is not empty:
            _data = data.copy()
            _data.update(post=context["post_id"])
        else:
            _data = data
        super().__init__(instance=instance, data=_data, **kwargs)

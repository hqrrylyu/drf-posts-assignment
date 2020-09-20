from django.db import models
from django.db.models import F
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class AuthoredModel(models.Model):
    author_name = models.CharField(_("author name"), max_length=50)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(
        _("created at"), auto_now_add=True, editable=False
    )

    class Meta:
        abstract = True


class Post(AuthoredModel, TimestampedModel):
    title = models.CharField(_("title"), max_length=100, help_text=_("Post title."))
    link = models.URLField(_("link"), help_text=_("Post link."))
    upvotes_number = models.PositiveSmallIntegerField(
        _("upvotes number"), default=0, help_text=_("The number of post upvotes.")
    )

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return self.title

    def upvote(self):
        self.upvotes_number = F("upvotes_number") + 1
        self.save(update_fields=["upvotes_number"])
        self.refresh_from_db()


class Comment(AuthoredModel, TimestampedModel, MPTTModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("comment's post"),
        help_text=_("Related post."),
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
        verbose_name=_("comment's parent"),
        help_text=_("Parent comment."),
    )
    content = models.CharField(
        _("content"), max_length=250, help_text=_("Comment content.")
    )

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    class MPTTMeta:
        order_insertion_by = ["id"]

    def __str__(self):
        return self.content

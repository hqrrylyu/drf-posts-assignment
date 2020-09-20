from django.core.management.base import BaseCommand, CommandError

from posts_api.posts.models import Post


class Command(BaseCommand):
    help = "A command to reset posts upvotes"

    def handle(self, *args, **options):
        try:
            Post.objects.update(upvotes_number=0)
        except Exception as exc:
            raise CommandError("Posts upvotes has not been reset.") from exc

        self.stdout.write(
            self.style.SUCCESS("Posts upvotes has been reset successfully.")
        )

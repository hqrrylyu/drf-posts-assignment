"""posts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework_extensions.routers import ExtendedSimpleRouter

from posts_api.posts.api.viewsets import CommentViewset, PostViewset

router = ExtendedSimpleRouter()

router.register(r"posts", PostViewset).register(
    r"comments",
    CommentViewset,
    basename="post-comments",
    parents_query_lookups=["post"],
)

# fmt: off
urlpatterns = [
    path("api/", include(router.urls)),
]
# fmt: on

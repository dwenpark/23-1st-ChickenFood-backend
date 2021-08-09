from django.urls import path

from .views      import LikesView

urlpatterns = [
    path("", LikesView.as_view()),
    path("<int:product_id>", LikesView.as_view())
]
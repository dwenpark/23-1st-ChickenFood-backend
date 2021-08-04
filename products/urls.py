from django.urls  import path

from .views       import ProductView

urlpatterns = [
    path("/catalog", ProductView.as_view()),
]
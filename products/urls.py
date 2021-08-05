from django.urls  import path

from .views       import BrandView, TypeView, ProductView

urlpatterns = [
    path("/brand", BrandView.as_view()),
    path("/type", TypeView.as_view()),
    path("/catalog", ProductView.as_view()),
]
from django.urls  import path

from .views       import ProductsView, ProductPublicView, ProductPrivateView

urlpatterns = [
    path("", ProductsView.as_view()),
    path("/<product_id>/public", ProductPublicView.as_view()),
    path("/<product_id>/private", ProductPrivateView.as_view()),
]
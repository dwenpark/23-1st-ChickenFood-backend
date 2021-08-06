from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from .models          import Brand, Type, Product

class BrandsView(View):
    def get(self, request):
        brands  = Brand.objects.all().order_by("id")

        catalog = [{
            "id"    : brand.id,
            "name"  : brand.name,
            "image" : brand.image
        } for brand in brands]

        return JsonResponse({"catalog": catalog}, status=200)

class TypesView(View):
    def get(self, request):
        types   = Type.objects.all().order_by("id")

        catalog = [{
            "id"    : type.id,
            "name"  : type.name,
            "image" : type.image
        } for type in types]

        return JsonResponse({"catalog": catalog}, status=200)

class ProductsView(View):
    def get(self, request):
        brand_id = request.GET.get("brand")
        type_id  = request.GET.get("type")
        filter   = request.GET.get("filter", "id")

        if brand_id or type_id:
            products = Product.objects.filter(Q(brand=brand_id) | Q(type=type_id)).order_by("id")

        else:
            products = Product.objects.all().order_by("id")

        items = [{
                "id"          : product.id,
                "name"        : product.name,
                "price"       : product.price,
                "thumbnail"   : product.thumbnail,
                "like_number" : product.like_number
            } for product in products.order_by(filter)]

        return JsonResponse({"items" : items}, status=200)
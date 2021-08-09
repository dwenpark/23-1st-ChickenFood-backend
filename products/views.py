from django.views           import View
from django.http            import JsonResponse
from django.db.models       import Q
from django.core.exceptions import FieldError

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
        try:
            brand_id = request.GET.get("brand")
            type_id  = request.GET.get("type")
            filter   = request.GET.get("filter")

            q        = Q()

            if brand_id:
                q &= Q(brand=brand_id)

            if type_id:
                q &= Q(type=type_id)

            product_prefixes = {
                "best"   : "-like_number",
                "recent" : "-register_date",
                "old"    : "register_date"
            }

            items = [{
                    "id"          : product.id,
                    "name"        : product.name,
                    "price"       : product.price,
                    "thumbnail"   : product.thumbnail,
                    "like_number" : product.like_number
                } for product in Product.objects.filter(q).order_by(product_prefixes.get(filter, "id"))]
            return JsonResponse({"items" : items}, status=200)

        except FieldError:
            return JsonResponse({"RESULT" : "FILTER_ERROR"}, status=404)
from django.views           import View
from django.http            import JsonResponse
from django.db.models       import Q
from django.core.exceptions import FieldError, ObjectDoesNotExist

from .models                import Brand, Type, Product, Option
from likes.models           import Like
from members.utils          import login_decorator

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

class ProductPublicView(View):
    def get(self, request, product_id):
        if not product_id.isdigit():
            return JsonResponse({"ERROR": "NEED_NUMBER"}, status=400)

        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({"ERROR": "DOES_NOT_EXIST"}, status=400)

        product = Product.objects.get(id=product_id)

        item = [{
            "id"           : product.id,
            "name"         : product.name,
            "price"        : product.price,
            "thumbnail"    : product.thumbnail,
            "brand"        : product.brand.name,
            "type"         : product.type.name,
            "detail_image" : product.detail_image,
            "element"      : product.element,
            "weight"       : product.weight,
            "liked"        : False
        }]

        return JsonResponse({"item": item}, status=200)

class ProductPrivateView(View):
    @login_decorator
    def get(self, request, product_id):
        if not product_id.isdigit():
            return JsonResponse({"ERROR": "NEED_NUMBER"}, status=400)

        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({"ERROR": "DOES_NOT_EXIST"}, status=400)

        product = Product.objects.get(id=product_id)

        item = [{
            "id"          : product.id,
            "name"        : product.name,
            "price"       : product.price,
            "thumbnail"   : product.thumbnail,
            "brand"       : product.brand.name,
            "type"        : product.type.name,
            "detail_image": product.detail_image,
            "element"     : product.element,
            "weight"      : product.weight,
            "liked"       : Like.objects.filter(member_id = request.member.id, product_id = product_id).exists()
        }]

        return JsonResponse({"item": item}, status=200)

class OptionsView(View):
    def get(self, request):
        options = [{
            "id"   : option.id,
            "name" : option.name
        } for option in Option.objects.all()]

        return JsonResponse({"options" : options}, status=200)
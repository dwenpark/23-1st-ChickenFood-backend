from django.views   import View
from django.http    import JsonResponse

from .models        import Brand, Type, Product

class BrandView(View):
    def get(self, request):
        brands = Brand.objects.all()

        catalog = [{
            "id": brand.id,
            "name": brand.name,
            "image": brand.image
        } for brand in brands]

        return JsonResponse({"catalog": catalog}, status=200, safe=False)

class TypeView(View):
    def get(self, request):
        types = Type.objects.all()

        catalog = [{
            "id": type.id,
            "name": type.name,
            "image": type.image
        } for type in types]

        return JsonResponse({"catalog": catalog}, status=200, safe=False)

class ProductView(View):
    def get(self, request):
        filter   = request.GET.get("filter")
        id       = request.GET.get("id")

        if filter == "brand":
            id       = id if id else Brand.objects.all()[0].id
            products = Product.objects.filter(brand=id)

        elif filter == "type":
            id       = id if id else Type.objects.all()[0].id
            products = Product.objects.filter(type=id)

        elif filter == "best":
            products = Product.objects.all().order_by("-like_number")

        elif filter == "main":
            id       = Brand.objects.all()[0].id
            products = Product.objects.filter(brand=id).order_by("-like_number")

        else:
            products = Product.objects.all()

        items = [{
                "id"          : product.id,
                "name"        : product.name,
                "price"       : product.price,
                "thumbnail"   : product.thumbnail,
                "like_number" : product.like_number
            } for product in products]

        return JsonResponse({"items" : items}, status=200, safe=False)
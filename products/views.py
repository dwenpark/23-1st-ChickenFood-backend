from django.views   import View
from django.http    import JsonResponse

from .models        import Brand, Type, Product

class ProductView(View):
    def get(self, request):
        filter   = request.GET.get("filter")
        id       = request.GET.get("id")
        catalogs = []

        if filter == "brand":
            brands = Brand.objects.all()

            id = id if id else brands[0].id

            products = Product.objects.filter(brand=id)

            for brand in brands:
                catalogs.append({
                    "id"    : brand.id,
                    "name"  : brand.name,
                    "image" : brand.image
                })

        elif filter == "type":
            types = Type.objects.all()

            id = id if id else types[0].id

            products = Product.objects.filter(type=id)

            for type in types:
                catalogs.append({
                    "id"    : type.id,
                    "name"  : type.name
                })

        elif filter == "best":
            products = Product.objects.all().order_by("-like_number")

        else:
            products = Product.objects.all()

        items = []

        for product in products:
            items.append({
                "id"          : product.id,
                "name"        : product.name,
                "price"       : product.price,
                "thumbnail"   : product.thumbnail,
                "like_number" : product.like_number
            })
        return JsonResponse({"catalogs": catalogs if catalogs else None, "items":items}, status=200, safe=False)
from django.views   import View
from django.http    import JsonResponse

from .models        import Brand, Type, Product

class ProductView(View):
    def get(self, request):
        category = request.GET.get("category")
        id       = request.GET.get("id", 1)
        catalogs = []

        if category == "brand":
            products = Product.objects.filter(brand=id)
            brands   = Brand.objects.all()

            for brand in brands:
                catalogs.append({
                    "name"  : brand.name,
                    "image" : brand.image
                })

        elif category == "type":
            products = Product.objects.filter(type=id)
            types    = Type.objects.all()

            for type in types:
                catalogs.append({
                    "name" : type.name,
                    "image": type.image
                })

        elif category == "best":
            products = Product.objects.all().order_by("like_number")

        results  = []

        for product in products:
            results.append({
                "name"      : product.name,
                "price"     : product.price,
                "thumbnail" : product.thumbnail
            })
        return JsonResponse([catalogs if catalogs else None, results], status=200, safe=False)
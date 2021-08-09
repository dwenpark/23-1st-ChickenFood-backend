from django.views    import View
from django.http     import JsonResponse

from products.models import Product
from members.utils   import login_decorator
from .models         import Like

class LikesView(View):
    @login_decorator
    def get(self,request):
        results = [{
            "name"      : like.product.name,
            "price"     : like.product.price,
            "thumbnail" : like.product.thumbnail
        } for like in Like.objects.filter(member_id=request.member)]

        return JsonResponse({"Result": results}, status=200)

    @login_decorator
    def post(self, request, product_id):
        if Like.objects.filter(member_id=request.member, product_id=product_id).exists():
            return JsonResponse({"ERROR": "ALREADY_LIKED"}, status=400)

        Like.objects.create(member_id=request.member, product_id=product_id)

        product = Product.objects.get(id=product_id)
        product.like_number += 1
        product.save()
        return JsonResponse({"Result": "LIKED"}, status=200)

    @login_decorator
    def delete(self, request, product_id):
        if not Like.objects.filter(member_id=request.member, product_id=product_id).exists():
            return JsonResponse({"ERROR": "DID_NOT_LIKED"}, status=400)

        Like.objects.filter(member_id=request.member, product_id=product_id).delete()

        product = Product.objects.get(id=product_id)
        product.like_number -= 1
        product.save()
        return JsonResponse({"Result": "UNLIKED"}, status=200)
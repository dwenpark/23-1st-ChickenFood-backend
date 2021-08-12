import json
import re
import bcrypt
import jwt

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from chickenfood.settings import SECRET_KEY
from members.models       import Member
from products.models      import Product, Option
from inventorys.models    import Inventory
from members.utils        import login_decorator

class InventorysView(View):
    @login_decorator
    def post(self, request):
        data   = json.loads(request.body)
        member = request.member.id

        if not (data.get('product_id') and data.get('quantity')):
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        if not Product.objects.filter(id=data['product_id']).exists():
            return JsonResponse({"message": "INVALID_VALUE"}, status=400)

        if data['quantity'] < 1:
            return JsonResponse({"message": "INVALID_VALUE"}, status=400)

        product = Product.objects.get(id=data['product_id']).id
        option  = data.get('option_id')

        if not Option.objects.filter(id=option).exists():
            option = None

        item, created = Inventory.objects.get_or_create(
                            member_id = member,
                            product_id = product,
                            option_id = option
                        )
        item.quantity += data['quantity']
        item.save()

        return JsonResponse({"message": "SUCCESS"}, status=201)

    @login_decorator
    def get(self, request):
        inventorys = Inventory.objects.filter(member_id=request.member.id)

        items = [{
            "id"        : inventory.id,
            "name"      : inventory.product.name,
            "price"     : inventory.product.price,
            "thumbnail" : inventory.product.thumbnail,
            "quantity"  : inventory.quantity,
            "option"    : {
                "id"   : inventory.option.id if inventory.option else None,
                "name" : inventory.option.name if inventory.option else None
            }
        } for inventory in inventorys]

        return JsonResponse({"items": items}, status=200)

    @login_decorator
    def delete(self, request):
        inventorys = request.GET.getlist('id')

        items = Inventory.objects.filter(member_id=request.member.id)

        if inventorys:
            items = Inventory.objects.filter(id__in=inventorys, member_id=request.member.id)

        items.delete()

        return JsonResponse({"message": "SUCCESS"}, status=204)

    @login_decorator
    def patch(self, request):
        data = json.loads(request.body)
 
        item = Inventory.objects.filter(id=request.GET.get('id'), memeber_id=request.member.id)

        if data.get('quantity'):
            item.update(quantity = data['quantity'])

        if data.get('option'):
            itemupdate(option_id = data['option'])

        return JsonResponse({"message": "SUCCESS"}, status=200)

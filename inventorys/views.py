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

        product = Product.objects.get(id=data['product_id']).id
        option  = data.get('option_id')

        if not Option.objects.filter(id=option).exists():
            option = None

        item, created = Inventory.objects.get_or_create(
                            member_id = member,
                            product_id = product,
                            option_id = option
                        )
        item.quantity += int(data['quantity'])
        item.save()

        return JsonResponse({"message": "SUCCESS"}, status=201)

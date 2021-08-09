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

class InventorysView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        member = request.member

        print(member)

        product = Product.objects.get(id=data['product_id'])
           
        if Option.objects.filter(id=data.get('option_id')).exists():
            option = Option.objects.get(id=data['option_id'])
        else:
            option = None

        items = Inventory.objects.filter(
                    member_id=member,
                    product_id=product,
                    option_id=option
                )
            
        if Inventory.objects.filter(member_id=member, product_id=product, option_id=option).exists():
            item = Inventory.objects.get(
                        member_id=member,
                        product_id=product,
                        option_id=option_id
                   )
            item.quantity += int(data['quantity'])
            item.save()

        return JsonResponse({"message": "SUCCESS"}, status=201)
            
        Inventory.objects.create(
                member_id=member.id,
                product_id=data['product_id'],
                quantity=data['quantity'],
                option_id=data.get('option_id')
        )

        return JsonResponse({"message": "SUCCESS"}, status=201)


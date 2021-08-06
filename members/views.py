import json
import re
import bcrypt
import jwt

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from chickenfood.settings import SECRET_KEY
from members.models       import Member

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if not (data.get('name') or data.get('email') or data.get('password') or data.get('phone_number')):
                return JsonResponse({"message": "EMPTY_VALUE"}, status=400)
            
            data['phone_number'] = data['phone_number'].replace("-", "")

            if not (re.match('^(?=.*[a-zA-Z]+).{1,}$', data['name']) or
                        re.match('^\w+@\w+\.\w+$', data['email']) or
                        re.match('\S{8,}', data['password']) or
                        re.match('\d{10,11}', data['phone_number'])):
                return JsonResponse({"message": "INVALID_FORMAT"}, status=400)
            
            if data.get('recommender'):
                if not Member.objects.filter(name=data['recommender']).exists():
                    return JsonResponse({"message": "INVALID_VALUE"}, status=400)

            if Member.objects.filter(Q(name=data['name']) | Q(email=data['email']) | Q('phone_number')).exists():
                return JsonResponse({"message": "EXISTED_MEMBER"}, status=400)

            Member.objects.create(
                    name         = data['name'],
                    email        = data['email'],
                    password     = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                    phone_number = data['phone_number'],
                    address      = data.get('address'),
                    recommender  = Member.objects.get(name=data['recommender'])
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)
        except Exception:
            return JsonResponse({"message": "INVALID_VALUE"}, status=400)

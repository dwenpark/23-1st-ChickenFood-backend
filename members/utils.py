import json
import jwt
import requests

from django.http import JsonResponse

def member_token(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token          = request.headers.get('Authorization')
            payload        = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            member         = Member.objects.get(id=payload['id'])
            request.member = member

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=400)

        except Exception:
            return JsonResponse({"message": "INVALID_AUTHORIZATION"}, status=400)

        return func(self, request, *args, **kwargs)
    return wrapper

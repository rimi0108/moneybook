import json, bcrypt, re

from django.views import View
from django.http import JsonResponse

from .models import User


class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"message": "EMAIL_ALREADY_EXISTS"}, status=400)

            EMAIL_VALIDATION = re.compile("[a-z0-9-_.]+@[a-z]+\.[a-z]")
            PASSWORD_VALIDATION = re.compile(
                "(?=.{8,})(?=.*[a-zA-Z!@#$%^&*()_+~])(?=.*[!@#$%^&*()_+~0-9]).*"
            )

            if not EMAIL_VALIDATION.match(data["email"]):
                return JsonResponse({"message": "EMAIL_FORMAT_ERROR"}, status=401)

            if not PASSWORD_VALIDATION.match(data["password"]):
                return JsonResponse({"message": "PASSWORD_FORMAT_ERROR"}, status=401)

            hashed_password = bcrypt.hashpw(
                data["password"].encode("utf-8"), bcrypt.gensalt()
            ).decode()

            User.objects.create(email=data["email"], password=hashed_password)
            return JsonResponse({"message": "SIGNUP_SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except json.decoder.JSONDecodeError:
            return JsonResponse({"message": "JSONDecodeError"}, status=400)

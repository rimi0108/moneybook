import json, bcrypt, re, jwt

from django.views import View
from django.http import JsonResponse

from my_settings import SECRET_KEY, ALGORITHM

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


class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email = data["email"]
            password = data["password"]

            user = User.objects.get(email=email)

            if not bcrypt.checkpw(
                password.encode("utf-8"), user.password.encode("utf-8")
            ):
                return JsonResponse({"MESSAGE": "WRONG_PASSWORD"}, status=401)

            access_token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse(
                {"message": "LOGIN_SUCCESS", "token": access_token},
                status=200,
            )

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"MESSAGE": "USER_DOES_NOT_EXIST"}, status=400)

        except User.MultipleObjectsReturned:
            return JsonResponse({"MESSAGE": "MULTIPLE_OBJECTS_RETURNED"}, status=400)

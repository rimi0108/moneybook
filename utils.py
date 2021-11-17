import jwt

from django.http import JsonResponse

from users.models import User, Token
from my_settings import SECRET_KEY, ALGORITHM


def log_in_confirm(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            user_token = request.headers.get("Authorization", None)

            user = jwt.decode(user_token, SECRET_KEY, ALGORITHM)

            if not User.objects.filter(id=user["id"]).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            if not Token.objects.filter(user_id=user["id"]).exists():
                return JsonResponse({"message": "INVALID_USER"})

            request.user = User.objects.get(id=user["id"])

            return func(self, request, *args, **kwargs)

        except jwt.InvalidSignatureError:
            return JsonResponse({"message": "JWT_SIGNATURE_ERROR"}, status=400)

        except jwt.DecodeError:
            return JsonResponse({"message": "JWT_DECODE_ERROR"}, status=400)

    return wrapper

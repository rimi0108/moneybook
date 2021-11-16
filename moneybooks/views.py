import json

from django.core.exceptions import ValidationError
from django.http.response   import JsonResponse
from django.views           import View

from .models import MoneyBook
from utils   import log_in_confirm


class MoneyBookView(View):
    @log_in_confirm
    def post(self, request):
        try:
            data = json.loads(request.body)

            user = request.user

            if len(str(data["amount"])) > 15:
                return JsonResponse({"message": "TOO_MUCH_AMOUNT"}, status=400)

            MoneyBook.objects.create(
                user_id=user.id,
                amount=data["amount"],
                date=data["date"],
                property=data["property"],
                category=data["category"],
                memo=data["memo"],
            )

            return JsonResponse({"message": "RECORD_SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except json.decoder.JSONDecodeError:
            return JsonResponse({"message": "JSONDecodeError"}, status=400)

        except ValidationError:
            return JsonResponse({"message": "VALIDATION_ERROR"}, status=404)

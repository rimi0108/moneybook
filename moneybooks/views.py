import json, datetime

from django.core.exceptions import ValidationError
from django.http.response import JsonResponse
from django.views import View
from django.db.models import Sum

from .models import MoneyBook
from utils import log_in_confirm


class UserMoneyBookView(View):
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

    @log_in_confirm
    def get(self, request):
        user = request.user

        now = datetime.datetime.now()

        year = request.GET.get("year", None)
        month = request.GET.get("month", None)
        day = request.GET.get("day", None)

        # 들어온 쿼리 파라미터에 따라 결과 list 필터링
        if year != None and month != None and day != None:
            all_records = MoneyBook.objects.filter(
                user_id=user.id, date__year=year, date__month=month, date__day=day
            )
        elif year != None and month != None:
            all_records = MoneyBook.objects.filter(
                user_id=user.id, date__year=year, date__month=month
            )
        elif year != None:
            all_records = MoneyBook.objects.filter(user_id=user.id, date__year=year)
        elif month != None:
            all_records = MoneyBook.objects.filter(
                user_id=user.id,
                date__year=now.strftime("%Y"),
                date__month=month,
            )
        elif day != None:
            all_records = MoneyBook.objects.filter(
                user_id=user.id,
                date__year=now.strftime("%Y"),
                date__month=now.strftime("%m"),
                date__day=day,
            )
        else:
            # 쿼리 파라미터 들어오지 않았을 때 현재 날짜의 기록 반환
            all_records = MoneyBook.objects.filter(
                user_id=user.id, date=now.strftime("%Y-%m-%d")
            )

        # 월별 총 입금 금액과 출금 금액 계산
        total_deposit = all_records.filter(type="DEPOSIT").aggregate(Sum("amount"))[
            "amount__sum"
        ]
        if total_deposit == None:
            total_deposit = 0

        total_withdraw = all_records.filter(type="WITHDRAW").aggregate(Sum("amount"))[
            "amount__sum"
        ]
        if total_withdraw == None:
            total_withdraw = 0

        total_price = {
            "total_deposit": format(total_deposit, ","),
            "total_withdraw": format(total_withdraw, ","),
        }

        results = [
            {
                "amount": format(record.amount, ","),
                "date": record.date,
                "property": record.property,
                "category": record.category,
                "memo": record.memo,
            }
            for record in all_records
        ]

        return JsonResponse(
            {"total_price": total_price, "records": results}, status=200
        )

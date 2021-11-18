import datetime

import jwt, json

from django.test import TestCase, Client
from django.db.models import Sum

from moneybooks.models import MoneyBook
from users.models import User, Token
from my_settings import SECRET_KEY, ALGORITHM


class CreateMoneyBookTest(TestCase):
    def setUp(self):
        user = User.objects.create(id=1, email="user1@gmail.com", password="abcd1234!")
        self.token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

        Token.objects.create(token=self.token, user_id=user.id)

        MoneyBook.objects.bulk_create(
            [
                MoneyBook(
                    id=1,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-09-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=2,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-10-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=3,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=4,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-17",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
            ]
        )

    def tearDown(self):
        User.objects.all().delete()
        MoneyBook.objects.all().delete()

    def test_moneybook_record_success(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}
        token = header["HTTP_Authorization"]

        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user = User.objects.get(id=payload["id"])

        data = {
            "user_id": user.id,
            "amount": 10000,
            "type": "DEPOSIT",
            "date": "2021-11-16",
            "property": "카드",
            "category": "식비",
            "memo": "",
        }
        response = client.post(
            "/moneybook", json.dumps(data), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "RECORD_SUCCESS"})

    def test_moneybook_enter_too_much_amount_fail(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}
        token = header["HTTP_Authorization"]

        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user = User.objects.get(id=payload["id"])

        data = {
            "user_id": user.id,
            "amount": 10000000000000000,
            "type": "DEPOSIT",
            "date": "2021-11-16",
            "property": "카드",
            "category": "식비",
            "memo": "",
        }
        response = client.post(
            "/moneybook", json.dumps(data), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "TOO_MUCH_AMOUNT"})

    def test_moneybook_key_error_fail(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}
        token = header["HTTP_Authorization"]

        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user = User.objects.get(id=payload["id"])

        data = {
            "user_id": user.id,
            "amount": 1000,
            "date": "2021-11-16",
            "property": "카드",
        }
        response = client.post(
            "/moneybook", json.dumps(data), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})


class MoneyBookListTest(TestCase):
    def setUp(self):
        user = User.objects.create(id=1, email="user1@gmail.com", password="abcd1234!")
        self.token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

        Token.objects.create(token=self.token, user_id=user.id)

        MoneyBook.objects.bulk_create(
            [
                MoneyBook(
                    id=1,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-09-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=2,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-10-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=3,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=4,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-17",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
            ]
        )

    def test_postview_get_success(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}
        token = header["HTTP_Authorization"]

        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user = User.objects.get(id=payload["id"])

        now = datetime.datetime.now()

        all_records = MoneyBook.objects.filter(
            user_id=user.id, date=now.strftime("%Y-%m-%d")
        )

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
                "date": record.date.strftime("%Y-%m-%d"),
                "type": record.type,
                "property": record.property,
                "category": record.category,
                "memo": record.memo,
            }
            for record in all_records
        ]

        response = client.get("/moneybook", **header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"total_price": total_price, "records": results},
        )

    def test_postview_month_filter_get_success(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}
        token = header["HTTP_Authorization"]

        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user = User.objects.get(id=payload["id"])

        all_records = MoneyBook.objects.filter(
            user_id=user.id, date__year=2021, date__month=10
        )

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
                "date": record.date.strftime("%Y-%m-%d"),
                "type": record.type,
                "property": record.property,
                "category": record.category,
                "memo": record.memo,
            }
            for record in all_records
        ]

        response = client.get("/moneybook?year=2021&month=10", **header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"total_price": total_price, "records": results},
        )

    def test_detail_postview_get_success(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}

        record = {
            "amount": "10,000.00",
            "date": "2021-09-16",
            "type": "WITHDRAW",
            "property": "현금",
            "category": "식비",
            "memo": "오늘도 돈 썼네..",
        }

        response = client.get("/moneybook/1", **header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"record": record},
        )


class UpdateMoneyBookTest(TestCase):
    def setUp(self):
        user = User.objects.create(id=1, email="user1@gmail.com", password="abcd1234!")
        self.token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

        Token.objects.create(token=self.token, user_id=user.id)

        MoneyBook.objects.bulk_create(
            [
                MoneyBook(
                    id=1,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-09-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=2,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-10-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=3,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=4,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-17",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
            ]
        )

    def test_post_update_success(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}

        data = {
            "amount": "1000",
            "date": "2021-09-16",
            "type": "WITHDRAW",
            "property": "현금",
            "category": "식비",
            "memo": "수정..",
        }

        response = client.patch(
            "/moneybook/1", json.dumps(data), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "UPDATE_SUCCESS"},
        )

    def test_post_update_key_error(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}

        data = {
            "amount": "1000",
            "date": "2021-09-16",
            "type": "WITHDRAW",
            "property": "현금",
            "memo": "수정..",
        }

        response = client.patch(
            "/moneybook/1", json.dumps(data), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"message": "KEY_ERROR"},
        )


class DeleteMoneyBookTest(TestCase):
    def setUp(self):
        user = User.objects.create(id=1, email="user1@gmail.com", password="abcd1234!")
        self.token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

        Token.objects.create(token=self.token, user_id=user.id)

        MoneyBook.objects.bulk_create(
            [
                MoneyBook(
                    id=1,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-09-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=2,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-10-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=3,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
                MoneyBook(
                    id=4,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-17",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                ),
            ]
        )

    def test_delete_moneybook_success(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}

        response = client.delete("/moneybook/1", **header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "DELETE_SUCCESS"},
        )

    def test_delete_fail(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}

        response = client.delete("/moneybook/100", **header)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"message": "RECORD_NOT_FOUND"},
        )


class RestoreMoneyBookTest(TestCase):
    def setUp(self):
        user = User.objects.create(id=1, email="user1@gmail.com", password="abcd1234!")
        self.token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

        Token.objects.create(token=self.token, user_id=user.id)

        MoneyBook.objects.bulk_create(
            [
                MoneyBook(
                    id=1,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-09-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                    is_deleted=True,
                ),
                MoneyBook(
                    id=2,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-10-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                    is_deleted=False,
                ),
                MoneyBook(
                    id=3,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-16",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                    is_deleted=False,
                ),
                MoneyBook(
                    id=4,
                    user_id=user.id,
                    amount=10000,
                    type="WITHDRAW",
                    date="2021-11-17",
                    property="현금",
                    category="식비",
                    memo="오늘도 돈 썼네..",
                    is_deleted=False,
                ),
            ]
        )

    def test_restore_moneybook_success(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}

        response = client.post("/moneybook/restore/1", **header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "RESTORE_SUCCESS"},
        )

    def test_restore_moneybook_fail(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}

        response = client.post("/moneybook/restore/2", **header)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"message": "RECORD_NOT_FOUND"},
        )

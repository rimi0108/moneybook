import jwt, json

from django.test import TestCase, Client

from moneybooks.models      import MoneyBook
from users.models           import User
from my_settings            import SECRET_KEY, ALGORITHM


class CreateMoneyBookTest(TestCase):
    def setUp(self):
        user = User.objects.create(id=1, email="user1@gmail.com", password="abcd1234!")
        self.token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

        MoneyBook.objects.create(
            user_id  = 1,
            amount   = 1000,
            date     = "2021-11-16",
            property = "현금",
            category = "간식",
            memo     = "오늘도 돈 씀..",
        )

    def tearDown(self):
        MoneyBook.objects.all().delete()

    def test_moneybook_record_success(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}
        token  = header["HTTP_Authorization"]

        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user    = User.objects.get(id=payload["id"])

        data = {
            "user_id"  : user.id,
            "amount"   : 10000,
            "date"     : "2021-11-16",
            "property" : "카드",
            "category" : "식비",
            "memo"     : "",
        }
        response = client.post(
            "/moneybook", json.dumps(data), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "RECORD_SUCCESS"})

    def test_moneybook_enter_too_much_amount_fail(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}
        token  = header["HTTP_Authorization"]

        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user    = User.objects.get(id=payload["id"])

        data = {
            "user_id"  : user.id,
            "amount"   : 10000000000000000,
            "date"     : "2021-11-16",
            "property" : "카드",
            "category" : "식비",
            "memo"     : "",
        }
        response = client.post(
            "/moneybook", json.dumps(data), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "TOO_MUCH_AMOUNT"})

    def test_moneybook_key_error_fail(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}
        token  = header["HTTP_Authorization"]

        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user    = User.objects.get(id=payload["id"])

        data = {
            "user_id"  : user.id,
            "amount"   : 1000,
            "date"     : "2021-11-16",
            "property" : "카드",
        }
        response = client.post(
            "/moneybook", json.dumps(data), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})

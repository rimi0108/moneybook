import bcrypt, jwt

from django.test import TestCase, Client

from users.models import User, Token
from my_settings import SECRET_KEY, ALGORITHM


class SignUpTest(TestCase):
    def setUp(self):
        User.objects.create(email="user1@gmail.com", password="abcd1234!")

    def tearDown(self):
        User.objects.all().delete()

    def test_sign_up_post_success(self):
        client = Client()
        data = {"email": "user2@gmail.com", "password": "abcd1234!"}
        response = client.post(
            "/users/signup", data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "SIGNUP_SUCCESS"})

    def test_sign_up_post_email_validation_fail(self):
        client = Client()
        data = {"email": "user2gmail.com", "password": "abcd1234!"}
        response = client.post(
            "/users/signup", data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "EMAIL_FORMAT_ERROR"})

    def test_sign_up_post_password_validation_fail(self):
        client = Client()
        data = {"email": "user2@gmail.com", "password": "abc123"}
        response = client.post(
            "/users/signup", data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "PASSWORD_FORMAT_ERROR"})

    def test_sign_up_post_key_error_fail(self):
        client = Client()
        data = {"email": "user2@gmail.com"}
        response = client.post(
            "/users/signup", data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})


class LogInTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            email="user1@gmail.com",
            password=bcrypt.hashpw(
                "abcd1234!".encode("utf-8"), bcrypt.gensalt()
            ).decode(),
        )
        self.token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

    def tearDown(self):
        User.objects.all().delete()

    def test_log_in_post_success(self):
        client = Client()
        data = {"email": "user1@gmail.com", "password": "abcd1234!"}
        response = client.post(
            "/users/login", data=data, content_type="application/json"
        )
        token = self.token

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "LOGIN_SUCCESS", "token": token})

    def test_log_in_post_invalid_email_fail(self):
        client = Client()
        data = {"email": "user@gmail.com", "password": "abcd1234!"}
        response = client.post(
            "/users/login", data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "USER_DOES_NOT_EXIST"})

    def test_log_in_post_invalid_password_fail(self):
        client = Client()
        data = {"email": "user1@gmail.com", "password": "wrong_password"}
        response = client.post(
            "/users/login", data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": "WRONG_PASSWORD"})

    def test_log_in_post_key_error_fail(self):
        client = Client()
        data = {"password": "abcd1234!"}
        response = client.post(
            "/users/login", data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})


class LogoutTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            email="user1@gmail.com",
            password=bcrypt.hashpw(
                "abcd1234!".encode("utf-8"), bcrypt.gensalt()
            ).decode(),
        )

        self.token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

        Token.objects.create(token=self.token, user_id=user.id)

    def tearDown(self):
        User.objects.all().delete()

    def test_log_out_success(self):
        client = Client()

        header = {"HTTP_Authorization": self.token}

        response = client.post("/users/logout", **header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "LOGOUT_SUCCESS"})

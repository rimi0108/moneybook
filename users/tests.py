import bcrypt, jwt

from django.test import TestCase, Client

from users.models import User
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

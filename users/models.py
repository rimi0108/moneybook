from django.db import models


class User(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"


class Token(models.Model):
    token = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tokens"

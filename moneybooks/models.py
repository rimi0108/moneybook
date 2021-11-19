from django.db import models


class MoneyBook(models.Model):
    TRANSACTION_TYPE = (("DEPOSIT", "DEPOSIT"), ("WITHDRAW", "WITHDRAW"))

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    date = models.DateField(db_index=True)
    type = models.CharField(max_length=8, choices=TRANSACTION_TYPE, default="WITHDRAW")
    property = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    memo = models.CharField(max_length=200, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "moneybooks"

from django.urls import path

from .views import UserMoneyBookView, MoneyBookView

urlpatterns = [
    path("moneybook", UserMoneyBookView.as_view()),
    path("moneybooks", MoneyBookView.as_view()),
]

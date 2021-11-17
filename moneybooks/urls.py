from django.urls import path

from .views import MoneyBookView, DetailMoneyBookView

urlpatterns = [
    path("moneybook", MoneyBookView.as_view()),
    path("moneybook/<int:moneybook_id>", DetailMoneyBookView.as_view()),
]

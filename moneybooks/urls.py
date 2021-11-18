from django.urls import path

from .views import MoneyBookView, DetailMoneyBookView, RestoreMoneyBookView

urlpatterns = [
    path("moneybook", MoneyBookView.as_view()),
    path("moneybook/<int:moneybook_id>", DetailMoneyBookView.as_view()),
    path("moneybook/restore/<int:moneybook_id>", RestoreMoneyBookView.as_view()),
]

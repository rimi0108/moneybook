from django.urls import path

from .views import MoneyBookView

urlpatterns = [
    path("moneybook", MoneyBookView.as_view()),
]

from django.urls import path

from .views import UserMoneyBookView

urlpatterns = [
    path("moneybook", UserMoneyBookView.as_view()),
]

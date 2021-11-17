from django.urls import path

from users.views import LoginView, SignupView, LogoutView

urlpatterns = [
    path("/signup", SignupView.as_view()),
    path("/login", LoginView.as_view()),
    path("/logout", LogoutView.as_view()),
]

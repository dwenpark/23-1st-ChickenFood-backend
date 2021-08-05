from django.urls import path

from members.views import AgreementView, LoginView

urlpatterns = [
        path('/agreement', AgreementView.as_view()),
        path('/login', LoginView.as_view()),
]

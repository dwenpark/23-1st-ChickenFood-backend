from django.urls import path

from members.views import SignUpView

urlpatterns = [
        path('/signup', SignUpView.as_view()),
]

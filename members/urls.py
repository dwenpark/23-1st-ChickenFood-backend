from django.urls import path

from members.views import SignUpView, SignInView, MemberCheckView

urlpatterns = [
        path('/signup', SignUpView.as_view()),
        path('/signin', SignInView.as_view()),
        path('/membercheck', MemberCheckView.as_view())
]

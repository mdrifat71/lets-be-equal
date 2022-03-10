from django.urls import path

from .views import SignUpUser

urlpatterns = [
    path('authentication/signup/', SignUpUser.as_view())
]
# accounts URL config 

from django.urls import path 
from structure.accounts.views import (
    LoginView,
    RegisterView,
    CheckPhoneNumber,
    CheckPassword
)


urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('sign-up/',RegisterView.as_view(),name='register'),

]

hx_response_url = [
    path('check/phone/number/',CheckPhoneNumber.as_view(),name="check_phone"),
    path('check/password/',CheckPassword.as_view(),name='check_password')
]

urlpatterns += hx_response_url



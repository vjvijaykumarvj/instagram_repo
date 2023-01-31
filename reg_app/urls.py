from django.urls import path
from.import views

urlpatterns=[
    path('register/',views.Signup),
    path('userlogin/',views.Userlogin),
    path('userlogout/',views.UserlogOut),
]
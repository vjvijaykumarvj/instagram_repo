from django.urls import path
from.import views

urlpatterns=[
    path('washning_machine/',views.Washning_Machine),
    path('washing_payment/',views.washing_payment),
    path('payment_success/',views.payment_success),
]
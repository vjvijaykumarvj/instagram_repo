from django .urls import path
from.import views


urlpatterns=[
    path('contactus/',views.Contactus),
    path('contactus_success/',views.contactus_success),
    path('aboutus/',views.aboutus),
    path('blog/',views.Blog),
]
from django.urls import path
from .views import SingUP

urlpatterns = [
    path('singup/',SingUP.as_view(), name='singup')
]
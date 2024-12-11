from django.urls import path
from .views import brand,car

urlpatterns = [
   path('',brand),
   path('car/',car), 
]

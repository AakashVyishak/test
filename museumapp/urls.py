from django.urls import path
from . import views
urlpatterns = [
   path('',views.fun,name='fun'),
   path('ggg',views.car,name='car')
]

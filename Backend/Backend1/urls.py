from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name='home'),
    path('insert_data',views.insert_data,name='insert_data'),
    path('getSensorType',views.getSensorType,name='getSensorType'),
]
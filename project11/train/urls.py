from django.urls import path
from train.views import *


app_name='train'

urlpatterns=[
    path('listoftrains/',listoftrains,name='listoftrains')
]
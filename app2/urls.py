from django.urls import path
from app2.views import *
app_name='some2'

urlpatterns=[
    path('third/',third,name='third'),
    path('four/',four,name='four'),
]
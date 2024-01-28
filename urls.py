from django.urls import path
from . import views
urlpatterns=[
    path('member1/',views.member1,name='member1'),
]
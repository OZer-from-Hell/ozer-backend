from django.urls import path
from . import views

urlpatterns = [
    path('nickname',views.Nickname.as_view()),
  
     
]
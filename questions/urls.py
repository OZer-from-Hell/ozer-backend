from django.urls import path
from . import views

urlpatterns = [
    path('list',views.QustionView.as_view()),
     
]
from django.urls import path
from . import views

urlpatterns = [
    path('items',views.OzerView.as_view()),
    path('items/totalOzer',views.TotalOzerView.as_view()),
  
     
]
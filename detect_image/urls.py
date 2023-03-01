from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='HomePage'),
    path('predict', views.Predict.as_view(), name='Predict'),
]

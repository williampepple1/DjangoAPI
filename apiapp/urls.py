from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstView.as_view(), name='first'),
    path('second-endpoint', views.SecondView.as_view(), name='second'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('city/<int:pk>/', views.city_detail, name='city_detail'),
    path('api/city/<int:pk>/', views.CityAPIView.as_view()),
    path('api/cities/', views.CityAPIView.as_view()),
]

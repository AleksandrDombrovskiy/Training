from django.urls import path
from .import views

urlpatterns = [
    path('', views.AnimeView.as_view(), name='home'),
    path('<slug:slug>/', views.AnimeDeteil.as_view(), name='anime_detel'),
    path('reviews/<int:pk>/', views.AddReview.as_view(), name='add')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='games-list'),
    path('<int:pk>/', views.game_detail, name='games-details'),
]

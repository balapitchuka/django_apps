from django.urls import path
from . import views

urlpatterns = [
    # path('', views.polls_list, name='polls-list'),
    # path('<int:pk>/', views.polls_detail, name='polls-detail'),
    path('', views.PollList.as_view(), name='polls-list'),
    path('<int:pk>/', views.PollDetail.as_view(), name='polls-detail'),
]
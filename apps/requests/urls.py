from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_request, name='create_request'),
    path('submitted/<int:pk>/', views.request_submitted, name='request_submitted'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('my-requests/<int:pk>/', views.request_detail, name='request_detail'),
]

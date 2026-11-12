from django.urls import path

from .views import AccountLoginView, AccountLogoutView, register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
]

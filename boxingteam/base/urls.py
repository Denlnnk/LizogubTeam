from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register-page'),
    path('update-user/', views.updateUser, name='update-user'),

    path('', views.index, name='home'),
    path('team/', views.teamPage, name='team'),
    path('user/<str:pk>', views.userPage, name='user-page'),
]
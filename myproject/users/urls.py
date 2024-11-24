from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.users_register, name='register'),
    path('login/', views.users_login, name='login'),
    path('logout/', views.users_logout, name='logout'),

    # path('<slug:slug>', views.post_page, name='page'),


]
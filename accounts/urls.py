from django.urls import path
from .views import index, login, logout, register

app_name = 'accounts'
urlpatterns = [
    path('', index, name = 'index'),
    path('login/', index, name = 'login'),
    path('logout/', index, name = 'logout'),
    path('register/', index, name = 'register'),

]

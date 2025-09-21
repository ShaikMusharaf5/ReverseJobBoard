from django.urls import path
from .views import profile_view, dashboard_view, register_page, login_page, root_redirect

app_name = 'core'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', root_redirect, name='root_redirect'),
    path('register_page/', register_page, name='register'),
    path('login_page/', login_page, name='login'),
]

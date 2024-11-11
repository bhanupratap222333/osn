from django.urls import path
from . import views
from .views import register_view


urlpatterns = [
    path("login/", views.login_view, name="login"),
   # path('login/', login_view, name='login'),

    path("logout/", views.logout_view, name="logout"),
    path("password_change/", views.password_change_view, name="password_change"),
    path("password_reset/", views.password_reset_view, name="password_reset"),
    path("verify_otp/", views.verify_otp_view, name="verify_otp"),
    path('register/', register_view, name='register'),

]

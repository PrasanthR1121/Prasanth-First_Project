from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("form_view/", form_view, name="form_view"),
    path("user_reg/", user_registration, name='registration'),
    path("user_login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
    path("special/", special, name="special")

]

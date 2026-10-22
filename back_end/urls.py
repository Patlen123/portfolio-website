from django.contrib import admin
from django.urls import path, include

from back_end import views

urlpatterns = [
    path('discord/auth', views.discord_auth, name="discord_login"),
    path('discord/auth/redirect', views.discord_auth_redirect, name="discord_auth_redirect"),
    path('discord/invite', views.invite_request, name="discord_invite_request"),

]

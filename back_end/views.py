from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

import back_end.discord_bot_manager as bm

AUTH_URL_DISCORD = "https://discord.com/api/oauth2/authorize?client_id=1089042302791589938&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fauth%2Fdiscord%2Fredirect&response_type=code&scope=identify"


def discord_auth(request):
    return redirect(AUTH_URL_DISCORD)


# TODO Make this work properly
def discord_auth_redirect(request):
    return JsonResponse({"msg": "This works!"})


# TODO Also make this work properly
def invite_request(request):
    username = request.GET.get('username')
    bm.send_invite_request(username)
    response_data = {
        'message': 'Invite request sent successfully',
    }

    # Return the response as JSON
    return JsonResponse(response_data)

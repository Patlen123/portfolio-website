from random import randint

from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests
import json
import back_end.discord_bot_manager as bm
from back_end.models import ExecMember, IdentityMember, OtherMember, AboutImage


def show_construction(request):
    return render(request, 'under_construction.html')


def show_index(request):
    events = bm.get_events_as_list()
    announcements, avatars, guild_ids = bm.get_announcements()
    return render(request, 'index.html',
                  {'events': events, 'announcements': announcements, 'avatars': avatars, 'guild_ids': guild_ids})


def show_about(request):
    return render(request, 'about.html')


"""
def show_com(request):
    exec = ExecMember.objects.all()
    identity = IdentityMember.objects.all()
    other = OtherMember.objects.all()
    return render(request, 'meet_the_com.html', {'exec': exec, 'identity': identity, 'other': other})


def show_about_image(request):
    about_images = AboutImage.objects.all()
    return render(request, 'about.html', {'about_images': about_images})

"""

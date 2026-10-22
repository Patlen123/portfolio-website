# TODO Handle Errors all that shit

import json

import requests
from django.conf import settings
from django.core.cache import cache

API_BASE_URL = "https://discord.com/api/v9"
GUILD_ID = "687976926949670933"
GUILD_URL = API_BASE_URL + "/guilds/" + GUILD_ID
CHANNEL_URL_INVITE = API_BASE_URL + "/channels/1089227275318329344/messages"

AVATAR_BASE_URL = "https://cdn.discordapp.com/avatars"

NUM_OF_MESSAGE = "5"
CHANNEL_URL_ANNOUNCE = API_BASE_URL + "/channels/687984537577324575/messages?limit=" + NUM_OF_MESSAGE

# TODO Remove and regenerate this before actually making the site live
TEMP_BOT_TOKEN = "MTA4OTA0MjMwMjc5MTU4OTkzOA.GS3ozo.xLKicJtog5KJqutb0KqMFPVl46RpyIv6qJr2Lc"

headers_get = {
    'Authorization': 'Bot ' + TEMP_BOT_TOKEN,
}

headers_post = {
    "Authorization": f"Bot {TEMP_BOT_TOKEN}",
    "Content-Type": "application/json"
}


# Grabs the events and formats them so that the rest of the website can handle it
def get_events_as_list():
    events = cache.get(settings.EVENTS_CACHE_KEY)
    if events is None:
        try:
            response = requests.get(GUILD_URL + "/scheduled-events", headers=headers_get)
            events = json.loads(response.text)
            events.sort(key=sort_events)
            cache.set(settings.EVENTS_CACHE_KEY, events, timeout=300)
        except Exception:

            return "ConFail"
    return events


# Discord gives us the events in reverse of the order created, so we need to sort them by scheduled_start_timee
def sort_events(sortBy):
    return sortBy['scheduled_start_time']


def send_invite_request(username):
    payload = {
        "content": username + " is asking for an invite link"
    }
    response = requests.post(CHANNEL_URL_INVITE, headers=headers_post, json=payload)

    # Check if the message was sent successfully
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Error code: {response.status_code}")


# Get a list of announcements from Discord
def get_announcements():
    announcements = cache.get(settings.ANNOUNCEMENTS_CACHE_KEY)
    if announcements is None:
        try:
            response = requests.get(CHANNEL_URL_ANNOUNCE, headers=headers_get)
            if response.status_code != 200:
                return "ConFail"
            announcements = json.loads(response.text)
            cache.set(settings.ANNOUNCEMENTS_CACHE_KEY, announcements, timeout=300)
        except Exception:
            return "ConFail"
    guild_ids = get_guild_identity(announcements)
    avatars = get_avatars(announcements)
    return announcements, avatars, guild_ids


# Gets the Guild Member object so names are displayed as "Naomi (She/They) - Lesbian Off" and not "munchkin"
def get_guild_identity(announcements):
    guild_ids = cache.get(settings.GUILD_ID_CACHE_KEY)
    if guild_ids is None:
        guild_ids = []
        try:
            authors = [announcement['author'] for announcement in announcements]
            author_data = [{'id': author['id']} for author in authors]

            unique_data = []
            for data in author_data:
                if data not in unique_data:
                    unique_data.append(data)

            for unique_id in unique_data:
                response = requests.get(GUILD_URL + "/members/" + unique_id['id'], headers=headers_get)
                guild_member = json.loads(response.text)
                if response.status_code == 200 and guild_member['nick'] is not None:
                    guild_ids.append({'id': unique_id['id'], 'guild_nick': guild_member['nick']})
                else:
                    guild_ids.append(guild_ids.append({'id': unique_id['id'], 'guild_nick': "NO UNIQUE NAME"}))
                cache.set(settings.GUILD_ID_CACHE_KEY, guild_ids, timeout=300)
        except Exception:
            return "ConFail"
    return guild_ids


# Could expand this later to grab Nitro guild pictures if you want, I didn't bother because it's such a niche case
def get_avatars(announcements):
    avatars = cache.get(settings.AVATAR_CACHE_KEY)
    if avatars is None:
        avatars = []
        # Take out the needed data from the announcement set and unique it
        authors = [announcement['author'] for announcement in announcements]
        author_data = [{'id': author['id'], 'avatar': author['avatar']} for author in authors]

        # Remove repeats
        unique_data = []
        for data in author_data:
            if data not in unique_data:
                unique_data.append(data)

        # Make a list of the URLs needed and the hash
        for id_and_hash in author_data:
            count = 0
            count += 1
            current_avatar_url = AVATAR_BASE_URL + "/" + id_and_hash['id'] + "/" + id_and_hash['avatar'] + ".png"
            response = requests.get(current_avatar_url, headers=headers_get)
            if response.status_code == 200:
                # Add the URL as a dict item
                avatars.append({'author_id': id_and_hash['id'], 'image_url': current_avatar_url})
        cache.set(settings.AVATAR_CACHE_KEY, avatars, timeout=300)

    return avatars

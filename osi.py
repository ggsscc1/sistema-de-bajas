import requests
import re
import sys
import json


def obtain_ids(user):
    response = requests.get('https://www.instagram.com/' + user)
    appid = re.search('appId":"(\d*)', response.text)[1]
    serverid = re.search('server_revision":(\d*)', response.text)[1]

    return appid, serverid


def obtain_user_json(app, server, user):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) 20100101 Firefox/103.0',
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.3',
        'X-Instagram-AJAX': server,
        'X-IG-App-ID': app,
        'X-ASBD-ID': '198337',
        'X-IG-WWW-Claim': '0',
        'Origin': 'https://www.instagram.com',
        'DNT': '1',
        'Alt-Used': 'i.instagram.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.instagram.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Sec-GPC': '1',
    }

    params = {
        'username': user,
    }

    response = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/', params=params, headers=headers)
    print(json.dumps(response.json(), indent=2))


user = "sushitrash"
app_id, server_id = obtain_ids(user)
obtain_user_json(app_id, server_id, user)
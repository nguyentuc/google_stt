# -*- encoding: utf-8 -*-

import requests, urllib


def get_speech(text):
    api = 'https://ailab.hcmus.edu.vn/service/vos'

    data = {u'czt' : u'c828a25de1d', u'text' : text.encode('utf-8')}
    data = urllib.urlencode(data)

    response = requests.post(api, data=data)
    with open('resources/answer.mp3', 'wb') as f:
        f.write(response.content)
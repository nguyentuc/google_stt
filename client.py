import requests
from play_audio import play
from record import record
from stt_ailab import get_speech
import utils


utils.mkdir('resources')

# api = 'http://devopenai.topica.vn:11119/get_stt'
api = 'http://0.0.0.0:11119/get_stt'

while True:
    # record()
    with open('resources/question.wav', 'rb') as f:
        audio = f.read()

    r = requests.post(api, files={'file':audio})
    try:
        answer = unicode(r.content)
    except:
        answer = unicode(r.content, encoding='utf-8')
    print(u'answer: %s' % (answer))
    # get_speech(answer)
    # play()
    break
# server side
# -*- encoding: utf-8 -*-

import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

import bot_brain
from pydub import AudioSegment

os.environ[
    'GOOGLE_APPLICATION_CREDENTIALS'] = '/home/tucng/Desktop/Topica/google_speech_to_text/google_stt/service-account-file.json'

# Instantiates a client
client = speech.SpeechClient()

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code='vi')


def get_content_test():
    # record()
    with open('resources/answer.mp3', 'rb') as f:
        audio_content = f.read()

    audio = types.RecognitionAudio(content=audio_content)
    # Detects speech in the audio file
    try:
        response = client.recognize(config, audio)
        questions = []
        for result in response.results:
            questions.append(unicode(result.alternatives[0].transcript))
        text = bot_brain.get_response(u'\n'.join(questions))
    except:
        text = 'Không lấy được nội dung do tín hiệu quá yếu'

    try:
        answer = unicode(text)
    except:
        answer = unicode(text, encoding='utf-8')
    print answer
    pathOut = 'resources/answer.txt'
    fOut = open(pathOut, "w")
    fOut.write("%s\n" % answer.encode('utf-8'))


def get_content(folder, text_content, path_record_file):
    # record()
    with open(path_record_file, 'rb') as f:
        audio_content = f.read()

    audio = types.RecognitionAudio(content=audio_content)
    # Detects speech in the audio file
    try:
        response = client.recognize(config, audio)
        questions = []
        for result in response.results:
            questions.append(unicode(result.alternatives[0].transcript))
        text = bot_brain.get_response(u'\n'.join(questions))
    except:
        text = 'Không lấy được nội dung do tín hiệu quá yếu'

    try:
        answer = unicode(text)
    except:
        answer = unicode(text, encoding='utf-8')
    print answer
    pathOut = folder + '/' + text_content
    fOut = open(pathOut, "w")
    fOut.write("%s\n" % answer.encode('utf-8'))


def get_audio_file(dataset):
    stack = os.listdir(dataset)
    if len(stack) > 0:
        for file_name in stack:
            file_path = dataset + '/' + file_name

            print 'Loading data in ' + file_path
            record_folder = os.listdir(file_path)
            if len(record_folder) > 0:
                for record_file in record_folder:
                    if 'wav' in record_file:
                        name_record_file = record_file.split('wav')
                        text_content = name_record_file[0] + 'txt'
                    path_record_file = file_path + '/' + record_file
                    print 'Getting content in :', path_record_file
                    # check length of audio_file
                    audio = AudioSegment.from_file(path_record_file)
                    if audio.duration_seconds < 300: # only get content for audio less than 5 minutes.
                        get_content(file_path, text_content, path_record_file)
    return


get_audio_file(dataset='Record')

from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg
import os
import re

desktop = os.path.expanduser('~/Desktop')

sg.theme('LightGrey1')

layout = [
    [sg.Text('URL Vídeo Youtube'), sg.Input(key='url')],
    [sg.Radio('MP3', "RADIO1", default=True, key='mp3'), sg.Radio('MP4', "RADIO1", key='mp4')],
    [sg.Button('Converter'), sg.Button('Cancelar')]
]

window = sg.Window('Youtube Conversor MP3/MP4', layout)

def remove_special_characters(string):
    return re.sub(r'[^a-zA-Z0-9\s]', '', string)

def is_youtube_url(url):
    youtube_regex = re.compile(r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+')
    return youtube_regex.match(url) is not None

while True:
    event, values = window.read()

    url_validation = is_youtube_url(values['url'])

    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    
    elif event == 'Converter' and url_validation == False:
        sg.popup_ok('URL INVÁLIDA!')

    elif event == 'Converter' and url_validation:
        video = YouTube(values['url'])
        stream = video.streams.get_highest_resolution()

        if values['mp4'] == True:
            stream.download()
            sg.popup_ok('Download Concluído com Sucesso!')

        elif values['mp3'] == True:
            stream.download(filename='video.mp4')
            os.system(f'ffmpeg -i video.mp4 output.mp3')
            os.rename('output.mp3', f'{remove_special_characters(video.title)}.mp3')
            os.remove('video.mp4')
            sg.popup_ok('Download Concluído com Sucesso!')
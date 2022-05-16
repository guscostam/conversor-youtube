from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg
from os import path

desktop = path.expanduser('~/Desktop')

sg.theme('LightGrey1')

layout = [
    [sg.Text('URL Vídeo Youtube'), sg.Input(key='url')],
    [sg.Radio('MP3', "RADIO1", default=True, key='mp3'), sg.Radio('MP4', "RADIO1", key='mp4')],
    [sg.Button('Converter'), sg.Button('Cancelar')]
]

window = sg.Window('Youtube Conversor MP3/MP4', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    
    elif event == 'Converter' and 'youtube' not in values['url']:
        sg.popup_ok('URL INVÁLIDA!')

    elif event == 'Converter' and 'youtube' in values['url']:
        video = YouTube(values['url'])

        if values['mp4'] == True:
            stream = video.streams.get_highest_resolution()
            stream.download(output_path=desktop)
            sg.popup_ok('Download Concluído com Sucesso!')

        elif values['mp3'] == True:
            stream = video.streams.get_audio_only()
            video_name = video.title + '.mp3'
            stream.download(output_path=desktop, filename=video_name)
            sg.popup_ok('Download Concluído com Sucesso!')

from pytube import YouTube
from os import path

desktop = path.expanduser('~/Desktop')

while True:
    url = str(input('URL Vídeo do Youtube: '))

    print('-' * 20 + 'MENU' + '-' * 20)
    print('[1] - Download MP4\n[2] - Download MP3')

    video = YouTube(url)

    type_download = 0

    while type_download <= 0 or type_download >= 3:
        type_download = int(input('Escolha uma das Opções: '))

    if type_download == 1:
        stream = video.streams.get_highest_resolution()

        stream.download(output_path=desktop)
        print('Download Concluido com Sucesso!')

    if type_download == 2:
        stream = video.streams.get_audio_only()

        stream.download(output_path=desktop, filename='audio.mp3')
        print('Download Concluido com Sucesso!')

    option = ' '

    while option not in 'SN':
        option = input(str('Quer Continuar? [S/N]: ')).upper()

    if option in 'N':
        break

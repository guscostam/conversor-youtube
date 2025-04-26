import os
import re
from yt_dlp import YoutubeDL

desktop = os.path.expanduser('~/Desktop')

def remove_special_characters(string):
    return re.sub(r'[^a-zA-Z0-9\s]', '', string)

def is_youtube_url(url):
    youtube_regex = re.compile(r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+')
    return youtube_regex.match(url) is not None

def main():
    url = input("Digite a URL do vídeo do YouTube: ").strip()
    if not is_youtube_url(url):
        print("URL INVÁLIDA!")
        return

    print("Escolha o formato de download:")
    print("1. MP3")
    print("2. MP4")
    choice = input("Digite 1 ou 2: ").strip()

    try:
        ffmpeg_path = r'c:\Users\gusco\Desktop\youtube-conversor\ffmpeg.exe'  # Update to the directory containing ffmpeg.exe
        ydl_opts = {}
        if choice == "2":  # MP4
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': f'{desktop}/%(title)s.%(ext)s',
                'ffmpeg_location': ffmpeg_path,
            }
        elif choice == "1":  # MP3
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{desktop}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'ffmpeg_location': ffmpeg_path,
            }
        else:
            print("Opção inválida!")
            return

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download Concluído com Sucesso!")
    except Exception as e:
        print(f"Erro ao processar o vídeo: {e}")

if __name__ == "__main__":
    main()
from pytube import YouTube
from pathlib import Path

def main():
    print("Welcome to Youtube to MP4")
    print("To get started, please enter a youtube link")

    youtube_link = input()

    download_youtube_audio(youtube_link, default_path())

# Downloads just the audio from a youtube video
def download_youtube_audio(yt_link, path):
    yt = YouTube(yt_link) 
    audio_stream = yt.streams.get_audio_only()
    audio_stream.download(path)

#initiates a default download path to the user's download folder
def default_path():
    download_path = Path().home().joinpath("Downloads")
    return download_path

main()
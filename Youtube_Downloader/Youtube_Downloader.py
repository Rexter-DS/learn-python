from pytube import YouTube
from pathlib import Path

def main():
    print("Welcome to Youtube to MP4")
    print("To get started, please enter a youtube link")

    youtube_link = input()

    download_youtube_audio(youtube_link)

# Downloads just the audio from a youtube video
def download_youtube_audio(youtube_link):
    yt = YouTube(youtube_link) 
    audio_stream = yt.streams.get_audio_only()
    audio_stream.download()

main()
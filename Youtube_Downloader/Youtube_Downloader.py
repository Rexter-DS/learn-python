from pytube import YouTube
from pathlib import Path

def main():
    print("Welcome to Youtube to MP4 Converter")

    choice = user_choice()

    if choice is 1:
        download_youtube_video(default_path())
    elif choice is 2:
        download_youtube_audio(default_path())

# Downloads just the audio from a youtube video
def download_youtube_audio(path):
    yt = YouTube("yt_link") 
    audio_stream = yt.streams.get_audio_only()
    audio_stream.download(path)

# Downloads the video 
def download_youtube_video(path):

    yt = YouTube("")
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(path)


def user_choice():
    print("Type 1 or 2 to specify whether you would like to download the full video (with sound) or just the audio")
    
    while True:
        try:
            choice = int(input("Type 1 for video or 2 for audio: "))
        except ValueError:
            print("Invalid option")
            continue
        
        if choice in (1, 2):
            break
        else:
            print("Invalid option")

    return choice

def retry_user_link():
    yt_link = input("Please enter the youtube link: ")
    return yt_link

#initiates a default download path to the user's download folder
def default_path():
    download_path = Path().home().joinpath("Downloads")
    return download_path

main()
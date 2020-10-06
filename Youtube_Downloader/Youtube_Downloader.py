from pytube import YouTube
from pathlib import Path

def main():
    print("Welcome to Youtube to MP4 Converter")
    print("To get started please enter your youtube link")
    youtube_link = input()

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

    if choice == 1:
        print("Something")
    elif choice == 2:
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
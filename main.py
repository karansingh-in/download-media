import requests
import yt_dlp


# for yt videos
URL = ['https://youtu.be/8BhYqOC79M4?si=a2hWyHFNpWbYEaba']
       
with yt_dlp.YoutubeDL() as me:
        me.download(URL)    


# for yt audio
ydl_opts = {
    'format': 'mp3/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URL)

    
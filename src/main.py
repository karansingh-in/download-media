import os
import yt_dlp
from flask import Flask,render_template,request

app = Flask(__name__)

# VIDEO DOWNLOADER 
def yt_in_best(url, quality = "1080"):
    opts = {
         'format': f'bestvideo[height<={quality}]',
    }
 
    with yt_dlp.YoutubeDL(opts) as me:
        me.download([url])

# AUDIO DOWNLOADER 
def audio_from_yt(url):
    ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg_file', 'bin')
    opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_path,    # this should point to the ffmpeg bin path
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',   # downloads video and then extract the audio from it
            'preferredcodec': 'mp3',       # mp3 type is mostly used and compatible with every device
            'preferredquality': '192',     # bitrate of 192
        }],
    }

    with yt_dlp.YoutubeDL(opts) as me:
        me.download([url])

# handling download requests with flask
@app.route("/store", methods=['POST'])
def store():
    data = request.get_json()
    url = data.get('urlInput')
    return url

@app.route("/download_video", methods=['POST'])
def download_video():
    data = request.get_json()
    url = data.get('url')
    yt_in_best(url)
    return {"status": "success"}

@app.route("/download_audio", methods=['POST'])
def download_audio():
    data = request.get_json()
    url = data.get('url')
    audio_from_yt(url)
    return {"status": "success"}

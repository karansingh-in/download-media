import os
import yt_dlp
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# VIDEO DOWNLOADER 
def yt_in_best(url, quality = "1080"):
    opts = {
         'format': f'bestvideo[height<={quality}]',

      #  'format': 'best',
    }
 
    with yt_dlp.YoutubeDL(opts) as me:
        me.download([url])

# AUDIO DOWNLOADER 
def audio_from_yt(url):
    ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg_file', 'bin')
    opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_path,    # set this to your ffmpeg bin path
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',   # downloads video and then extract the audio from it
            'preferredcodec': 'mp3',       # mp3 type is mostly used and compatible with every device
            'preferredquality': '192',     # bitrate of 192
        }],
    }

    
    
    with yt_dlp.YoutubeDL(opts) as me:
        me.download([url])


@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    dtype = data.get('type')  # 'video' or 'audio'

    if not url or dtype not in ('video', 'audio'):
        return {"status": "error", "message": "Invalid input"}, 400

    try:
        if dtype == 'video':
            yt_in_best(url)
        else:
            audio_from_yt(url)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

import os
import yt_dlp
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# finds a connection to downloads folder in the current directory
DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), 'downloads')

# checks if ther is a downloads folder, if not then creates it
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# VIDEO DOWNLOADER 
def yt_in_best(url, quality="1080"):
    opts = {
        'format': f'bestvideo[height<={quality}]',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(opts) as me:
        info = me.extract_info(url, download=True)
        filename = me.prepare_filename(info)
    return filename

# AUDIO DOWNLOADER 
def audio_from_yt(url):
    ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg_file', 'bin')
    opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_path,    # this should point to the ffmpeg bin path
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',   # downloads video and then extract the audio from it
            'preferredcodec': 'mp3',       # mp3 type is mostly used and compatible with every device
            'preferredquality': '192',     # bitrate of 192
        }],
    }

    with yt_dlp.YoutubeDL(opts) as me:
      #  me.download([url])
        info = me.extract_info(url, download=True)
        filename = me.prepare_filename(info)
    return filename    

# handling download requests with flask
# @app.route("/store", methods=['POST'])
# def store():
#     data = request.get_json()
#     url = data.get('urlInput')
#     return url

@app.route("/download_video", methods=['POST'])
def download_video():
    data = request.get_json()
    url = data.get('url')
    filename = yt_in_best(url)
    basename = os.path.basename(filename)
    return send_from_directory(DOWNLOAD_DIR, basename, as_attachment=True)

@app.route("/download_audio", methods=['POST'])
def download_audio():
    data = request.get_json()
    url = data.get('url')
    filename = audio_from_yt(url)
    basename = os.path.basename(filename)
    return send_from_directory(DOWNLOAD_DIR, basename, as_attachment=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
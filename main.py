import os
import yt_dlp

# VIDEO DOWNLOADER FROM YOUTUBE
def yt_in_best(url, quality = "1080"):
    opts = {
        'format': 'best',
    }
 
    with yt_dlp.YoutubeDL(opts) as me:
        me.download([url])


    
# def yt_in_720(url, quality = "720"):
#     opts = {
#         'format': f'best[height<={quality}]/best',
#     }
 
#     with yt_dlp.YoutubeDL(opts) as me:
#         me.download([url])
    
# def yt_in_480(url, quality = "480"):
#     opts = {
#         'format': f'best[height<={quality}]/best',
#     }
 
#     with yt_dlp.YoutubeDL(opts) as me:
#         me.download([url])

# def yt_in_360(url, quality = "360"):
#     opts = {
#         'format': f'best[height<={quality}]/best',
#     }
 
#     with yt_dlp.YoutubeDL(opts) as me:
#         me.download([url])
    
        
# AUDIO DOWNLOADER FROM YOUTUBE
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

# mus = audio_from_yt('https://youtu.be/8BhYqOC79M4?si=XmuPuDNJkifoYUd5')

# vid_best = yt_in_best('https://youtu.be/8BhYqOC79M4?si=XmuPuDNJkifoYUd5')

# vid360 = yt_in_360('https://youtu.be/8BhYqOC79M4?si=XmuPuDNJkifoYUd5')


mus = audio_from_yt('https://pin.it/5iiPy8Bmf')

vid_best = yt_in_best('https://pin.it/5iiPy8Bmf')

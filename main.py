import os
import yt_dlp

# VIDEO DOWNLOADER 
def yt_in_best(url, quality = "1080"):
    opts = {
        'format': 'best',
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


mus = audio_from_yt('https://www.reddit.com/r/interestingasfuck/comments/1dd7fbq/ai_noodle_videos_one_year_later_were_cooked/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button')

vid_best = yt_in_best('https://www.reddit.com/r/interestingasfuck/comments/1dd7fbq/ai_noodle_videos_one_year_later_were_cooked/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button')

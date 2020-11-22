# A simple YouTube downloader with a simple progress indicator
from pytube import YouTube
from pytube.cli import on_progress
import os

def downloadVideo():
     yt_url=input('Please paste the URL of the video you wish to download: ')

     try:
          if type(yt_url)==str:
               yt_video=YouTube(yt_url,on_progress_callback=on_progress)
               yt_video.streams\
                    .filter(file_extension='mp4')\
                    .get_highest_resolution()\
                    .download(os.path.curdir+'/Downloads')
     except EOFError as err:
          print(err)
          downloadVideo()
     else:
          print("Download Successfull!!")

downloadVideo()
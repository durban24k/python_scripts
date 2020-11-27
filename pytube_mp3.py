from pytube import YouTube
from pytube.cli import on_progress
import os

def downloadAudio():
     yt_url=input('Please paste the URL of the video you wish to download: ')
     try:
          if type(yt_url)==str:
               yt_audio=YouTube(yt_url,on_progress_callback=on_progress)
               t=yt_audio.streams.filter(only_audio=True)
               t[0].download(os.path.curdir+'/Downloads/Audio')
     except EOFError as err:
          print(err)
          downloadAudio()
     else:
          print(f'Download Successfull-----')

if __name__ == '__main__':
     downloadAudio()
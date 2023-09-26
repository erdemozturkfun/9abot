from pytube import YouTube

def getAudio(url):
  yt = YouTube(url=url)
 
  return yt

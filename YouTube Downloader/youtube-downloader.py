from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D")

yt.streams \
    .filter(progressive=True, file_extension='mp4') \
    .first() \
    .download()
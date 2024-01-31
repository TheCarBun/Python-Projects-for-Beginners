from pytube import YouTube

link = input("Enter YouTube video link: ")
yt = YouTube(link)
path = "./Downloads"

print("========== Video Details ===========")
print("Video Title : ", yt.title)
print("Views on video : ", yt.views)
print("Channel Name: ", yt.author)
print("====================================")

ch = input("Do you want to download this video?(y/n) ")
if ch == 'y':
    try:
        yd = yt.streams.get_highest_resolution()
        yd.download(path)
    except:
        print("Unable to download the video...")
    else:
        print(f'Video successfully downloaded to {path} folder')
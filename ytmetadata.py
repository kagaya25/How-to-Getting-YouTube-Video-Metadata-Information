from pytube import YouTube

#https://github.com/kagaya25/How-to-Getting-YouTube-Video-Metadata-Information
#pip install pytube
try:
    val = input("Enter your URL: ")
    #yt_obj = YouTube('https://www.youtube.com/watch?v=YwNlVeReXXc') 
    yt_obj = YouTube(str(val))
    print(f'Video Title is {yt_obj.title}')
    print(f'Video Length is {yt_obj.length} seconds')
    print("---------------------------------------------")
    print(f'Video Description is \n {yt_obj.description}')
    print("---------------------------------------------")
    print(f'Video Rating is {yt_obj.rating}')
    print(f'Video Views Count is {yt_obj.views}')
    print(f'Video Author is {yt_obj.author}')
except Exception as e:
    print(e)


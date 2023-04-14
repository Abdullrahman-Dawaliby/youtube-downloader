# youtube-downloader
So Simple YouTube Downloader Programmed In Python

# Feautures:
1.Download From YouTube For Now Only

2.Choose Audio Or Video

3.Shows Quality In Both Audio Or Video 

# Requirements
1.pyhton3 
 Which Can Be Installed Easily In Debian/Ubuntu With:
 ```
 sudo apt install python3 pip3
 ```
 
 Or In Windows You Should Download And Install Python.
 
 2.pytube:
 ```
 pip3 install pytube
 ```
 
 # Running:
 In All Platforms Run Using :
 ```
 python3 ytdl.py
 ```
 You Will Get Output Like This:
 ```
 ➜  ~ python3 ytdl.py    
usage: ytdl.py [-h] [-v] url
ytdl.py: error: the following arguments are required: url
 ```
 
 This Is An Example Of Downloading Song From YouTube :
 ```
 ➜  ~ python3 ytdl.py
Enter the YouTube video URL: http://www.youtube.com/watch?v=Example
Available download options:
1. Video
2. Audio/Song
Enter the number corresponding to the download option you want: 2
Available audio types:
1. 48kbps
2. 128kbps
3. 160kbps
Enter the number corresponding to the audio type you want to download: 3
Downloading audio with name: "The Name Of YouTube Video".mp3
Download finished!
```

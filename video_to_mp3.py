import os
import subprocess
files=os.listdir("video")
b=0
for file in files:
    b=b+1
    subprocess.run(["ffmpeg","-i",f"video/{file}",f"audio/{b}_{file[4:]}.mp3"])

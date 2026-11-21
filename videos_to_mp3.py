#we will convert the mp4 files to mp3 first
import os
import subprocess

files = os.listdir("videos")
for file in files:
    tutorial_number = file.split(".")[0].split(" ｜")[-1]
    tutorial_name = file.split("｜")[0]
    print(tutorial_number, tutorial_name)
    subprocess.run(["ffmpeg","-i" , f"videos/{file}" , f"audio/{tutorial_number}_{tutorial_name}.mp3" ])



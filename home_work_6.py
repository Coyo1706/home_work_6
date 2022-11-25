import os
import shutil


root_direct = input(f"Please enter the full path to the folder to sort the files: ")
try:
    dir = os.listdir(root_direct)
except FileNotFoundError:
    print(f"The path '{root_direct}' does not exist, please make sure it is typed correctly.")
# try:
#     os.mkdir(fr"{root_direct}\video")
#     os.mkdir(fr"{root_direct}\audio")
#     os.mkdir(fr"{root_direct}\archives")
#     os.mkdir(fr"{root_direct}\images")
#     os.mkdir(fr"{root_direct}\documents")
#     os.mkdir(fr"{root_direct}\others")
# except FileExistsError:
#     pass

docs = (".doc", ".docx", ".txt", ".pdf", ".xlxs", ".xlx", ".pptx", ".ppt")
images = (".jpeg", ".png", ".jpg", ".svg")
video = (".avi", ".mp4", ".mov", ".mkv")
audio = (".mp3", ".ogg", ".wav", ".amr")
archives = (".zip", ".rar", ".gz", ".tar")
old_path = list()



for path, direct, files in os.walk(root_direct):
    old_path.append(path)
    for file in files:

        if file.endswith(docs):
            try:
                os.mkdir(fr"{root_direct}\documents")
            except FileExistsError:
                pass
            try:
                shutil.move(path + "\\" + file, fr"{root_direct}\documents") # Запитати як обійтися без try - except
            except shutil.Error:
                pass

        elif file.endswith(images):
            try:
                os.mkdir(fr"{root_direct}\images")
            except FileExistsError:
                pass
            try:
                shutil.move(path + "\\" + file, fr"{root_direct}\images")
            except shutil.Error:
                pass

        elif file.endswith(video):
            try:
                os.mkdir(fr"{root_direct}\video")
            except FileExistsError:
                pass
            try:
                shutil.move(path + "\\" + file, fr"{root_direct}\video")
            except shutil.Error:
                pass

        elif file.endswith(audio):
            try:
                os.mkdir(fr"{root_direct}\audio")
            except FileExistsError:
                pass
            try:
                shutil.move(path + "\\" + file, fr"{root_direct}\audio")
            except shutil.Error:
                pass

        elif file.endswith(archives):
            try:
                os.mkdir(fr"{root_direct}\archives")
            except FileExistsError:
                pass
            try:
                shutil.move(path + "\\" + file, fr"{root_direct}\archives")
            except shutil.Error:
                pass

        else:
            try:
                os.mkdir(fr"{root_direct}\others")
            except FileExistsError:
                pass
            try:
                shutil.move(path + "\\" + file, fr"{root_direct}\others")
            except shutil.Error:
                pass

for path, direct, files in os.walk(root_direct):

    for dir_path in old_path[1::]:
        shutil.rmtree(dir_path, ignore_errors=True)
        """А якщо папка вже була у {root_direct} з назвою video, audio, 
        # etc. Запитати. Можливо реалізувати:
        
            try:
                os.mkdir(fr"{root_direct}\audio")
            except FileExistsError:
                os.mkdir(fr"{root_direct}\audio_sort")
                """


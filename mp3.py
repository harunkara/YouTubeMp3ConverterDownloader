import pafy
import os
import readline
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
print(folder_selected)
while True:
    readline.parse_and_bind("control-v: paste")
    path=folder_selected
    url=input("YouTube şarkı linkini girin:")
    video=pafy.new(url)
    audiostreams=video.audiostreams
    for i in audiostreams:
        print('bitrate: %s, ext: %s, size: %0.2fMb' % (i.bitrate, i.extension,i.get_filesize()/1024/1024))
    

    bestaudio=video.getbestaudio()
    bestaudio.download(filepath=path)



    old_extension = '.webm'
    new_extension = '.mp3'

    files_counter = 0

    with os.scandir(path) as files_and_folders:
        for element in files_and_folders:
            if element.is_file():
                root, ext = os.path.splitext(element.path)
                if ext == old_extension:
                    new_path = root + new_extension
                    os.rename(element.path, new_path)
                    files_counter += 1

    print("Şarkı indirildi")

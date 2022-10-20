from vidstream import *
import tkinter as tk
import socket
import threading
import requests

local_ip_address = socket.gethostbyname(socket.gethostname())

server = StreamingServer(local_ip_address, 9999)
receiver=AudioReceiver(local_ip_address, 8888)
def start_listener():
    t1=threading.Thread(target=server.start_server)
    t2=threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()

def camera():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def screenshare():
    screen_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def audio():
    audio_sender = CameraClient(text_target_ip.get(1.0, 'end-1c'), 6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()
# GUI
win=tk.Tk()
win.title("Calls v0.0.1 Alpha")
win.geometry("300x200")

target_ip=tk.Label(win,text="target device ip: ")
target_ip.pack()

text_target_ip=tk.Text(win,height=1)
text_target_ip.pack()

btn_listen=tk.Button(win,text="Start Listening",width=50,command=start_listener)
btn_listen.pack(anchor=tk.CENTER,expand=True)

btn_cam=tk.Button(win,text="Start Camera Stream",width=50,command=camera)
btn_cam.pack(anchor=tk.CENTER,expand=True)

btn_screen=tk.Button(win,text="Start Screen Sharing",width=50,command=screenshare)
btn_screen.pack(anchor=tk.CENTER,expand=True)

btn_audio=tk.Button(win,text="Start Audio Stream",width=50,command=audio)
btn_audio.pack(anchor=tk.CENTER,expand=True)
win.mainloop()
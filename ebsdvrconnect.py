import cv2
import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk

# RTSP bağlantısı ve video akışını görüntüleme
def stream_video(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)

    def update_frame():
        ret, frame = cap.read()
        if ret:
            # OpenCV'den gelen BGR görüntüyü RGB'ye dönüştür
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk
            label.configure(image=imgtk)
        label.after(10, update_frame)

    update_frame()

# GUI oluşturma
def start_stream():
    rtsp_url = url_entry.get()
    stream_video(rtsp_url)

# Tkinter ile basit GUI oluşturma
root = tk.Tk()
root.title("RTSP Video Stream")

# URL giriş kutusu
label_url = Label(root, text="RTSP URL:")
label_url.pack()
url_entry = Entry(root, width=50)
url_entry.pack()
url_entry.insert(0, "rtsp://rstpipbilgileri")  # Default URL

# Başlat butonu
start_button = Button(root, text="Start Stream", command=start_stream)
start_button.pack()

# Video görüntüsü için label
label = Label(root)
label.pack()

root.mainloop()

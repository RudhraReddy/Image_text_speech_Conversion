import tkinter as tk
from tkinter import *
from gtts import gTTS
from PIL import Image
from tkinter import ttk
from datetime import datetime
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter.filedialog import asksaveasfile


import pytesseract
import tkinter

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\saifr\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
d1 = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")


def img_f():
    txt_file = open('./'+str(d1)+'img_txt_lucii.txt', "w")
    txt_file.write(img_op_p.cget("text"))
    txt_file.close()


def txt_f():
    txt_file = open('./'+str(d1)+'txt_speech_lucii.txt', "w")
    txt_file.write(text_zone.get('1.0', tk.END))
    txt_file.close()


def img_txt_d():
    image1 = filedialog.askopenfilename()
    if image1:
        txt = pytesseract.image_to_string(Image.open(image1))
    img_op_p.config(text=txt)


def img_speech():
    name_info = img_op_p.cget("text")
    print(name_info)
    # language = 'en'
    # myobj = gTTS(text=name_info, lang=language, slow=False)
    # myobj.save(str(d1)+"_Img_Speech_lucii.mp3")


def txt_speech():
    name_info = text_zone.get('1.0', tk.END)
    print(name_info)
    # language = 'en'
    # myobj = gTTS(text=name_info, lang=language, slow=False)
    # myobj.save(str(d1)+"_Txt_Speech_lucii.mp3")


def save_as():
    Files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    asksaveasfile(filetypes=Files, defaultextension=Files)


def txt_Clear():
    text_zone.delete(1.0, END)


def txt_op():
    img_op_p.config(text=text_zone.get(1.0, END))


# Win start
root = tk.Tk()
root.geometry('800x600+500+100')
root.resizable(False, False)
root.configure(background='#212121')
root.title('I-T-S -Lucii')

name = StringVar()

title = tk.Label(
    root, text="Image to Text to Speech", font="Arial 24", bg='white', width=100).pack()

ImgtoTxt = tk.Label(
    root, text="Image to Text", font="Arial 24", fg='white', bg='#212121').place(x=100, y=60)

TxttoSpe = tk.Label(
    root, text="Text to Speech", font="Arial 24", fg='white', bg='#212121').place(x=510, y=60)

# Image Text output
img_op_p = Label(root, text='', font=("Arial 18", 16),
                 fg='#000000', bg='#b1b1b1', width=30, height=10, justify='left')
img_op_p.place(x=20, y=110)

# Text entry zone
text_zone = tk.Text(root, font=("Arial 18", 16), width=30, height=10)
text_zone.place(x=420, y=110)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=text_zone.yview)
scrollbar.place(x=770, y=110, height=244)
text_zone['yscrollcommand'] = scrollbar.set

# Buttons
Img_txt_B = tkinter.Button(
    root, text="Select Image", font="Arial 18", bg='#414141', fg='#ffffff', width=15, command=img_txt_d).place(x=40, y=370)

Img_txt_save_B = tkinter.Button(
    root, text="Generate '.txt' file", font="Arial 18", bg='#414141', fg='#ffffff', width=15, command=img_f).place(x=40, y=435)

Img_spee_B = tkinter.Button(
    root, text="Img to speech", font="Arial 18", bg='#414141', fg='#ffffff', width=15, command=img_speech).place(x=40, y=500)

txt_speech_B = tkinter.Button(
    root, text="Text to Speech", font="Arial 18", bg='#414141', fg='#ffffff', width=15, command=txt_speech).place(x=450, y=370)

txt_save_B = tkinter.Button(
    root, text="Generate '.txt' file", font="Arial 18", bg='#414141', fg='#ffffff', width=15, command=txt_f).place(x=450, y=435)

root.mainloop()

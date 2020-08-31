#!usr/bin/env python3
# -*- encoding:utf-8 -*-

from export_video import create_video
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser

#主窗口
window = tk.Tk()
window.title("Export Video from Blibili")
window.geometry("350x110")

#过滤用户输入
def isnot_qualified(s):
    try:
        if int(s)>0 :
            return False
        else:
            return True
    except ValueError:
        return True

#视频码率输入
vlable = tk.Label(window,text='视频码率：')
vbit = tk.Entry(window, width=10)
vscale = tk.Label(window,text='k')
vlable.grid(row=1,column=0)
vbit.grid(row=1,column=1)
vscale.grid(row=1,column=2)

#音频码率输入
alable = tk.Label(window,text='音频码率：')
abit = tk.Entry(window,width=10)
ascale = tk.Label(window,text='k')
alable.grid(row=2,column=0)
abit.grid(row=2,column=1)
ascale.grid(row=2,column=2)

#编码器选择
clable = tk.Label(window,text='编码器：')
clable.grid(row=3,column=0)
codecombo = ttk.Combobox(window,state='readonly')
codecombo['values'] = ('libx264','h264_qsv','h264_nvenc','h264_amf')
codecombo.current(0)
codecombo.grid(row=3,column=1)

#转换按钮动作
def start_convert():
    video_bitrate = vbit.get()
    audio_bitrate = abit.get()
    codecfun = codecombo.get()
    if isnot_qualified(video_bitrate) :
        vbit.select_clear()
        messagebox.showinfo("Export Video from Blibili", "视频码率错误！")
    elif isnot_qualified(audio_bitrate) :
        abit.select_clear()
        messagebox.showinfo("Export Video from Blibili", "音频码率错误！")
    else:
        create_video(codecfun,video_bitrate,audio_bitrate)
        messagebox.showinfo("Export Video from Blibili", "转换完成！")

#转换按钮
btn = tk.Button(window,text='开始转换',command=start_convert)
btn.grid(row=2,column=4)

#帮助按钮动作
def start_help():
    webbrowser.open("https://github.com/MrZQAQ/bilibili_recoder")
    
#帮助按钮
helpbtn = tk.Button(window,text='点此获取帮助',command=start_help)
helpbtn.grid(row=5,column=4)

if __name__ == '__main__':
    window.mainloop()
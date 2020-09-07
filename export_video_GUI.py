#!usr/bin/env python3
# -*- encoding:utf-8 -*-

from export_video import create_video
from sys import exit
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import webbrowser

class convert_thread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, codecfun, video_bitrate, audio_bitrate):
        threading.Thread.__init__(self)
        self.codecfun = codecfun
        self.video_bitrate = video_bitrate
        self.audio_bitrate = audio_bitrate
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        create_video(self.codecfun, self.video_bitrate, self.audio_bitrate)

def isnot_qualified(s):    #过滤用户输入
    try:
        if int(s)>0 :
            return False
        else:
            return True
    except ValueError:
        return True


class bit_input(tk.Frame):          #封装码率输入fream
    def __init__(self, bit_name, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(bit_name)

    def create_widgets(self, bit_name):
        self.bit_lable = tk.Label(self)
        self.bit_lable["text"] = bit_name
        self.bit_entry = tk.Entry(self)
        self.bit_entry["width"] = "10"
        self.bit_scale = tk.Label(self)
        self.bit_scale["text"] = "k"
        self.bit_lable.pack(side=tk.LEFT)
        self.bit_entry.pack(side=tk.LEFT)
        self.bit_scale.pack(side=tk.LEFT)
    
    def getvar(self):
        return self.bit_entry.get()

class coded_selector(tk.Frame):         #封装编码器选择fream
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.codec_lable = tk.Label(self)
        self.codec_lable["text"] = "编码器 : "
        self.codec_combo = ttk.Combobox(self)
        self.codec_combo["state"] = "readonly"
        self.codec_combo["values"] = ('libx264','h264_qsv','h264_nvenc','h264_amf')
        self.codec_combo["width"] = 10
        self.codec_combo.current(0)
        self.codec_lable.pack(side=tk.LEFT)
        self.codec_combo.pack(side=tk.LEFT)

    def getvar(self):
        return self.codec_combo.get()


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.convert_started = 0
        self.convert = convert_thread('libx264', '2000', '128')
        self.pack()
        self.create_widgets()

    def create_widgets(self):          #创建容器内部各个子组件
        self.input_fream = tk.Frame(self)       #输入子组件
        self.input_fream.pack(side=tk.LEFT)
        self.input_fream.vbitlable = bit_input("视频码率 : ", self.input_fream)      #最上面是视频码率输入
        self.input_fream.abitlable = bit_input("音频码率 : ", self.input_fream)      #音频码率输入
        self.input_fream.codec = coded_selector(self.input_fream)                  #编码器选择

        self.start_btn = tk.Button(self, text="开始转换", command=self.start_convert)       #开始按钮
        self.start_btn.pack(side=tk.LEFT)
        self.help_btn = tk.Button(self, text="帮助", command=self.start_help)           #帮助按钮
        self.help_btn.pack(side=tk.LEFT)

    def start_convert(self):        #开始按钮动作
        if isnot_qualified(self.input_fream.vbitlable.getvar()) :
            messagebox.showinfo("Export Video from Blibili", "视频码率错误！")
        elif isnot_qualified(self.input_fream.abitlable.getvar()) :
            messagebox.showinfo("Export Video from Blibili", "音频码率错误！")
        else:
            if self.convert_started == 1 :
                messagebox.showinfo('Export Video from Blibili','正在转换\n请勿重复点击')
            else:
                self.convert.codecfun = self.input_fream.codec.getvar()
                self.convert.video_bitrate = self.input_fream.vbitlable.getvar()
                self.convert.audio_bitrate = self.input_fream.abitlable.getvar()
                self.convert.start()        #启动转换线程
                self.convert_started = 1        #线程启动标志
                self.after(500,self.convert_done)       #启动线程结束监听

    def start_help(self): 
        webbrowser.open("https://github.com/MrZQAQ/bilibili_recoder")
        
    def convert_done(self):     #检测转换是否完成
        if self.convert_started == 1:
            if self.convert.is_alive() == False :
                self.convert_started = 0
                if messagebox.showinfo('Export Video from Blibili','转换完成！') == 'ok' :
                    exit(0)
        self.after(500,self.convert_done)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Export Video from Blibili")
    root.geometry("350x110")
    app = Application(master=root)
    app.mainloop()


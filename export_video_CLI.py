#!usr/bin/env python3
# -*- encoding:utf-8 -*-

from export_video import create_video

#过滤用户输入
def isnot_qualified(s):
    try:
        if int(s)>0 :
            return False
        else:
            return True
    except ValueError:
        return True

def CLI_encodemode():
    # CLI选择输出模式
    print('选择使用的解编码器(不确定请使用libx264)\n'
                + '1 - libx264模式\n'
                + '2 - intel QSV模式\n'
                + '3 - NVIDIA nvenc模式\n'
                + '4 - AMD VCE模式\n')
    codecnum = input('输入数字选择: ')
    if codecnum == '1':
        codecnum = 'libx264'
    elif codecnum == '2':
        codecnum = 'h264_qsv'
    elif codecnum == '3':
        codecnum = 'h264_nvenc'
    elif codecnum == '4':
        codecnum = 'h264_amf'
    else:
        print('输入错误，程序将以libx264模式运行')
        codecnum = 'libx264'
    return codecnum

def CLI_vbitrate():
    print('\n输入转换后的视频码率(不懂请输入2500)\n')
    video_bitrate = input('视频码率: ')
    while isnot_qualified(video_bitrate) :
        print("请输入大于0的数字！\n")
        video_bitrate = input('视频码率: ')
    return video_bitrate

def CLI_abitrate():
    print('\n输入转换后的音频码率(不懂请输入128)\n')
    audio_bitrate = input('音频码率: ')
    while isnot_qualified(audio_bitrate):
        print("请输入大于0的数字！\n")
        audio_bitrate = input('音频码率: ')
    return audio_bitrate

if __name__ == '__main__':
    print("Export Video from Blibili\n"
          + "Version 1.1.0\n"
          + "https://github.com/MrZQAQ/bilibili_recoder")
    create_video(CLI_encodemode(),CLI_vbitrate(),CLI_abitrate())
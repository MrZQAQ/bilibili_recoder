#!usr/bin/env python3
# -*- encoding:utf-8 -*-

import os
import json
import subprocess


# 读取文件夹内的json文件， 获取文件名称，当前章节
def get_video_information(json_path):
    videoInfo = json.load(open(json_path, 'r', encoding='utf-8'))
    title = videoInfo['title']
    page_data = videoInfo['page_data']['part']
    return title, page_data


def get_file_path(file_path='folder'):
    """
    需要的文件类型： entry.json
    :return:
    """
    file_list = []
    if os.path.exists(file_path):
        for root, dirs, files in os.walk(file_path):
            if 'index.json' in files:
                file_list.append(root)  # root为需要转换的地址
        return file_list
    else:
        print('请检查“folder”文件夹是否存在。并确保要转换的文件夹放置在 folder 文件夹下。')
        return False


def video_add_mp3(file_name, mp3_file, codecfunc, video_bitrate, audio_bitrate, report_name="1"):
    """
     视频添加音频
    :param file_name: 传入视频文件的路径
    :param mp3_file: 传入音频文件的路径
    :param report_name: 导出视频文件名/路径
    :return: True / False
    """
    report_name = report_name if '.' in report_name else report_name + '.mp4'
    try:
        
        subprocess.call('ffmpeg -i ' + file_name    #添加视频流
                        + ' -i ' + mp3_file     #添加音频流
                        + ' -y '    #默认覆盖已有文件
                        + ' -strict -2'     #音频使用AAC编码
                        + ' -vcodec ' + "\"" + codecfunc + "\""     #设置编码器
                        + ' -b:v ' + "\"" + video_bitrate + "k\""   #设置视频码率
                        + ' -b:a ' + "\""+ audio_bitrate + "k\""    #设置音频码率
                        + ' -f mp4 '        #mp4格式输出
                        + "\""+ report_name + "\"", shell=True)
        '''
        print('ffmpeg -i ' + file_name
                        + ' -i ' + mp3_file 
                        + ' -strict -2'
                        + ' -vcodec ' + "\"" + codecfunc + "\""
                        + ' -b:v ' + "\"" + video_bitrate + "\""
                        + ' -b:a ' + "\""+ audio_bitrate + "\""
                        + ' -f mp4 '
                        + "\""+ report_name + "\"")
        '''
        return True
    except:
        return False

def create_video(codecnum,video_bitrate,audio_bitrate):
    file_list = get_file_path()
    if file_list:
        # 获取文件夹正确名称, 名称在上级目录的entry.json中
        for f in file_list:
            f_path = ''
            a = f.split('\\')[:-1]
            for _path in a:
                f_path = os.path.join(f_path, _path)
            f_path = os.path.join(f_path, "entry.json")
            title, page_data = get_video_information(f_path)
            # 创建文件夹
            title = os.path.join('export', title)
            os.makedirs(title, exist_ok=True)
            # 拼接视频文件
            video_add_mp3(os.path.join(f, 'video.m4s'), os.path.join(f, 'audio.m4s'),
                          codecnum,video_bitrate,audio_bitrate,os.path.join(title, page_data + '.mp4'))


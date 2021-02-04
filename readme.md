# bilibili客户端缓存重编码
  
找到手机缓存下来的视频文件夹，它位于
  
    Android/tv.danmaku.bili/download
  
目录下文件夹名称即视频AV号
  
复制你想转换的那个视频文件夹，放入本项目的`folder`文件夹中
  
项目程序有命令行和图形界面两种版本，你可以自由选择

命令行版本以`_CLI`结尾，图形版本以`_GUI`结尾

同时还提供了打包好的exe文件，你可以直接运行它

得到你需要的视频，它位于项目的`export`文件夹

## 下载地址

目前仅在本项目[Releases](https://github.com/MrZQAQ/bilibili_recoder/releases)页面提供下载

## 关于编码器的选择

ffmpeg支持GPU硬件编码加速

对于intel显卡，请使用`h264_qsv`编码器

对于nVidia显卡，请使用`h264_nvenc`编码器

对于AMD显卡，请使用`h264_amf`编码器

如果存在转码问题，请使用`libx264`编码器（较慢）

## 检查更新

双击运行update.exe，自动获取当前最新版本

## 依赖

`webbrowser`  `tkinter`  `requests`
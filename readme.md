# bilibili客户端缓存重编码
  
找到手机缓存下来的视频文件夹，它位于
  
    Android/tv.danmaku.bili/download
  
目录下文件夹名称即视频AV号
  
复制你想转换的那个视频文件夹，放入本项目的`folder`文件夹中
  
项目程序有命令行和图形界面两种版本，你可以自由选择

命令行版本以_CLI结尾，图形版本以_GUI结尾

同时还提供了打包好的exe文件，你可以直接运行它

得到你需要的视频，它位于项目的`export`文件夹

##关于编码器的选择

ffmpeg支持GPU硬件编码加速

对于intel核心显卡，请使用`h264_qsv`编码器

对于nVidia显卡，请使用`h264_nvenc`编码器

对于AMD显卡，请使用`h264_amf`编码器

如果存在转码问题，请使用`libx264`编码器（较慢）

##依赖

`webbrowser`、`tkinter`
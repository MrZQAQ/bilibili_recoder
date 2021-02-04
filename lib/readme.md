# 接口开发规范

更新程序预留了接口，可以配置更新地址
调用程序会通过接口类生成一个对象，调用各个功能

## 输入函数

 `decode_api(api_url)`

 - 返回值类型：布尔，标志是否成功解析

## 输出函数

 `get_version(program_name)`
 - 参数：program_name，字符串类型；示例：`export_video_GUI.exe`
 - 返回值：字符串类型；示例："V1.1.3"
 - 若无此名称对应的版本号，则返回 flase 布尔值

 `get_download_url(program_name)`
 - 参数：program_name，字符串类型；示例：`export_video_GUI.exe`
 - 返回值：字符串类型
 - 若无此名称对应的版本号，则返回 flase 布尔值
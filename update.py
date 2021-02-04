# -*- encoding:utf-8 -*-

import requests
import json
import time
import importlib


def _update_check(config) :
    new_flag = "0"
    update_method = config["update_method"]
    for func in config["update_func"] :
        if  update_method == func["name"] :
            api_url = func["api"]


            module_name = "lib." + str(update_method)
    var_module = importlib.import_module(str(module_name))
    var_class = getattr(var_module, "Remoteinfo")
    info = var_class(api_url)
    if info.decode_api(api_url) :
        for version_info in config["program"] :
            if not(version_info["version"] == info.get_version(version_info["name"])) :
                _get_program_file(info.get_download_url(version_info["name"]),version_info["name"])
                version_info["version"] = info.get_version(version_info["name"])
                new_flag = "1"
    else:
        new_flag = "-1"
    return new_flag

def _get_program_file(url,name):
    name = "./" + str(name)
    program = requests.get(url).content
    with open(str(name), 'wb') as f:
        f.write(program)

def _readconf(file_path):
    try:
        with open(str(file_path),'r') as conf_file :
            return json.load(conf_file)
    except IOError:
        return "-1"

def _saveconf(file_path,config):
    if file_path == "-1":
        config = {"program":[{"name":"export_video_CLI.exe","version":"V1.1.2"},{"name":"export_video_GUI.exe","version":"V1.1.2"}],"update_method":"github","update_func":[{"name":"github","api":"https://api.github.com/repos/MrZQAQ/bilibili_recoder/releases/latest"}]}
        with open("./update_config.json",'w+') as f:
            json.dump(config,f,indent="")
    else:
        with open(str(file_path),'w') as f:
            json.dump(config,f,indent="")

if __name__ == "__main__":
    config = _readconf("./update_config.json")
    if config == "-1":
        print("配置文件缺失，正在获取配置文件……")
        _saveconf("-1",config)
        config = _readconf("./update_config.json")
    print("正在检查更新，请稍侯……")
    check = _update_check(config)
    if check == "1":
        print("更新完成")
        _saveconf("./update_config.json",config)
    elif check == "0" :
        print("软件已是最新")
    else:
        print("更新出错")
    print("3秒后自动关闭窗口……")
    time.sleep(3)



import requests
import json
import time

def _readconf(file_path):
    try:
        with open(str(file_path),'r') as conf_file :
            return json.load(conf_file)
    except IOError:
        return "-1"

def _update_check(config) :
    new_flag = False
    update_method = config["update_method"]
    for func in config["update_func"] :
        if  update_method == func["name"] :
            url = func["api"]
    data = _get_response(url)
    for assets in data["assets"] :
        for version_info in config["program"] :
            if assets["name"] == version_info["name"] :
                if not(data["tag_name"] == version_info["version"]):
                    _get_program_file(assets["browser_download_url"],version_info["name"])
                    version_info["version"] = data["tag_name"]
                    new_flag = True
    if new_flag :
        return True
    else:
        return False

def _get_response(url):
    return requests.get(url).json()

def _get_program_file(url,name):
    name = "./" + str(name)
    program = requests.get(url).content
    with open(str(name), 'wb') as f:
        f.write(program)

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
    if _update_check(config):
        print("更新完成")
        _saveconf("./update_config.json",config)
    else:
        print("软件已是最新")
    print("3秒后自动关闭窗口……")
    time.sleep(3)



from urllib.request import urlopen, Request;import requests
from os import system, mkdir, popen

def get_exact_path(old_path):return popen("echo " + old_path).read().split("\n")[0]
installpath=get_exact_path('%appdata%\\bmts_macro')
def download(url, path):
    filedata = urlopen(url)
    datatowrite = filedata.read()
    with open(path, 'wb') as f:
        f.write(datatowrite)
def get_site_content(url):
    return requests.get(url).content.decode("utf-8") 

def check_installed():
    try: open(installpath+"\\version", 'r').close(); return True
    except: return False

def check_version():
    return open(installpath+"\\version", 'r').read().split("\n")[0]
def check_right_version():
    if check_version() == get_site_content("https://raw.githubusercontent.com/Benomat/macro/main/version").split("\n")[0]: print("everything up to date");return True
    else: return False
def update():
    system("title Updating!")
    print("updating...")
    download("https://github.com/Benomat/macro/releases/download/main/main.exe",installpath+"\\main.exe")
    download("https://raw.githubusercontent.com/Benomat/macro/main/version",installpath+"\\version")


if __name__ == '__main__':
    if check_installed():
        system("title"+check_version)
        if not check_right_version(): update()
        system("title"+check_version)
        print("starting macro")
        system(f"{installpath}\\main.exe")
    else:
        system("title Installing!")
        print("installing..")
        mkdir(installpath)
        download("https://github.com/Benomat/macro/releases/download/main/main.exe",installpath+"\\main.exe")
        download("https://raw.githubusercontent.com/Benomat/macro/main/version",installpath+"\\version")
        system("title"+check_version)
        system(f"{installpath}\\main.exe")
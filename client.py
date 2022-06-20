import ctypes
import sys
import requests
from run import *
import json
from search_server import *


def main():
    try:
        ip_address = fetch_server_ip()
        print(ip_address)
        re = requests.get('http://'+ip_address+':1080/', timeout=5).text
        # print(re)
    except:
        print('can not connect to server')
        exit()

    display_tree(ip_address)
    if len(sys.argv) > 1:
        run_once(sys.argv[1:])
        exit()

    while 1:
        command = input('po:')
        excute_command(ip_address, command)


try:
    with open('config.json')as config_data:
        config_data = json.load(config_data)
except:
    pass


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    while 1:
        try:
            main()
        except Exception as e:
            print(e)
else:
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)

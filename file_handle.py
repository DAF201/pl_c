import base64
import requests
import json
import os
import zipfile


def add_file(ip_address, command):
    files = []
    for file in command[2:]:
        files.append(('files', open(file, 'rb')))
    re = requests.post('http://%s:1080/add' %
                       ip_address, params={'dir': command[1]}, files=files).text
    return re


def del_file(ip_address, command):
    files = []
    for file in command[2:]:
        files.append(file)
    re = requests.post('http://%s:1080/del' %
                       ip_address, params={'dir': command[1], 'files': list(files)}).text
    return re


def archive(ip_address, command):
    local_files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files = []
    for file in local_files:
        if file == os.path.basename(__file__):
            continue
        files.append(('files', open(file, 'rb')))

    re = requests.post('http://%s:1080/archive' %
                       ip_address, params={'dir': command[1]}, files=files).text
    return re


def destroy(ip_address, command):
    re = requests.post('http://%s:1080/destroy' %
                       ip_address, params={'dir': command[1]}).text
    return re


def fetch(ip_address, command):
    re = requests.get('http://%s:1080/fetch' %
                      ip_address, params={'dir': command[1], 'files': command[2:]}).text
    return re


def restore(ip_address, command):
    re = requests.get('http://%s:1080/restore' %
                      ip_address, params={'dir': command[1]}).text
    with open('test.zip', 'wb')as zip:
        zip.write(base64.b64decode(re))
    print(re)
    with zipfile.ZipFile('test.zip', 'r')as zip:
        zip.extractall()
    os.remove('file.json')
    os.remove('test.zip')
    return re

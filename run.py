from urllib import response
import requests
from file_handle import *


def run_once(args):

    for x in args:
        print(x)


def display_tree(ip_address, command='.'):

    re = requests.get('http://%s:1080/log' %
                      ip_address, params={'dir': command}).text
    print(re)


def excute_command(ip_address, command):
    # try:
    command = command.split(' ')

    if command[0] == 'log':
        if len(command) > 1:
            display_tree(ip_address, command[1])
        else:
            display_tree(ip_address)
        return

    if command[0] == 'add':
        if len(command) in [1, 2]:
            print('check syntax')
            return
        re = add_file(ip_address, command)
        print(re)

    if command[0] == 'delete':
        if len(command) in [1, 2]:
            print('check syntax')
            return
        re = del_file(ip_address, command)
        print(re)

    if command[0] == 'fetch':
        if len(command) in [1, 2]:
            print('check syntax')
            return
        re = json.loads(fetch(ip_address, command))
        for key in re.keys():
            with open(key, 'wb')as recieved_file:
                recieved_file.write(base64.b64decode(re[key]))
        print('following files fetched:')
        for file in re.keys():
            print(file)

    if command[0] == 'archive':
        if len(command) != 2:
            print('check syntax')
            return
        re = archive(ip_address, command)
        print(re)

    if command[0] == 'destroy':
        if len(command) != 2:
            print('check syntax')
            return
        re = destroy(ip_address, command)
        print(re)

    if command[0] == 'restore':
        if len(command) != 2:
            print('check syntax')
            return
        re = restore(ip_address, command)
        print(re)
    # except Exception as e:
    #     print(e)

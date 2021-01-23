#-*- coding:utf-8 -*-
import cv2
import numpy as n
import subprocess
import threading
import time
import smbus
def image1():
    #画像読み込み
    img = cv2.imread("testdata/lena.jpg")
    #画像サイズ変更
    img = cv2.resize(img,(800,600))
    #文字表示
    cv2.putText(img, 'hoge hoge', (50,50), cv2.FONT_HERSHEY_SIMPLEX,2.0,(255,0,0),6)
    #画像表示
    cv2.imshow('image',img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    #t=threading.Timer(1,image1)
    #t.start();
def music1():
    subprocess.call("aplay testdata/test.wav",shell=True)
    #t=threading.Timer(1.2,music1)
    #t.start();def music1():
#def SE1():
#    subprocess.call("aplay testdata/test.wav",shell=True)
    #t=threading.Timer(1.2,SE1)
    #t.start();
    
def arduinoS():
        # I2Cの指定
        bus = smbus.SMBus(1)

        # スレーブのアドレス
        adress = 0x04
        
        #msg = chr(bus.read_byte(adress))
        #msg = 'B'
        # 書き込み処理
        msg = input()
        if msg == 'R':  # 当たったら
            bus.write_byte(adress,ord('R'))
        if msg == 'B':  # 
            bus.write_byte(adress,ord('B'))
        if msg == 'G':  # 
            bus.write_byte(adress,ord('G'))
        if msg == 'W':  # 当たらなかったら（ひとまずいらない）
            bus.write_byte(adress,ord('W'))
        
        # 出力
        print(msg)

        # Delay
        time.sleep(1)
        
        t=threading.Timer(1.1,arduinoS)
        t.start()

t1=threading.Thread(target=image1)
#t2=threading.Thread(target=music1)
#t3=threading.Thread(target=SE1)
t4=threading.Thread(target=arduinoS)
t1.start()
#t2.start()
#t3.start()
t4.start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#作成者　くわはら
#作成日　21/01/07
#機能　　忍ズム　センサー　i2c マスター


import smbus                #I2C通信するためのモジュールsmbusをインポートする
import time                 #sleepするためにtimeモジュールをインポートする
from websocket import create_connection
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# 自身のIDを定義
DEVICE_ID = "D0001"

# Firebaseの設定
cred = credentials.Certificate("key/halms-49316-firebase-adminsdk-y7wsu-6a5942aa12.json")

# RealtimeDBの定義
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://halms-49316-default-rtdb.firebaseio.com/'
})

# IPアドレスの取得
ref = db.reference('/devices/' + DEVICE_ID)
server_info = ref.get()


#i2c 　スレーブからの受信
now_t = 0


#速度算出　最初に反応したn番目のセンサー　＋　２回目に反応したn番目のセンサー　/ 　2
farst_sensar        = -1
farst_flg           = 0
farst_time = 0
last_time  = 0
speed = 0
speed_ = 0



def recvSlave(adress):
    recv_t = 0
    bus = smbus.SMBus(1)    ##I2C通信するためのモジュールsmbusのインスタンスを作成
    for i in range(4):
        msg = chr(bus.read_byte(4))
        c = ord(msg)
        #print(c)
        #print(' ')
        for j in range(i):
            c = c << 8
        recv_t |= c

    #print(recv_t)
    #print(' ')
    #time.sleep(0.01)
    return recv_t


# """メイン関数"""
if __name__ == '__main__':
    # ソケットの接続
    ws = create_connection("ws://" + server_info['server'] + ":50000")
    print("サーバ接続")

    while True:
        for i in range(1,10):    #1~9
            now_t = recvSlave(i)
            #print(i,end = ' ')
            #print(now_t)
            
            if farst_flg and i == farst_sensar and now_t:
                last_time = now_t

            if farst_flg and i == farst_sensar and now_t == 0:
                speed     = last_time - farst_time
            
            if now_t and farst_flg == 0:
                farst_sensar = i
                farst_flg    = 1
                farst_time   = now_t
              
        if speed:
        
            if speed > 0 and speed < 1000:
                # print("speed = ",end= ' ')
                # print(speed,end = ' ')
                hit = "R"
                if farst_sensar >= 0 and farst_sensar <= 2:
                      hit = "L"
                elif farst_sensar >= 3 and farst_sensar <= 5:
                      hit = "H"
                # elif farst_sensar >= 6 and farst_sensar <= 8:
                # else:
                #      print("R")

                # ソケットサーバへ送信
                # ws.send(b'hello!')
                ws.send("{\"mode\":\"damage\",\"damage\":\"" + str(speed) + "\",\"hit\":\"" + str(hit) + "\"}")
                # repr(s.recv(1024))
                time.sleep(0.1)
                
            

            farst_sensar = -1
            farst_flg    = 0
            farst_time   = 0
            last_time    = 0
            speed_ = speed
            speed        = 0
    ws.close()



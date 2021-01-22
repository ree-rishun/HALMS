# -*- coding: utf-8 -*-

import websocket
import smbus                #I2C通信するためのモジュールsmbusをインポートする
import time                 #sleepするためにtimeモジュールをインポートする
from websocket import create_connection
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

SLAVE_ADDR = [0x0b, 0x0c, 0x0d]


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


# """メイン関数"""
if __name__ == '__main__':
  # ソケットの接続
  ws = create_connection("ws://" + server_info['server'] + ":50000")
  print("サーバ接続")
  
  while True:
    bus = smbus.SMBus(1)    ##I2C通信するためのモジュールsmbusのインスタンスを作成

    # 全スレーブの値を取得
    for i in range(3):
      damage = bus.read_byte(SLAVE_ADDR[i])
      print(damage)
      
      if damage != 0:
        ws.send("{\"mode\":\"damage_user\",\"damage\":\"" + str(damage) + "\"}")
    time.sleep(2)


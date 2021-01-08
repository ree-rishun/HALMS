from websocket_server import WebsocketServer
import ipget    # pip3 install ipget
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

# 新規クライアント接続時処理
def new_client(client, server):
    print("New client has joined")

# 新規メッセージ受信時処理
def send_msg_allclient(client, server, message):
    print(message)
    server.send_message_to_all(message)

# 自身のIPを取得
host = ipget.ipget().ipaddr("wlan0")
# host = ipget.ipget().ipaddr("eth0")
host_address = host[:host.find('/')]

# IPアドレスをDBへ保存
ref = db.reference('/devices')
users_ref = ref.child(DEVICE_ID)
users_ref.set({
    'server': host_address
})

print(host_address)

# ソケットサーバを作成
server = WebsocketServer(50000, host=host_address)

# 新しいクライアントが接続したときの処理
server.set_fn_new_client(new_client)

# クライアントがメッセージを送信したときの処理
server.set_fn_message_received(send_msg_allclient)
server.run_forever()

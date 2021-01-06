from websocket_server import WebsocketServer
import ipget    # pip3 install ipget

def new_client(client, server):
    print("New client has joined")

def send_msg_allclient(client, server, message):
    server.send_message_to_all(message)

# 自身のIPを取得
host = ipget.ipget().ipaddr("eth0")
host_address = host[:host.find('/')]

print(host_address)

# ソケットサーバを作成
server = WebsocketServer(50000, host=host_address)

# 新しいクライアントが接続したときの処理
server.set_fn_new_client(new_client)

# クライアントがメッセージを送信したときの処理
server.set_fn_message_received(send_msg_allclient)
server.run_forever()
from websocket_server import WebsocketServer

def new_client(client, server):
    print("New client has joined")

def send_msg_allclient(client, server, message):
    server.send_message_to_all(message)

server = WebsocketServer(50000, host='172.20.10.7')

# 新しいクライアントが接続したときの処理
server.set_fn_new_client(new_client)

# クライアントがメッセージを送信したときの処理
server.set_fn_message_received(send_msg_allclient)
server.run_forever()
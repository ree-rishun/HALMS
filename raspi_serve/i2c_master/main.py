# coding: UTF-8

import websocket
import threading
import time
import logging
import json
import smbus
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(' %(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Arduino
SLAVE_RIGHT = 0x04
SLAVE_LEFT  = 0x05
SLAVE_HEAD  = 0x06
bus = smbus.SMBus(1)  

# コールバック関数

# メッセージが届いた際の処理
def on_message(ws, message):
  # 受信内容の出力
  logger.info('Received:{}'.format(message))

  # パース
  msg_obj=json.loads(message)

  print(msg_obj["mode"])
  if msg_obj["mode"] == "damage":
    print('R')
    print(msg_obj["hit"])

    # ヒット箇所によって処理を分岐
    if msg_obj["hit"] == "left":
      bus.write_byte(SLAVE_LEFT,ord('R'))
    elif msg_obj["hit"] == "right":
      bus.write_byte(SLAVE_RIGHT,ord('R'))
    elif msg_obj["hit"] == "head":
      bus.write_byte(SLAVE_HEAD,ord('R'))
    
  elif msg_obj["mode"] == "router":
    print('G')
    bus.write_byte(SLAVE_LEFT,ord('G'))

  else:
    print('W')
    bus.write_byte(SLAVE_LEFT,ord('W'))


# エラー発生時の処理
def on_error(ws, error):
  logger.info('Error:{}'.format(error))

# ソケットが閉じた時の処理
def on_close(ws):
  logger.info('Close')

# ソケットが開いたときの処理
def on_open(ws):
  def run(*args):
    logger.info('Open')
    for i in range(3):
      time.sleep(1)
      message = "Hello " + str(i)
      ws.send(message)
      logger.info('Sent:{}'.format(message))
    time.sleep(1)
    ws.close()
    logger.info('Thread terminating...')
  thread.start_new_thread(run, ())
 

# メイン処理
if __name__ == "__main__":
    #websocket.enableTrace(True)
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://172.20.10.10:50000",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
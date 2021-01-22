from websocket import create_connection
import logging
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(' %(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
 
ws = create_connection("ws://172.20.10.10:50000")
logger.info("Open")
logger.info("Sending 'Hellow, World'...")
ws.send("Hello, World")
logger.info("Sent")
logger.info("Receiving...")
result = ws.recv()
logger.info("Received '{}'".format(result))
ws.close()
logger.info("Close")
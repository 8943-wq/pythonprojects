import asyncio
from json import loads
from pprint import pprint

import websockets
from websockets.legacy.client import WebSocketClientProtocol

ws_adress = "wss://socket.paratic.com/socket.io/?EIO=4&transport=websocket"
ws_USD_TRY_MESSAGE = r'42["joinStream", {"codes": ["USD/TRL"]}]'
async def main():
    
    async with websockets.connect(ws_adress) as ws :
        ws: WebSocketClientProtocol
        
        await ws.recv()
        await ws.send("40")
        
        await ws.recv()
        await ws.recv()
        await ws.recv()
        await ws.send(ws_USD_TRY_MESSAGE)
          
        while True:
            
            data = str(await ws.recv())
            if "spot_pariteler" in data:
                  price = data.split("|")[2]
                  print(price)
            await ws.send("3")
              



        
        
        
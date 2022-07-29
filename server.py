import asyncio
from re import M
from attr import attributes
import websockets
from Client import client_class

CLIENTS = []

async def echo(websocket, path):
    CLIENTS.append(client_class(websocket))
    
    async for message in websocket:
        for i in CLIENTS:
            if i.websocket == websocket:
                currentclient = CLIENTS[CLIENTS.index(i)]


        if message[0:3] == "cdn":
            newname = message.strip("cdn ")
            currentclient.changename(newname)
            
        else:    
            for client in CLIENTS:
                try:
                    await client.websocket.send(currentclient.name+': '+message)
                except:
                    print("\n\nCLient that failed:",client.name)
                    CLIENTS.remove(client)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '192.168.1.80', 8765))

asyncio.get_event_loop().run_forever()
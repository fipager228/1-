import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"воу воу воу! сообщение : {message}")
        await websocket.send(f"ЭХО.. эхо.. эхо   : {message}")

async def main():
    server = await websockets.serve(echo,'localhost',8765)
    print("Сервер запущен")
    await server.wait_closed()

if __name__ == "__main__":
 asyncio.run(main())
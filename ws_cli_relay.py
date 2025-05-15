# ws_cli_relay.py

import asyncio
import websockets
import subprocess

PORT = 8765  # Change as needed

async def handle_connection(websocket, path):
    await websocket.send("🟢 Gilliam WebSocket CLI ready.")
    try:
        async for message in websocket:
            try:
                # Run the command received
                result = subprocess.run(
                    message, shell=True, capture_output=True, text=True
                )
                output = result.stdout if result.stdout else result.stderr
                await websocket.send(f"🟡 $ {message}\n```bash\n{output.strip()}\n```")
            except Exception as e:
                await websocket.send(f"🔴 Error: {str(e)}")
    except websockets.ConnectionClosed:
        print("🔌 Connection closed.")

async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", PORT):
        print(f"🌐 WebSocket CLI server running on ws://0.0.0.0:{PORT}")
        await asyncio.Future()  # Keep the server alive

if __name__ == "__main__":
    asyncio.run(main())

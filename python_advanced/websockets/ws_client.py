#!/usr/bin/env python3

"""Client using the asyncio API."""

import asyncio
from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    async with connect(uri) as websocket:
        await websocket.send("Hello WebSocket")
        message = await websocket.recv()
        print(message, end="")
        return text


if __name__ == "__main__":
    asyncio.run(connect_and_send("ws://localhost:8765", "demo"))

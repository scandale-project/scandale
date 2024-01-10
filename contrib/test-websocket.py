import asyncio
import os
import sys

from fastapi_websocket_pubsub import PubSubClient

PORT = int(os.environ.get("PORT") or "8000")


async def on_events(data, topic):
    print(f"running callback for {topic}!")
    print(data)


async def main():
    # Create a client and subscribe to topics
    client = PubSubClient(["scan", "tst"], callback=on_events)
    client.start_client(f"ws://localhost:{PORT}/pubsub")
    await client.wait_until_done()


asyncio.run(main())

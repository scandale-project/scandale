import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour


class CorrelationEngine(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0

        async def run(self):
            print("Counter: {}".format(self.counter))
            self.counter += 1
            await asyncio.sleep(1)

    async def setup(self):
        print("Agent starting . . .")
        b = self.MyBehav()
        self.add_behaviour(b)


if __name__ == "__main__":
    agent = CorrelationEngine("CE@localhost", "passwordCE")
    future = agent.start()
    future.result()
    agent.web.start(hostname="127.0.0.1", port="10000")

    print("Wait until user interrupts with ctrl+C")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
    agent.stop()

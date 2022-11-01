import time
import getpass
import asyncio
from spade import quit_spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour


class CorrelationEngine(Agent):
    class CollectingBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0

        async def run(self):
            print("Counter: {}".format(self.counter))
            self.counter += 1
            await asyncio.sleep(1)

    async def setup(self):
        print("Agent starting . . .")
        b = self.CollectingBehav()
        self.add_behaviour(b)


if __name__ == "__main__":
    jid = "CE@localhost"
    passwd = getpass.getpass("Password for {}:\n".format(jid))
    agent = CorrelationEngine("CE@localhost", passwd)
    future = agent.start()
    future.result()
    agent.web.start(hostname="127.0.0.1", port="10000")

    print("Web Graphical Interface available at:")
    print("http://127.0.0.1:10000/spade")
    print("Wait until user interrupts with ctrl+C")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
    agent.stop()

    quit_spade()

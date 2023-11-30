import asyncio
import getpass
import time

from spade import quit_spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.behaviour import OneShotBehaviour
from spade.message import Message


class CorrelationEngine(Agent):
    class CollectingBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0

        async def run(self):
            print(f"Counter: {self.counter}")
            self.counter += 1
            await asyncio.sleep(1)

    class SharingBehav(OneShotBehaviour):
        async def run(self):
            print("SharingBehav running")
            msg = Message(to="receiver@your_xmpp_server")  # Instantiate the message
            msg.set_metadata(
                "performative", "inform"
            )  # Set the "inform" FIPA performative
            msg.set_metadata(
                "ontology", "myOntology"
            )  # Set the ontology of the message content
            msg.set_metadata(
                "language", "OWL-S"
            )  # Set the language of the message content
            msg.body = "data"  # Set the message content

            await self.send(msg)
            print("Message sent!")

            # set exit_code for the behaviour
            self.exit_code = "Job Finished!"

            # stop agent from behaviour
            # await self.agent.stop()

    async def setup(self):
        print("Agent starting . . .")
        collecting_behav = self.CollectingBehav()
        self.add_behaviour(collecting_behav)

        self.sharing_behav = self.SharingBehav()
        self.add_behaviour(self.sharing_behav)

        self.presence.set_available()
        self.presence.subscribe("probe2@localhost")


if __name__ == "__main__":
    jid = "correlation-engine@localhost"
    passwd = getpass.getpass(f"Password for {jid}:\n")
    agent = CorrelationEngine(jid, passwd)
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

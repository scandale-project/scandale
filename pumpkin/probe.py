import time
import getpass
import asyncio
from spade import quit_spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message


class CorrelationEngine(Agent):
    class ProbeBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0

        async def run(self):
            await asyncio.sleep(1)

    class InformBehav(OneShotBehaviour):
        async def run(self):
            print("InformBehav running")
            msg = Message(to="CE@localhost")  # Instantiate the message
            msg.set_metadata(
                "performative", "inform"
            )  # Set the "inform" FIPA performative
            msg.set_metadata(
                "ontology", "myOntology"
            )  # Set the ontology of the message content
            msg.set_metadata(
                "language", "OWL-S"
            )  # Set the language of the message content
            msg.body = "Y21WemRXeDBJRzltSUc1dFlYQWdUbE5GSUdadmNpQk5hV05vY205emIyWjBJRVY0WTJoaGJtZGxJRk5sY25abGNpQjJkV3h1WlhKaFltbHNhWFI1"  # Set the message content

            await self.send(msg)
            print("Message sent!")

            # set exit_code for the behaviour
            self.exit_code = "Job Finished!"

            # stop agent from behaviour
            # await self.agent.stop()

    async def setup(self):
        print("Agent starting . . .")
        probe_behav = self.ProbeBehav()
        self.add_behaviour(probe_behav)

        self.InformBehav = self.InformBehav()
        self.add_behaviour(self.InformBehav)


if __name__ == "__main__":
    probe_jid = input("Probe JID> ")
    passwd = getpass.getpass("Password for {}:\n".format(jid))
    agent = CorrelationEngine(probe_jid, passwd)
    future = agent.start()
    future.result()

    # agent.web.start(hostname="127.0.0.1", port="10001")
    # print("Web Graphical Interface available at:")
    # print("http://127.0.0.1:10000/spade")

    print("Wait until user interrupts with ctrl+C")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
    agent.stop()

    quit_spade()

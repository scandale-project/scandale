import time
import getpass
import asyncio
import json
from spade import quit_spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message


def exec_cmd(cmd: str) -> str:
    """Execute a command in a sub process and wait for the result."""
    bash_string = r"""#!/bin/bash
    set -e
    {}
    """.format(
        cmd
    )
    result = subprocess.check_output(
        bash_string, shell=True, executable="/bin/bash", text=True, cwd=BASE_DIR
    )
    return result.strip()


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
            try:
                result = exec_cmd(self.config["command"])
            except Exception:
                pass
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
            msg.body = "Y21WemRXeDBJRzltSUUbE5GSUdadmNpQk"  # Set the message content

            await self.send(msg)
            print("Message sent!")

            # set exit_code for the behaviour
            self.exit_code = "Job Finished!"

            # stop agent from behaviour
            # await self.agent.stop()

    async def setup(self):
        print("Agent starting . . .")
        with open('probe-agent.config.json', 'r') as json_file:
                self.config =  json.load(fcc_file)

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

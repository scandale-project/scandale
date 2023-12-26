import argparse
import json
import time
import uuid

import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message

from scandale.utils import exec_cmd


class ProbeEngine(Agent):
    class InformBehav(OneShotBehaviour):
        async def run(self):
            print("InformBehav running")

            # Send a subscription request
            self.presence.subscribe(self.config["up_agent"])

            try:
                result = exec_cmd(self.config["command"])
            except Exception as e:
                print(e)
                result = "Error with the command: "
            # Instantiate the message
            msg = Message(to=self.config["up_agent"])
            msg.set_metadata(
                "performative", "inform"
            )  # Set the "inform" FIPA performative
            msg.set_metadata(
                "ontology", "probeAgentOntology"
            )  # Set the ontology of the message content
            msg.set_metadata(
                "language", "OWL-S"
            )  # Set the language of the message content

            # Set the message content
            scan_uuid = str(uuid.uuid4())
            msg.body = json.dumps(
                {
                    "version": self.config["version"],
                    "format": self.config["format"],
                    "meta": {
                        "uuid": scan_uuid,
                        "ts": int(time.time()),
                        "type": self.config["type"],
                    },
                    "payload": {"row": result.decode()},
                }
            )

            await self.send(msg)
            print("Message sent!")

            # set exit_code for the behaviour
            self.exit_code = 10

    async def setup(self):
        print("Agent starting . . .")

        self.InformBehav = self.InformBehav()
        self.InformBehav.config = self.config
        self.add_behaviour(self.InformBehav)

    def __init__(self, probe_jid, passwd):
        super().__init__(probe_jid, passwd)
        self.config = {}


async def main(config):
    agent = ProbeEngine(config["jid"], config["passwd"])
    agent.config = config
    await agent.start()
    await agent.InformBehav.join()
    print("Stopping agent.")
    await agent.stop()

    # wait until user interrupts with ctrl+C
    # while True:  # not agent.CollectingBehav.is_killed():
    #     try:
    #         await asyncio.sleep(1)
    #     except KeyboardInterrupt:
    #         break

    # assert agent.InformBehav.exit_code == 10


if __name__ == "__main__":
    # Point of entry in execution mode.
    parser = argparse.ArgumentParser(prog="probe-agent")
    parser.add_argument(
        "-c",
        "--configuration",
        dest="configuration_file",
        required=True,
        help="Configuration file.",
    )

    arguments = parser.parse_args()

    with open(arguments.configuration_file) as json_file:
        config = json.load(json_file)

    spade.run(main(config))

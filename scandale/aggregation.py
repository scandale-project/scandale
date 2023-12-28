import asyncio
import json
import urllib.parse

import requests
import rfc3161ng
import spade
from pydantic import ValidationError
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

from api.schemas import ScanDataCreate

try:
    from instance import config
except Exception:
    from instance import example as config


CERTIFICATE = open(config.CERTIFICATE_FILE, "rb").read()
RT = rfc3161ng.RemoteTimestamper(config.REMOTE_TIMESTAMPER, certificate=CERTIFICATE)


class AggregationEngine(Agent):
    class CollectingBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour...")

            self.headers_json = {
                "Content-Type": "application/json",
                "accept": "application/json",
            }
            self.headers_octet_stream = {
                "Content-Type": "application/octet-stream",
                "accept": "application/json",
            }

        async def run(self):
            msg = await self.receive(timeout=10)  # Wait for a message for 10 seconds
            if msg:
                print(f"Message received with content: {msg.body}")
                try:
                    # Convert the JSON string to a JSON object
                    dict_msg = json.loads(msg.body)
                    # Validate the format with Pydantic
                    ScanDataCreate(**dict_msg)
                except json.decoder.JSONDecodeError:
                    return
                except ValidationError:
                    return
                # TimeStampToken (TST, see RFC 3161)
                tst = RT.timestamp(data=dict_msg["payload"]["row"])
                dict_tst = str(
                    {
                        "tst": tst,
                        "scan_uuid": dict_msg["meta"]["uuid"],
                    }
                )

                try:
                    requests.post(
                        urllib.parse.urljoin(config.API_URL, "items/"),
                        json=dict_msg,
                        headers=self.headers_json,
                    )
                except requests.exceptions.ConnectionError as e:
                    print(
                        f"Error when sending POST request to the FastAPI server:\n{e}"
                    )
                try:
                    requests.post(
                        urllib.parse.urljoin(config.API_URL, "TimeStampTokens/"),
                        data=dict_tst,
                        headers=self.headers_octet_stream,
                    )
                except requests.exceptions.ConnectionError as e:
                    print(
                        f"Error when sending POST request to the FastAPI server:\n{e}"
                    )
            else:
                print("Did not received any message after 10 seconds")

        def on_subscribed(self, jid):
            print(
                "[{}] Agent {} has accepted the subscription.".format(
                    self.agent.name, jid.split("@")[0]
                )
            )
            print(
                "[{}] Contacts List: {}".format(
                    self.agent.name, self.agent.presence.get_contacts()
                )
            )

        def on_subscribe(self, jid):
            print(
                "[{}] Agent {} asked for subscription. Let's aprove it.".format(
                    self.agent.name, jid.split("@")[0]
                )
            )
            self.presence.approve(jid)

    async def setup(self):
        print("Agent starting . . .")
        collecting_behav = self.CollectingBehav()
        self.add_behaviour(collecting_behav)

        self.presence.set_available()
        # self.presence.subscribe("probe1@localhost")


async def main():
    # do not forget to configure OMEMO
    jid = "correlation-engine@localhost"
    passwd = "securePasswordforCE"  # getpass.getpass(f"Password for {jid}:\n")
    agent = AggregationEngine(jid, passwd)
    await agent.start()

    print("Contacts:")
    contacts = agent.presence.get_contacts()
    for contact in contacts:
        print(f"  {contact}")

    await agent.web.start(hostname="127.0.0.1", port="10000")
    print("Web Graphical Interface available at:")
    print("  http://127.0.0.1:10000/spade")
    print("Wait until user interrupts with ctrl+C")

    # wait until user interrupts with ctrl+C
    while True:  # not agent.CollectingBehav.is_killed():
        try:
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break

    assert agent.CollectingBehav.exit_code == 10

    await agent.stop()


if __name__ == "__main__":
    spade.run(main())

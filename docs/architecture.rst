Architecture
============


.. mermaid::

    flowchart LR

    P[Probe] -->|Standardized result| A(Aggregation Engine with cyclic behaviour)
    P1[Probe] -->|Standardized result| A
    P2[Probe] -->|Standardized result| A

    A -.->|Ask for a timestamp| RTS(Remote timestamper *for example: freetsa.org*)

    P -.-> H[Agents registry]
    P1 -.-> H
    P2 -.-> H
    A -.-> H

    A -->|HTTP POST| B[FastAPI]
    A -->|Send| M[Ad hoc module]
    B -.->|Ask for a timestamp| RTS
    B -->|Write| G[Database]
    E[External source] -->|HTTP POST| B


In summary, the outlined architecture operates as follows:
Probes efficiently gather data through localized scans conducted at diverse locations.
The aggregation engine is tasked with consolidating data from these probes and generating cryptographic timestamps in adherence to RFC 3161 standards.
Powered by FastAPI, the API offers a range of services for the storage and retrieval of checks (scans, etc.), and the proof of checks.

An early demonstation is available on Youtube:
https://www.youtube.com/watch?v=eW9y5KWcXhE


The responsibility of the different components is explained in detail below.

The project's changelog, detailing its updates, can be accessed
`here <https://github.com/scandale-project/scandale/blob/main/CHANGELOG.md>`_.


API
===

The core part of the API is responsible of collecting,
verifying the format of the data (with `Pydantic <https://pydantic.dev>`_)
and to provide different ways to access the results from the various
scanning tools.

The API is based on the `FastAPI <https://fastapi.tiangolo.com>`_ framework
well known for its excellent performance.

The OpenAPI documentation is available in :ref:`this section <http-api>`.

The API also provides a PubSub mechanism.


Type of agents
==============

Each agent is authenticated, registered and declare its availability
(for the presence notification system).

``Ad hoc module``: a module in order to share data with external platforms,
such as MISP :footcite:p:`10.1145/2994539.2994542` or other database systems.


Each agent has the possibility to provide a HTML view and different services.


Aggregation Engine
------------------

Time-Stamp Protocol (TSP) RFC 3161
``````````````````````````````````

This main responsibility of this agent is to collect data from the
different scanning tools.
This agent is as well responsible of timestamping the collected data
by using a third party provider (see `RFC 3161 <https://www.ietf.org/rfc/rfc3161.txt>`_).


Probe agent
-----------

The probe agent is responsible of:

- embedding different scanning tools (probes);
- normalizing and verifying the format of analysis tools output;
- transferring the standardized data to the aggregation engine.


Configuration file of a probe agent:

.. code-block:: json

   {
      "uuid": "",
      "period": 3600,
      "target": "",
      "command": "<-how-to-launch-the-scanning-tool>",
      "args": [],
      "result_parser": "",
      "up_agent": ""
   }



One shot
````````

A one shot probe agent can be launched for a ponctual task.
For example a task triggered by an action of a user via a
graphical user interface.
A agent is able to manage a list of jobs. For an important
number of jobs it is possible to launch several agents in parallel.


Periodic
````````

An agent capable of executing a specific task at a scheduled ``period``.




Screenshots
===========

.. figure:: _static/01-behaviour-page.png
   :alt: List behaviours of the Correlation Engine

   List behaviours of the Correlation Engine


.. figure:: _static/02-list-of-messages.png
   :alt: Messages received by the Correlation Engine

   Messages received by the Correlation Engine from various probes.


.. figure:: _static/03-presence-notification.png
   :alt: Presence notification

   Presence notification


.. figure:: _static/04-contact-details.png
   :alt: Some details about a contact of the Correlation Engine.

   Some details about a contact of the Correlation Engine.


.. footbibliography::

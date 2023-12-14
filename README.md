# Pumpkin

## Presentation

[Pumpkin](https://github.com/scandale-project/pumpkin),
is a libre software which is providing a backend architecture
for collecting data from probes and storing proof of checks.

The platform is providing:

- a documenteted HTTP API connected to an aggregation engine;
- connection with a database (PostgreSQL);
- the aggregation engine also provides a PubSub mechanism;
- a backend to deploy and monitor a network of probes with the
  [Smart Python Agent Development Environment](https://github.com/javipalanca/spade);
- ``Ad hoc module``: a module in order to share data with external platforms,
  such as MISP or other database systems.

The API is based on the [FastAPI](https://fastapi.tiangolo.com) framework
well known for its excellent performance.


```mermaid
flowchart LR

P[Probe with periodic behaviour] -->|Standardized result| A(Aggregation Engine with cyclic behaviour)
P1[Probe with cyclic behaviour] -->|Standardized result| A
P2[Probe with one shot behaviour] -->|Standardized result| A
E[External source] -->|HTTP POST| A

A -.->|Ask for a timestamp| RTS(Remote timestamper *for example: freetsa.org*)

A -->|HTTP POST| B[FastAPI]
A -->|Send| M[Ad hoc module]
B -.->|Ask for a timestamp| RTS
B -->|Write| G[Database]

P -.-> H[Agents registry]
P1 -.-> H
P2 -.-> H
A -.-> H
```

The aim of this rather complex example is to show what is currently possible
to do. You can install an aggregation engine with only one probe
on the same server. But probes can be deployed on a large scale and use a
behavioral mechanism to accomplish their duty.

A probe can reason locally or globally.
The selection of the communication channel between probes is automatic,
based on the probes duties, behaviour and availability. A probe do not
need to know the IP server of an other component of the architecture
(database, aggregation engine, etc.).

Each probe agent is authenticated, registered and declare its availability
(for the presence notification system). The OMEMO protocol can be used for
communications between agents.

![Behabiour page](docs/_static/01-behaviour-page.png "Behabiour page")


## Documentation

A documentation is available [here](https://pumpkin-project.readthedocs.io).


## License

`Pumpkin` is distributed under the terms of the
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html).

- Copyright (C) 2022-2023 [Cédric Bonhomme](https://www.cedricbonhomme.org)
- Copyright (C) 2022-2023 CIRCL - Computer Incident Response Center Luxembourg

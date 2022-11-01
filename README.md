# Pumpkin - The MAS Demonic Surveillance Platform 🎃

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)


```mermaid
flowchart LR

A[Probe with periodic behaviour] -->|JSON formatted result| B(Aggregation)
AA[Probe with cyclic behaviour] -->|JSON formatted result| B
AAA[Probe with one shot behaviour] -->|JSON formatted result| B
B --> C(Correlation Engine with cyclic behaviour)
C -->|Write| D[Database]
C -->|Send| E[Ad hoc module]
F[External source] -->|HTTP POST| C
```


## Installation

### Install an XMPP server

To choose an XMPP server, visit this [page](https://xmpp.org/software/servers.html).

To create a new XMPP account you can follow the steps
[here](https://xmpp.org/getting-started/).
Create an XMPP account for each demon.  


## License

`pumpkin` is distributed under the terms of the
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html).

Copyright (C) 2022 [Cédric Bonhomme](https://www.cedricbonhomme.org)
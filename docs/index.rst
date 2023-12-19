SCANDALE
========

Presentation
------------

`SCANDALE <https://github.com/scandale-project/scandale>`_, is a libre software which is providing a backend architecture
for collecting data from probes and storing proof of checks (cryptographic timestamping).

The platform is composed of:

- a documented HTTP API with a PubSub mechansim and a connection to a
  database;
- a backend to deploy and monitor a network of probes.
  The architecture is relying on the
  `Smart Python Agent Development Environment <https://github.com/javipalanca/spade>`_;
- a service to timestamp the collected data with a third party
  (`RFC 3161 <https://www.ietf.org/rfc/rfc3161.txt>`_) for the proof of checks.

It is possible to extend the platform in order to share data with external
system, such as MISP.


.. toctree::
   :caption: Conceptual considerations
   :maxdepth: 3
   :hidden:

   architecture
   formats


.. toctree::
   :caption: Technical considerations
   :maxdepth: 3
   :hidden:

   installation
   deployment


.. toctree::
   :caption: Bibliography
   :maxdepth: 3
   :hidden:

   references


License
-------

SCANDALE is licensed under
`GNU Affero General Public License version 3 <https://www.gnu.org/licenses/agpl-3.0.html>`_.

- Copyright (C) 2022-2023 `Cédric Bonhomme <https://www.cedricbonhomme.org>`_
- Copyright (C) 2022-2023 `CIRCL - Computer Incident Response Center Luxembourg <https://www.circl.lu>`_

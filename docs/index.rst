Pumpkin
=======

Presentation
------------

Pumpkin, is a libre software which is providing a backend architecture
for collecting data from probes and storing proof of checks.

The platform is providing:

- a documented HTTP API connected to an aggregation engine;
- connection with a database (PostgreSQL) through the HTTP API;
- a service to timestamp the collected data with a third party
  (`RFC 3161 <https://www.ietf.org/rfc/rfc3161.txt>`_);
- the aggregation engine also provides a PubSub mechanism;
- a backend to deploy and monitor a network of probes (scanning tools) with the
  `Smart Python Agent Development Environment <https://github.com/javipalanca/spade>`_.


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

Pumpkin is licensed under
`GNU Affero General Public License version 3 <https://www.gnu.org/licenses/agpl-3.0.html>`_.

.. Pumpkin documentation master file, created by
   sphinx-quickstart on Wed Nov  2 12:56:50 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Pumpkin
=======

Presentation
------------

Pumpkin, is a libre software which is providing a
**backend architecture** for collecting data from probes and storing proof
of checks.

The platform is providing:

- a documenteted HTTP API connected to an aggregation engine;
- connection with a Kvrocks database;
- the aggregation engine also provides a PubSub mechanism;
- a backend to deploy and monitor a network of probes with the
  `Smart Python Agent Development Environment <https://github.com/javipalanca/spade>`_;
- ``Ad hoc module``: a module in order to share data with external platforms,
  such as MISP or other database systems.


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

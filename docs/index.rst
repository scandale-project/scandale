.. SCANDALE documentation master file, created by
   sphinx-quickstart on Mon Nov 14 10:51:52 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

scanDALE's documentation
========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Components
----------

Backend:

- probes for variety of checks. Example: https://github.com/scandale-project/ms-exchange-version-nse
- kvrocks, (VAST ?)
- network of workers to gather and normalise information (https://github.com/scandale-project/pumpkin)
- API for connection to external sources of data


Frontend:

- Flask web app (with Celery)
- PostgreSQL, redis.



License
-------

scanDALE is licensed under
`GNU Affero General Public License version 3 <https://www.gnu.org/licenses/agpl-3.0.html>`_.



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Installation
============

Install PostgreSQL
------------------

.. code-block:: bash

    $ sudo apt install postgresql


FastAPI
-------

.. code-block:: bash

    $ poetry install

This will install FastAPI with its dependencies and SPADE.


.. code-block:: json

    $ uvicorn api.main:app
    INFO:     Started server process [18716]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

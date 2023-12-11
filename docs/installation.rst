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

    $ uvicorn main:app --reload
    INFO:     Will watch for changes in these directories: ['/home/cedric/git/SCANDAL/pumpkin/api']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [19750] using WatchFiles
    INFO:     Started server process [19752]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

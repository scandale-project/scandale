Formats
=======

Kvrocks
-------

Format of the data:


.. code-block:: json

    {
        "version": "1",
        "format": "scanning",
        "meta": {
            "uuid": "<UUID>",
            "ts": "date",
            "type": "nmap-scan",
            "",
        },
        "payload": {
            "row": "<base64-encoded-string>"
        }
    }



HTTP API
--------

Documentation is OpenAPI Specification v3.1.0 compliant.


.. code-block:: json

    $ uvicorn main:app --reload
    INFO:     Will watch for changes in these directories: ['/home/cedric/git/SCANDAL/pumpkin/api']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [19750] using WatchFiles
    INFO:     Started server process [19752]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

`FastAPI <https://fastapi.tiangolo.com>`_ is used.  
For production you can use `Uvicorn <https://www.uvicorn.org>`_. It's up to you.



POST operation
``````````````

/api/v1/items

Returns the checksum of the newly created data and timestamp.


GET operation
`````````````

/api/v1/items/payload_checksum



Agent configuration
-------------------

.. code-block:: json

    {
        "uuid": "",
        "period": 3600,
        "target": "",
        "command": "",
        "args": [],
        "up_agent": ""
        "jid": "",
        "passwd": ""
    }




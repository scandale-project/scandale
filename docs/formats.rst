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




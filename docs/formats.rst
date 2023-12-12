Formats
=======

Data from the scans
-------------------

Data from the various scanning tools is stored to the following format.


.. code-block:: json

    {
        "version": "1",
        "format": "scanning",
        "meta": {
            "uuid": "<UUID>",
            "ts": "date",
            "type": "nmap-scan"
        },
        "payload": {
            "row": "<base64-encoded-string>"
        }
    }


As defined `here <https://github.com/scandale-project/pumpkin/blob/main/api/schemas.py>`_.
Validation of the format is made with `Pydantic <https://pydantic.dev>`_.


HTTP API
--------

`FastAPI <https://fastapi.tiangolo.com>`_ is used.
For production you can use `Uvicorn <https://www.uvicorn.org>`_. It's up to you.

OpenAPI documentation
`````````````````````

Documentation is OpenAPI Specification v3.1.0 compliant.

.. openapi:: _static/openapi.json




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

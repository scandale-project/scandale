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


As defined `here <https://github.com/scandale-project/scandale/blob/main/api/schemas.py>`_.
Validation of the format is made with `Pydantic <https://pydantic.dev>`_.
The base64 encoded string is the raw output from a scanning tool.


.. _http-api:

HTTP API
--------

The API is based on the `FastAPI <https://fastapi.tiangolo.com>`_ framework.


OpenAPI documentation
`````````````````````

Documentation is OpenAPI Specification v3.1.0 compliant.

.. openapi:: _static/openapi.yaml




Agent configuration
-------------------

.. code-block:: json

    {
        "uuid": "",
        "period": 3600,
        "target": "",
        "command": "",
        "args": [],
        "expected_value": "",
        "up_agent": ""
        "jid": "",
        "passwd": ""
    }

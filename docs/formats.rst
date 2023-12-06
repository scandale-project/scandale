Formats
=======

Kvrocks
-------

Format of the data


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

POST operation
``````````````

/api/v1/data

Returns the checksum of the newly created data and timestamp.

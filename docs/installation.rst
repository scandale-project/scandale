Installation
============

Install kvrocks
---------------

Follow the steps here:  
https://github.com/apache/kvrocks


FastAPI
-------

.. code-block:: bash

    $ poetry install

This will install FastAPI, the Redis client and SPADE.


Deployment of the Agent platform
--------------------------------

Choose an XMPP server. Visit this [page](https://xmpp.org/software/servers.html).
We mainly tested with [Prosody](https://prosody.im).

To create a new XMPP account you can follow the steps
[here](https://xmpp.org/getting-started/).  
Create an XMPP account for each demon.
Each demon will have a different JID and a different password.

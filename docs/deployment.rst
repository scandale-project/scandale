Deployment
==========

Deployment of the Agent platform
--------------------------------

Choose an XMPP server. Visit this [page](https://xmpp.org/software/servers.html).
We mainly tested with [Prosody](https://prosody.im).

To create a new XMPP account you can follow the steps
[here](https://xmpp.org/getting-started/).  
Create an XMPP account for each demon.
Each demon will have a different JID and a different password.

Main steps:

- installation of the server;
- configuration of the server (OMEMO, etc.);
- creation of the required accounts for the correlation engine and the probes;
- configuration of Pumpkin;
- 

Description of the steps:

.. code-block:: bash

    $ sudo apt install prosody
    $ sudo apt install luarocks
    $ sudo prosodyctl install --server=https://modules.prosody.im/rocks/ mod_omemo_all_access


Generation of the self-signed certificate:

.. code-block:: bash

    $ openssl genrsa -out /etc/prosody/certs/localhost.key 2048
    $ openssl req -new -x509 -key /etc/prosody/certs/localhost.key -out /etc/prosody/certs/localhost.cert -days 1095

Configure a LocalHost section in ``/etc/prosody/conf.d/localhost.cfg.lua``.


Restart Prosody:

.. code-block:: bash

    $ sudo systemctl restart prosody


Check:

.. code-block:: bash

    $ sudo ss -lnptu | grep lua


Creation of accounts:

.. code-block:: bash

    $ sudo prosodyctl adduser correlation-engine@localhost
    Password: securePasswordforCE

    $ sudo prosodyctl adduser probe1@localhost
    Password: securePasswordforProbe1



Luanching the correlation engine:

.. code-block:: bash

    $ python pumpkin/correlation.py 
    Password for correlation-engine@localhost:

    Agent starting . . .
    Web Graphical Interface available at:
    http://127.0.0.1:10000/spade
    Wait until user interrupts with ctrl+C
    Starting behaviour . . .

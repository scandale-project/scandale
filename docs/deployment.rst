Deployment
==========

Installation of a XMPP communication server.
We will use Prosody.

Main steps:

- installation of the server;
- configuration of the server (OMEMO, etc.);
- creation of the required accounts for the correlation engine and the probes;
- configuration of Pumpkin;
- 

Description of the steps:


$ sudo apt install prosody
$ sudo apt install luarocks
$ sudo prosodyctl install --server=https://modules.prosody.im/rocks/ mod_omemo_all_access

confirure /etc/prosody/conf.d/localhost.cfg.lua

$ systemctl status prosody


$ sudo ss -lnptu | grep lua


$ sudo prosodyctl adduser ce@localhost
securePasswordforCE

$ sudo prosodyctl adduser probe1@localhost
securePasswordforProbe1

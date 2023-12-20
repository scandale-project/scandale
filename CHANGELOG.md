# SCANDALE project news


## 0.2.0 (not yet released)

The HTTP API is now providing several endpoints related
to the timestamp tokens. An endpoint to receive new
tokens, an endpoint to check the validity of a token by
passing the UUID of a scan as a parameter. And finally,
an endpoint to verify the timestamp of a cryptographic
timestamp token.

The aggregation engine can collect standardized data from
the probe agents and generate a cryptographic timestamp
token. The aggregation engine uses the HTTP API in order
to store the collected data and the timestamp tokens.

No notable changes related to the probe agents.


## 0.0.1 (2023-12-13)

First working prototype with the API and the first SPADE agents.

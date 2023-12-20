# SCANDALE project news


## 0.1.0 (2023-12-20)

The HTTP API is now providing several endpoints related
to the timestamp tokens (RFC 3161). First, an endpoint to
receive new tokens. Another endpoint to check the validity
of a token by passing as parameter the UUID of a scan.
And finally, an endpoint to verify the timestamp of a
cryptographic timestamp token.

The aggregation engine can collect standardized data from
the probe agents and generate a cryptographic timestamp
token. It uses the HTTP API in order to store the collected
data and to store the timestamp tokens.

No notable changes related to the probe agents.

Various improvements related to the schemas (Pydantic) and
to the models (SQLAlchemy).


## 0.0.1 (2023-12-13)

First working prototype with the API and the first SPADE agents.

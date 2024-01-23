#!/usr/bin/env python

import typer

from contrib.openapi import openapi_to_json
from contrib.openapi import openapi_to_yaml
from scandale import __version__

app = typer.Typer()


@app.command()
def version():
    print(__version__)


@app.command()
def openapi(format: str):
    if format == "json":
        print(openapi_to_json())
    elif format == "yaml":
        print(openapi_to_yaml())


if __name__ == "__main__":
    app()

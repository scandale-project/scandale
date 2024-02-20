#!/usr/bin/env python
import typer

from contrib.openapi import openapi_to_json
from contrib.openapi import openapi_to_yaml
from typing import Optional
from typing_extensions import Annotated
from scandale import __version__

app = typer.Typer()

__app_name__ = "scandale"

# @app.command()
# def version():
#     print(__version__)

def _version_callback(value: bool):
    print(__version__)
    raise typer.Exit()


@app.command()
def openapi(format: str):
    if format == "json":
        print(openapi_to_json())
    elif format == "yaml":
        print(openapi_to_yaml())


# @app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    app(prog_name=__app_name__)


# def main():




if __name__ == "__main__":
    # typer.run(main)
    # app()
    main()

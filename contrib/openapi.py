import io
import json

import yaml
from fastapi.openapi.utils import get_openapi

from api.main import app


def openapi_to_json():
    """Generates the OpenAPI schema to the JSON format."""
    return get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    )


def openapi_to_yaml():
    """Generates the OpenAPI schema to the YAML format."""
    yaml_s = io.StringIO()
    to_json = openapi_to_json()
    yaml.dump(to_json, yaml_s)
    return yaml_s.getvalue()


if __name__ == "__main__":
    # Point of entry in execution mode
    with open("docs/_static/openapi.json", "w") as f:
        json.dump(openapi_to_json(), f)

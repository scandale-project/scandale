import base64
import subprocess

def exec_cmd(cmd: str = "fortune", working_dir: str = "") -> str:
    """Execute a command in a sub process and wait for the result."""
    bash_string = r"""#!/bin/bash
    set -e
    {}
    """.format(
        cmd
    )
    if not working_dir:
        working_dir = "."
    result = subprocess.check_output(
        bash_string, shell=True, executable="/bin/bash", text=True, cwd=working_dir
    )
    result = result.encode("utf-8")
    base64_result = base64.b64encode(result)
    return base64_result

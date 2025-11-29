#!/usr/bin/env python3

import os
import re
import subprocess
from pathlib import Path

def main():
    script_dir = Path(__file__).parent.resolve()
    output_dir_python = script_dir / "python"

    # Ensure the output directory exists
    output_dir_python.mkdir(exist_ok=True)

    # Find all .proto files in the script directory
    proto_files = list(script_dir.glob("*.proto"))
    if not proto_files:
        print("No .proto files found.")
        return

    # Run the gRPC code generator for all proto files
    protoc_cmd = [
        "python", "-m", "grpc_tools.protoc",
        f"-I{script_dir}",
        f"--python_out={output_dir_python}",
        f"--grpc_python_out={output_dir_python}"
    ] + [str(pf) for pf in proto_files]
    subprocess.run(protoc_cmd, check=True)

    # Fix the import paths in the generated Python files
    # (Mimicking what 'sed' did in the Bash script)
    for py_file in output_dir_python.glob("*.py"):
        with py_file.open("r", encoding="utf-8") as f:
            content = f.read()

        # Replace line:
        # import remote_snake_pb2 as remote__snake__pb2
        # with:
        # from . import remote_snake_pb2 as remote__snake__pb2
        new_content = re.sub(
            r"import remote_snake_pb2 as remote__snake__pb2",
            "from . import remote_snake_pb2 as remote__snake__pb2",
            content
        )

        if new_content != content:
            with py_file.open("w", encoding="utf-8") as f:
                f.write(new_content)

    print(f"gRPC Python code generated successfully in {output_dir_python}")

if __name__ == "__main__":
    main()

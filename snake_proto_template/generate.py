#!/usr/bin/env python3

import os
import re
import subprocess
from pathlib import Path

def main():
    script_dir = Path(__file__).parent.resolve()
    proto_file = script_dir / "remote_snake.proto"
    output_dir_python = script_dir / "python"

    # Ensure the output directory exists
    output_dir_python.mkdir(exist_ok=True)

    # Run the gRPC code generator
    # Equivalent to: 
    #   python -m grpc_tools.protoc \
    #       -I {script_dir} \
    #       --python_out={output_dir_python} \
    #       --grpc_python_out={output_dir_python} \
    #       remote_snake.proto
    subprocess.run([
        "python", "-m", "grpc_tools.protoc",
        f"-I{script_dir}",
        f"--python_out={output_dir_python}",
        f"--grpc_python_out={output_dir_python}",
        str(proto_file)
    ], check=True)

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

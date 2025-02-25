#!/bin/bash
# get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

PROTO_FILE="./remote_snake.proto"
OUTPUT_DIR_PYTHON="./python"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR_PYTHON"
python3 -m grpc_tools.protoc -I$(dirname "$PROTO_FILE") --python_out="$OUTPUT_DIR_PYTHON" --grpc_python_out="$OUTPUT_DIR_PYTHON" "$PROTO_FILE"

# Fix the import paths in the generated Python files
sed -i 's/import remote_snake_pb2 as remote__snake__pb2/from . import remote_snake_pb2 as remote__snake__pb2/' "$OUTPUT_DIR_PYTHON"/*.py

echo "gRPC Python code generated successfully in $OUTPUT_DIR_PYTHON"
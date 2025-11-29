#!/bin/bash
# get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

OUTPUT_DIR_PYTHON="./python"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR_PYTHON"

# Find all .proto files in the current directory
PROTO_FILES=(./*.proto)
if [ ${#PROTO_FILES[@]} -eq 0 ]; then
	echo "No .proto files found."
	exit 1
fi

# Run the gRPC code generator for all proto files
python3 -m grpc_tools.protoc -I. --python_out="$OUTPUT_DIR_PYTHON" --grpc_python_out="$OUTPUT_DIR_PYTHON" "${PROTO_FILES[@]}"

# Fix the import paths in the generated Python files
sed -i 's/import remote_snake_pb2 as remote__snake__pb2/from . import remote_snake_pb2 as remote__snake__pb2/' "$OUTPUT_DIR_PYTHON"/*.py

echo "gRPC Python code generated successfully in $OUTPUT_DIR_PYTHON"
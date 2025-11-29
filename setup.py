from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
from pathlib import Path
import subprocess

class CustomBuild(_build_py):
    def run(self):
        # Run the generate.py script before building
        script_path = Path(__file__).parent / 'snake_proto_template' / 'generate.py'
        print(f'Running {script_path}')
        result = subprocess.run(['python', str(script_path)], check=True)
        if result.returncode != 0:
            raise RuntimeError(f"Failed to generate proto files: {result}")
        # Run the original build code
        super().run()

setup(
    name="snake_proto_template",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "grpcio>=1.69.0",
        "protobuf>=5.29.3",
        "grpcio-tools>=1.69.0",
    ],
    cmdclass={
        'build_py': CustomBuild,
    },
)

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
from pathlib import Path
import subprocess

class CustomBuild(_build_py):
    def run(self):
        # Run the original build code
        _build_py.run(self)
        # Run the build.py script
        print('Running generate.py')
        subprocess.run(['python', f'{Path(__file__).parent}/snake_proto_template/generate.py'])

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

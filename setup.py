
from setuptools import setup
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
    cmdclass={
        'build_py': CustomBuild,
    },
)

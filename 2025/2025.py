import os
import subprocess
import sys

current_file = os.path.basename(__file__)
folder = os.getcwd()

for file in os.listdir(folder):
    if file.endswith(".py") and file != current_file:
        print(f"Running day {file.replace('.py','')}")
        print("---------------")
        result = subprocess.run(
            [sys.executable, file],
            capture_output=True,
            text=True
        )
        print(result.stdout)
import os
import subprocess
import sys
from time import perf_counter

current_file = os.path.basename(__file__)
folder = os.getcwd()
time_start = perf_counter()

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
time_end = perf_counter()
print(f'Whole year took {time_end - time_start} seconds')
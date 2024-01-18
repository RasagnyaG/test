import sys
import os

directory = sys.argv[1]

for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                data = file.read()
                print(f"{file} =========> {data}")

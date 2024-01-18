import sys
import os

directory = sys.argv[1]

for root, dirs, files in os.walk(directory):
        for file in files:
            print(file)
            file_path = os.path.join(root, file)
            with open(file, 'r') as file:
                data = file.read()
                print(f"{file} =========> {data}")

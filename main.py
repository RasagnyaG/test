import sys
import os

directory = sys.argv[1]
print(directory)

for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file, 'r') as file:
                data = file.read()
                print(f"{file} =========> {data}")

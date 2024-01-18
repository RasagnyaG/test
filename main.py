import sys

file = sys.argv[1]

with open(file, 'r') as file:
        data = file.read()
        print(f"{file} =========> {data}")

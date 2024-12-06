from pathlib import Path
from time import perf_counter
mvmt = {"(": 1,
        ")": -1}

def get_puzzle(filename):
    file = Path.cwd() / filename
    with file.open("r") as f:
        return f.read()

start_time = perf_counter()
data = get_puzzle("puzzle1")
floor, dep  = 0, 0

# part 1
print(f"destination floor {data.count("(") -data.count(")")}")
time1 = perf_counter() - start_time
print(f"Temps d'exécution part 1: {time1}")

# part 2
for char in data:
    floor += mvmt[char]
    dep += 1
    if floor == -1:
        break
print(f"floor -1 en {dep} déplacement")
time2 = perf_counter() - start_time

print(f"Temps d'exécution part 2: {time2-time1} ")
print(f"Temps total : {time2}")

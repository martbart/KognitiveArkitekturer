import csv
from random import randint

def generate_tests_from_csv(path: str, transform: bool = False) -> tuple[list[list[float]], list[int]]:
    """Generates a list of tests from a csv file."""
    if path[-4:] != ".csv":
        raise ValueError("Path must be a csv file.")
    
    with open(path, 'r') as file:
        reader = csv.reader(file)
        inputs = []
        targets = []
        for row in reader:
            if "#" in row[0]:
                continue
            if transform:
                inputs.append([abs(float(row[0])), abs(float(row[1]))])
                targets.append(int(row[2]))
            else:
                inputs.append([float(row[0]), float(row[1])])
                targets.append(int(row[2]))
    return (inputs, targets)

def generate_tests_or(samples: int) -> tuple[list[list[float]], list[int]]:
    """Generates a list of tests for an OR gate."""
    inputs = []
    targets = []
    for _ in range(samples):
        x = randint(0,100)/100.0
        y = randint(0,100)/100.0
        target = 1 if x > 0.5 or y > 0.5 else 0
        inputs.append([x,y])
        targets.append(target)
    return (inputs, targets)

def main():
    tests = generate_tests_from_csv("KogArk/assign4data.csv")
    print(tests)

if __name__ == "__main__":
    main()
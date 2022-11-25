from naive_bayes import NaiveBayes


def read_data(filepath: str) -> tuple[list[str], list[list[str]]]:
    """ Read data from file. Return criterias and data."""
    data: list[list[str]] = []
    with open(filepath, "r", encoding="UTF-8") as file:
        for line in file:
            data.append(line.strip().split(","))
    return data[0], data[1:]


def main():
    # Read data
    criterias, data = read_data("assignment5/code/data/golf.csv")

    model = NaiveBayes(criterias)

    # Train model
    model.train(data)

    print("Task 5.11".center(100, "-"))

    probabilities = model.probabilites
    for criteria in criterias[:-1]:
        print(f"{criteria}:")
        for value in probabilities[criteria]:
            print(
                f"\tP(Golfing|{value}): {probabilities[criteria][value]['Yes']}")
            print(
                f"\tP(¬Golfing|{value}): {probabilities[criteria][value]['No']}")
    print("Golfing:")
    print(f"\tP(Golfing): {probabilities[criterias[-1]]['Yes']}")
    print(f"\tP(¬Golfing): {probabilities[criterias[-1]]['No']}")

    print("Task 5.12".center(100, "-"))
    day1 = {"Outlook": "Sunny", "Temperature": "Cool",
            "Humidity": "High", "Windy": "True"}
    day2 = {"Outlook": "Overcast", "Temperature": "Mild",
            "Humidity": "Normal", "Windy": "False"}
    day3 = {"Outlook": "Rainy", "Temperature": "Mild",
            "Humidity": "Normal", "Windy": "False"}

    print(f"day1={day1.values()} = {model.predict(**day1)}")
    print(f"day2={day2.values()} = {model.predict(**day2)}")
    print(f"day3={day3.values()} = {model.predict(**day3)}")


if __name__ == "__main__":
    main()

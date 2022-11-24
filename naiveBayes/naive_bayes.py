##  Format: Outlook, Temperature, Humidity, Windy, Play_Golf

from collections import defaultdict


data = []
with open("KogArk/naiveBayes/golf.csv", "r", encoding="UTF-8") as file:
    for line in file:
        data.append(line.strip().split(","))
    del data[0]

probailities_of_outlook = defaultdict(lambda: (0, 0))
probailities_of_temperature = defaultdict(lambda: (0, 0))
probailities_of_humidity = defaultdict(lambda: (0, 0))
probailities_of_windy = defaultdict(lambda: (0, 0))
probailities_of_play_golf = defaultdict(lambda: (0, 0))

for line in data:
    outlook, temperature, humidity, windy, play_golf = line
    probailities_of_outlook[outlook] = (
        probailities_of_outlook.get(outlook, (0,0))[0] + (1 if play_golf == "Yes" else 0), probailities_of_outlook.get(outlook, (0,0))[1] + (1 if play_golf != "Yes" else 0))
    probailities_of_temperature[temperature] = (
        probailities_of_temperature.get(temperature, (0,0))[0] + (1 if play_golf == "Yes" else 0), probailities_of_temperature.get(temperature, (0,0))[1] + (1 if play_golf != "Yes" else 0))
    probailities_of_humidity[humidity] = (
        probailities_of_humidity.get(humidity, (0,0))[0] + (1 if play_golf == "Yes" else 0), probailities_of_humidity.get(humidity, (0,0))[1] + (1 if play_golf != "Yes" else 0))
    probailities_of_windy[windy] = (
        probailities_of_windy.get(windy, (0,0))[0] + (1 if play_golf == "Yes" else 0), probailities_of_windy.get(windy, (0,0))[1] + (1 if play_golf != "Yes" else 0))
    probailities_of_play_golf[play_golf] = (
        probailities_of_play_golf.get(play_golf, (0,0))[0] + (1 if play_golf == "Yes" else 0), probailities_of_play_golf.get(play_golf, (0,0))[1] + (1 if play_golf != "Yes" else 0))
    
for key, value in probailities_of_outlook.items():
    probailities_of_outlook[key] = (value[0] / sum(value), value[1] / sum(value))
for key, value in probailities_of_temperature.items():
    probailities_of_temperature[key] = (value[0] / sum(value), value[1] / sum(value))
for key, value in probailities_of_humidity.items():
    probailities_of_humidity[key] = (value[0] / sum(value), value[1] / sum(value))
for key, value in probailities_of_windy.items():
    probailities_of_windy[key] = (value[0] / sum(value), value[1] / sum(value))
for key, value in probailities_of_play_golf.items():
    probailities_of_play_golf[key] = (sum(value) / len(data))


def predict(outlook: str, temperature: str, humidity: str, windy: str) -> str:
    yes = probailities_of_play_golf["Yes"] * probailities_of_outlook[outlook][0] * probailities_of_temperature[temperature][0] * probailities_of_humidity[humidity][0] * probailities_of_windy[windy][0]

    no = probailities_of_play_golf["No"] * probailities_of_outlook[outlook][1] * probailities_of_temperature[temperature][1] * probailities_of_humidity[humidity][1] * probailities_of_windy[windy][1]
    print(f"Yes: {yes}, No: {no}")
    if yes == no:
        return "Maybe"
    return "Yes" if yes > no else "No"

print(predict("Sunny", "Cool", "High", "True"))
print(predict("Overcast", "Mild", "Normal", "False"))
print(predict("Rain", "Mild", "Normal", "False"))

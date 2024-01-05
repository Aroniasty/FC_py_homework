import csv

with open("cost_of_living_us.csv") as file:
    data = csv.reader(file)
    for line in data:
        print(line)
import csv

def read_data_from_csv():
    data = []
    with open("cost_of_living_us.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            # rounded_line = [round(float(value), 2) for value in line]
            data.append(line)
    return data
             # print(line)

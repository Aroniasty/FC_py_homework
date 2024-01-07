import csv
from project import Data

with (open("cost_of_living_us.csv") as csv_file):
    csv_reader = csv.reader(csv_file)
    header = next(reader)
    # for line in csv_reader:
    #     print(line)
    for row in csv_reader:
        data_row = Data(
            state=row[1],
            areaname=row[3],
            total_cost=float(row[13]),
            median_family_income=float(row[14])
        )

import csv
from project import Data

with open("cost_of_living_us.csv", "r", newline="", encoding="") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    # for line in csv_reader:
    #     print(line)
    for row in csv_reader:
        data_row = Data(
            state=row[1],
            areaname=row[3],
            total_cost=float(row[13]),
            median_family_income=float(row[14])
        )
        db.session.add(data_row)

db.session.commit()

session.close()
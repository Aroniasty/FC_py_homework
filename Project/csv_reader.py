from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import csv

def read_data_from_csv():
    data = []
    # with open("cost_of_living_us.csv", "r") as csv_file:
    with open("csv_test.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            rounded_line = [round(float(value), 2) for value in line]
            data.append(rounded_line)
    return data
             # print(line)
    #     for row in csv_reader:
    #          data_row = Data(
    #             state=row[1],
    #             areaname=row[3],
    #             total_cost=float(row[13]),
    #             nie działa float
    #             median_family_income=float(row[14])


# # with open("cost_of_living_us.csv", "r") as csv_file:
# with open("csv_test.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     for line in csv_reader:
#         print(line)
#     for row in csv_reader:
#          data_row = Data(
#             state=row[1],
#             areaname=row[3],
#             total_cost=float(row[13]),
#             nie działa float
#             median_family_income=float(row[14])
#         )
#
# db.session.add(data_row)
# db.session.commit()
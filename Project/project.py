from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import csv
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def home_page():
    if request.method == "GET":
        return render_template("main.html")
    else:
        print(results)
        return redirect(url_for("results"))

@app.route("/results/", methods=["GET", "POST"])
def results():
    if request.method == "GET":
        return render_template("results.html")

@app.route("/about/", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")

class Data(db.Model):
    __tablename__ = "cost_of_living_us"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String, nullable=False)
    areaname = db.Column(db.String, nullable=False)
    total_cost = db.Column(db.Float, nullable=False, default=0)
    median_family_income = db.Column(db.Float, nullable=False, default=0)

with (open("cost_of_living_us.csv") as csv_file):
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    # for line in csv_reader:
    #     print(line)
    for row in csv_reader:
        # print(row)
        data_row = Data(
            state=row[1],
            areaname=row[3],
            total_cost=float(row[13]),
            # nie działa float
            # median_family_income=float(row[14])
        )
        # db.session.add(data_row)
# db.session.commit()


with app.app_context():
    db.create_all()
    # test = Data(state="SS", areaname="AA", total_cost="1111.11", median_family_income="2222.22")
    test = data_row
    db.session.add_all([test])
    db.session.commit()
    # kod do obsługi tabeli

if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from csv_reader import read_data_from_csv


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# @app.route("/")
# def home_page():
#     if request.method == "GET":
#         return render_template("main.html")
#     else:
#         print(results)
#         return redirect(url_for("results"))

@app.route('/')
def main():
    data = get_unique_states()
    return render_template('main.html', data=data)

@app.route('/result', methods=['POST'])
def result():
    selected_state = request.form.get('state')
    total_cost = get_total_cost_for_state(selected_state)
    return render_template('result.html', selected_state=selected_state, total_cost=total_cost)

@app.route('/about')
def about():
    return render_template("about.html")

# @app.route('/most_expensive')
# def most_expensive():
#     return render_template("most_expensive.html")

# @app.route('/total_cost')
# def total_cost():
#     return render_template("total_cost.html")


class cost_of_living_us(db.Model):
    __tablename__ = "cost_of_living_us"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50), unique=True, nullable=False)
    areaname = db.Column(db.String, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    median_family_income = db.Column(db.Float, nullable=False)

def get_unique_states():
    data = db.session.query(cost_of_living_us.state).distinct().all()
    return data

def get_total_cost_for_state(selected_state):
    total_cost = cost_of_living_us.query.filter_by(state=selected_state).first().total_cost
    return total_cost


# with (open("cost_of_living_us.csv") as csv_file):
#     csv_reader = csv.reader(csv_file)
#     header = next(csv_reader)
#     for row in csv_reader:
#         # print(row)
#         data_row = Data(
#             state=row[1],
#             areaname=row[3],
#             total_cost=float(row[13]),
            # nie działa float
            # median_family_income=float(row[14])
        # )
        # db.session.add(data_row)
# db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        data = db.session.query(cost_of_living_us).distinct().all()
        if len(data) == 0:
            data_from_csv = read_data_from_csv()
            for row in data_from_csv:
                data_row = cost_of_living_us(
                    state=row[1],
                    areaname=row[3],
                    total_cost=float(row[13]),
                    # nie działa float
                    median_family_income=float(row[14])
                )
                db.session.add(data_row)
            db.session.commit()
        # test = Data(state="SS", areaname="AA", total_cost="1111.11", median_family_income="2222.22")
        # test = data_row
        # db.session.add_all([test])
        # db.session.commit()
        # kod do obsługi tabeli
    app.run(debug=True)



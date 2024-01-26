from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from csv_reader import read_data_from_csv
import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def main():
    data = get_unique_states()
    current_year = datetime.datetime.now().year
    return render_template('main.html', data=data, current_year=current_year)


@app.route('/most_expensive', methods=['POST'])
def most_expensive():
    selected_state = request.form.get('state')
    # total_cost = get_total_cost_for_state(selected_state)
    areaname = get_areaname_for_state(selected_state)
    most_expensive = get_most_expensive(selected_state)
    average_cost = get_average_cost(selected_state)
    return render_template("most_expensive.html", selected_state=selected_state, most_expensive=most_expensive, areaname=areaname, average_cost=average_cost)

@app.route('/lowest_cost', methods=['POST'])
def lowest_cost():
    selected_state = request.form.get('state')
    areaname = get_areaname_for_state(selected_state)
    lowest_cost = get_lowest_cost(selected_state)
    return render_template("lowest_cost.html", selected_state=selected_state, lowest_cost=lowest_cost, areaname=areaname)

@app.route('/average_cost', methods=['POST'])
def average_cost():
    selected_state = request.form.get('state')
    average_cost = get_average_cost(selected_state)
    return render_template("average_cost.html", selected_state=selected_state, average_cost=average_cost)

@app.route('/all_data', methods=['POST'])
def all_data():
    selected_state = request.form.get('state')
    # total_cost = get_total_cost_for_state(selected_state)
    areaname = get_areaname_for_state(selected_state)
    most_expensive = get_most_expensive(selected_state)
    average_cost = get_average_cost(selected_state)
    lowest_cost = get_lowest_cost(selected_state)
    return render_template("all_data.html", selected_state=selected_state, most_expensive=most_expensive, areaname=areaname, average_cost=average_cost, lowest_cost=lowest_cost)


@app.route('/about')
def about():
    return render_template("about.html")

class cost_of_living_us(db.Model):
    __tablename__ = "cost_of_living_us"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50), nullable=False)
    areaname = db.Column(db.String, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    median_family_income = db.Column(db.Float, nullable=False)

def get_unique_states():
    data = db.session.query(cost_of_living_us.state).distinct().all()
    return data

def get_total_cost_for_state(selected_state):
    total_cost = cost_of_living_us.query.filter_by(state=selected_state).first().total_cost
    return total_cost

def get_areaname_for_state(selected_state):
    areaname = cost_of_living_us.query.filter_by(state=selected_state).first().areaname
    return areaname

def get_most_expensive(selected_state):
    most_expensive = cost_of_living_us.query.filter_by(state=selected_state).order_by(cost_of_living_us.total_cost.desc()).limit(3).all()
    return most_expensive

def get_lowest_cost(selected_state):
    lowest_cost = cost_of_living_us.query.filter_by(state=selected_state).order_by(cost_of_living_us.total_cost.asc()).limit(1).all()
    return lowest_cost

def get_average_cost(selected_state):
    average_cost = cost_of_living_us.query.filter_by(state=selected_state).all()
    total_cost = 0
    for city in average_cost:
        total_cost += city.total_cost
    return total_cost/len(average_cost)

# O ile procent powyzej fredniej wynosza koszty zycia
# w tych miastach w poróunaniu do Srednich kosztów zycia v danym stanie


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # get_average_cost("AL")
        data = db.session.query(cost_of_living_us).distinct().all()
        if len(data) == 0:
            data_from_csv = read_data_from_csv()
            for row in data_from_csv:
                # print(row)
                data_row = cost_of_living_us(
                    state=row[1],
                    areaname=row[3],
                    total_cost=float(row[13]),
                    median_family_income=float(row[14]) if row[14] else 0
                    # median_family_income=round(float(row[14]), 2)
                )
                db.session.add(data_row)
            db.session.commit()

    app.run(debug=True)


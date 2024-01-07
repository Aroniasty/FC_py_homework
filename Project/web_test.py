from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cost_of_living_us.db'
db = SQLAlchemy(app)

class cost_of_living_us(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50), unique=True, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    median_family_income = db.Column(db.Float, nullable=False)

def get_unique_states():
    data = db.session.query(cost_of_living_us.state).distinct().all()
    return data

def get_total_cost_for_state(selected_state):
    total_cost = cost_of_living_us.query.filter_by(state=selected_state).first().total_cost
    return total_cost

@app.route('/')
def index():
    data = get_unique_states()
    return render_template('index.html', data=data)

@app.route('/result', methods=['POST'])
def result():
    selected_state = request.form.get('state')
    total_cost = get_total_cost_for_state(selected_state)
    return render_template('result.html', selected_state=selected_state, total_cost=total_cost)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

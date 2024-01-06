from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

# engine = create_engine('sqlite:///project.db')
# db.create_all()

Session = sessionmaker(bind=engine)
session = Session()


with app.app_context():
    db.create_all()
    test = Data(state="SS", areaname="AA", total_cost="1111.11", median_family_income="2222.22")
    db.session.add_all([test])
    db.session.commit()
    # kod do obsługi tabeli

if __name__ == "__main__":
    app.run(debug=True)



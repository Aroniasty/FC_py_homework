from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
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
   id=db.Column(db.Integer, primary_key=True)

    # """
    # id
    # state
    # areaname
    # total_cost
    # median_family_income
    # """
# with app.app_context():
    # db.create_all() /// odkomentowac jak bedzie gotowa klasa
    # kod do obsługi tabeli

if __name__ == "__main__":
    app.run(debug=True)



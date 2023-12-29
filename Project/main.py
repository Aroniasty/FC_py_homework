from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
db=SQLAlchemy(app)


class Data(db.Model):
   id=db.Column(db.Integer, primary_key=True)

    """
    id
    state
    areaname
    total_cost
    median_family_income
    """
with app.app_context():
    # db.create_all() /// odkomentowac jak bedzie gotowa klasa
    # kod do obsługi tabeli

if __name__ == "__main__":
    app.run(debug=True)



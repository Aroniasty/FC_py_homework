from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

app = Flask(__name__)

# Konfiguracja bazy danych SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moja_baza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Definicja modelu dla tabeli
class Data(db.Model):
    __tablename__ = 'nazwa_tabeli'

    id = Column(Integer, primary_key=True)
    state = Column(String, nullable=False)
    areaname = Column(String, nullable=False)
    total_cost = Column(Float, nullable=False, default=0)
    median_family_income = Column(Float, nullable=False, default=0)


# Utworzenie silnika bazy danych
engine = create_engine('sqlite:///moja_baza.db')
db.create_all()

# Utworzenie sesji do komunikacji z bazą danych
Session = sessionmaker(bind=engine)
session = Session()


# Trasa do importu danych z pliku CSV
@app.route('/import_data', methods=['GET', 'POST'])
def import_data():
    if request.method == 'POST':
        # Ścieżka do pliku CSV
        csv_file_path = 'nazwa_pliku.csv'

        # Otwarcie pliku CSV i zaimportowanie danych do bazy danych
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Pominięcie nagłówka
            next(csv_reader)

            for row in csv_reader:
                # Utworzenie obiektu modelu i dodanie do sesji
                data_row = Data(
                    state=row[1],
                    areaname=row[2],
                    total_cost=float(row[3]),
                    median_family_income=float(row[4])
                )
                db.session.add(data_row)

        # Zapisanie zmian w bazie danych
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('import_data.html')


# Trasa do strony głównej
@app.route('/')
def index():
    data = Data.query.all()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)

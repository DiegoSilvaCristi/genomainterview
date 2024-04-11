from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:fono62333985@localhost/genomadb'
db = SQLAlchemy(app)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False)
    city = db.Column(db.String(200), nullable = False)
    country = db.Column(db.String(200), nullable = False)
    type = db.Column(db.String(200), nullable = False)
    rating = db.Column(db.Float)
    visited = db.Column(db.Boolean, nullable = False)
    created_ar = db.Column(db.DateTime, nullable = False, default = datetime.now)

    def __repr__(self):
        return f"Restaurant {self.name}"
    
    def __init__(self, name, city, country, type, rating, visited):
        self.name = name
        self.city = city
        self.country = country
        self.type = type
        self.rating = rating
        self.visited = visited

@app.route('/')
def hello():
    return 'HEY!'

if __name__ == '__main__':
    app.run()

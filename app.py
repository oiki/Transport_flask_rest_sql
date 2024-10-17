
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital_transport.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Transport

@app.route('/')
def home():
    return "Welcome to the Hospital Transport Regulation System"

if __name__ == '__main__':
    app.run(debug=True)

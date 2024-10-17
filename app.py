
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital_transport.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Transport

from flask import request, jsonify
from datetime import datetime

@app.route('/')
def home():
    return "Welcome to the Hospital Transport Regulation System"

@app.route('/transports', methods=['POST'])
def add_transport():
    data = request.get_json()
    new_transport = Transport(
        patient_name=data['patient_name'],
        transport_type=data['transport_type'],
        transport_time=datetime.strptime(data['transport_time'], '%Y-%m-%d %H:%M:%S'),
        status=data['status']
    )
    db.session.add(new_transport)
    db.session.commit()
    return jsonify({'message': 'Transport added successfully'}), 201

@app.route('/transports', methods=['GET'])
def get_transports():
    transports = Transport.query.all()
    output = []
    for transport in transports:
        transport_data = {
            'id': transport.id,
            'patient_name': transport.patient_name,
            'transport_type': transport.transport_type,
            'transport_time': transport.transport_time.strftime('%Y-%m-%d %H:%M:%S'),
            'status': transport.status
        }
        output.append(transport_data)
    return jsonify({'transports': output})

@app.route('/transports/<id>', methods=['PUT'])
def update_transport(id):
    data = request.get_json()
    transport = Transport.query.get(id)
    if not transport:
        return jsonify({'message': 'Transport not found'}), 404

    transport.patient_name = data['patient_name']
    transport.transport_type = data['transport_type']
    transport.transport_time = datetime.strptime(data['transport_time'], '%Y-%m-%d %H:%M:%S')
    transport.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Transport updated successfully'})

@app.route('/transports/<id>', methods=['DELETE'])
def delete_transport(id):
    transport = Transport.query.get(id)
    if not transport:
        return jsonify({'message': 'Transport not found'}), 404

    db.session.delete(transport)
    db.session.commit()
    return jsonify({'message': 'Transport deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

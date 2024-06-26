from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import Schema, fields
from sqlalchemy import text
from ..conn import Session
from ..logger import logger
from ..utils import limiter

update_patient_bp = Blueprint('update_patient', __name__)

class UpdatePatientSchema(Schema):
    patient_id = fields.Int(required=True)
    name = fields.Str(required=True)
    telephone = fields.Int(required=True)
    email = fields.Str(required=True)
    sex = fields.Str(required=True)
    birthdate = fields.Str(required=True)
    processnumber = fields.Str(required=True)
    address = fields.Str(required=True)
    postalcode = fields.Str(required=True)
    town = fields.Str(required=True)
    nif = fields.Int(required=True)
    sns = fields.Int(required=True)
    
@update_patient_bp.route('/update_patient', methods=['PATCH'])
@jwt_required()
@limiter.limit("5 per minute")
def update_patient():
    
    doctor_id = get_jwt_identity()

    data = request.get_json()
    schema = UpdatePatientSchema()
    errors = schema.validate(data)

    if errors:
        logger.error(f"Invalid patient update request made by Doctor ID:{doctor_id}.", extra={"method": "PATCH", "statuscode": 400})
        return jsonify({'errors': errors}), 400
    
    session = Session()
    
    patient_id = data['patient_id']
    
    try:
        session.execute(
            text('UPDATE patients SET name = :name, telephone = :telephone, email = :email, \
                sex = :sex, birthdate = :birthdate, processnumber = :processnumber, address = :address, \
                postalcode = :postalcode, town = :town, nif = :nif, sns = :sns WHERE patient_id = :patient_id'),
            {
                'name': data['name'], 
                'telephone': data['telephone'], 
                'email': data['email'],
                'sex': data['sex'], 
                'birthdate': data['birthdate'], 
                'processnumber': data['processnumber'], 
                'address': data['address'],
                'postalcode': data['postalcode'], 
                'town': data['town'], 
                'nif': data['nif'], 
                'sns': data['sns'], 
                'patient_id': patient_id,
            }
        )
        session.commit()
        
        logger.info(f"Doctor ID:{doctor_id} updated data of Patient ID:{patient_id}.", extra={"method": "PATCH", "statuscode": 200})
        return jsonify({'success': True}), 200
    except Exception as e:
        session.rollback()
        logger.error(f"Doctor ID:{doctor_id}'s attempt to update Patient ID:{patient_id} failed.", extra={"method": "PATCH", "statuscode": 500, "exc": str(e)})
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

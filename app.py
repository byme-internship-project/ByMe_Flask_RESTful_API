from flask import Flask

from endpoints.auth.register import register_bp
from endpoints.auth.login import login_bp

from endpoints.doctor.select_doctor import select_doctor_bp
from endpoints.doctor.select_doctor_id import select_doctor_id_bp
from endpoints.doctor.delete_doctor import delete_doctor_bp
from endpoints.doctor.update_doctor import update_doctor_bp

from endpoints.module.delete_module import delete_module_bp
from endpoints.module.select_module import select_module_bp
from endpoints.module.select_module_id import select_module_id_bp
from endpoints.module.insert_module import insert_module_bp
from endpoints.module.update_module import update_module_bp

from endpoints.patient.insert_patient import insert_patient_bp
from endpoints.patient.update_patient import update_patient_bp
from endpoints.patient.delete_patient import delete_patient_bp
from endpoints.patient.select_patient import select_patient_bp
from endpoints.patient.update_patient_doctor import update_patient_doctor_bp

app = Flask(__name__)

app.register_blueprint(register_bp, url_prefix='/auth')
app.register_blueprint(login_bp, url_prefix='/auth')

app.register_blueprint(select_doctor_bp, url_prefix='/doctor')
app.register_blueprint(select_doctor_id_bp, url_prefix='/doctor')
app.register_blueprint(delete_doctor_bp, url_prefix='/doctor')
app.register_blueprint(update_doctor_bp, url_prefix='/doctor')

app.register_blueprint(delete_module_bp, url_prefix='/module')
app.register_blueprint(select_module_bp, url_prefix='/module')
app.register_blueprint(select_module_id_bp, url_prefix='/module')
app.register_blueprint(insert_module_bp, url_prefix='/module')
app.register_blueprint(update_module_bp, url_prefix='/module')

app.register_blueprint(insert_patient_bp, url_prefix='/patient')
app.register_blueprint(select_patient_bp, url_prefix='/patient')
app.register_blueprint(update_patient_bp, url_prefix='/patient')
app.register_blueprint(delete_patient_bp, url_prefix='/patient')
app.register_blueprint(update_patient_doctor_bp, url_prefix='/patient')

@app.route('/', methods=['GET'])
def index():
    return 'Olá'

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=False)

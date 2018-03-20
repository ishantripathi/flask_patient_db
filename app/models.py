#: This is where the models are defined. A model is a representation of a database table in code.
#  However, because we will not be using a database in this tutorial, we won't be needing this file.

# app/models.py
#$ flask db init : create migration repository
#pycharm: alt+F12
#set FLASK_APP=run.py
# flask db init : This creates a migrations directory in the  directory:
# flask db init : This creates a migrations directory in the  directory:
#  flask db migrate: create the first migration:
# flask db upgrade: apply migration

#$ flask shell
#>>> from app.models import Employee
#>>> from app import db
#>>> admin = Employee(email="admin@admin.com",username="admin",password="admin2016",is_admin=True)
#>>> db.session.add(admin)
#>>> db.session.commit()

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

class Patient_info(db.Model):
    """
    Create a patient_info table
    """

    __tablename__ = 'patient_info'


    name = db.Column(db.String(60))
    mdtc = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(7))
    phone_no = db.Column(db.Integer)
    diagnosis = db.Column(db.String(60))
    symptoms = db.Column(db.String(400))
    histopathology = db.Column(db.String(400))
    ihc = db.Column(db.String(400))
    genetic_mutation = db.Column(db.String(400))
    ct_scan = db.Column(db.String(400))
    wpet = db.Column(db.String(400))
    ugie = db.Column(db.String(400))
    colonoscopy = db.Column(db.String(400))
    mri = db.Column(db.String(400))
    other_investigation = db.Column(db.String(400))
    remarks = db.Column(db.String(400))
    patient_chemo = db.relationship('Patient_chemo', backref='patient_info',
                                lazy='dynamic')

    def __repr__(self):
        return '<patient_info: {}>'.format(self.mdtc)

class Patient_chemo(db.Model):
    """
    Create a Chemo table
    """

    __tablename__ = 'patient_chemo'

    chemo_id = db.Column(db.Integer, primary_key=True)
    mdtc = db.Column(db.Integer, db.ForeignKey('patient_info.mdtc'))
    cycle = db.Column(db.Integer)
    chemotherapy = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    response = db.Column(db.String(1000))
    side_effect = db.Column(db.String(1000))




    def __repr__(self):
        return '<Patient_chemo: {}>'.format(self.mdtc)
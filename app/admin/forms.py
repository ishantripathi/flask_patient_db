# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField, IntegerField, TextAreaField, FieldList
from wtforms.validators import DataRequired


class PatientForm(FlaskForm):
    """
    Form for admin to add or edit a patient
    """

    name = StringField('Name', validators=[DataRequired()])
    mdtc = IntegerField('MTDC', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    sex = RadioField('Sex', choices=[('M', 'Male'), ('F', 'Female')])
    phone_no = IntegerField('Phone No', validators=[DataRequired()])
    diagnosis = SelectField('Diagnosis', choices=[('lung(adenoca)', 'Lung(adenoca)'),
                                                  ('lung(sclc)', 'Lung(sclc)'),
                                                  ('lung(sqsclc)', 'Lung(sqsclc)'),
                                                  ('net', 'NET'),
                                                  ('nec', 'NEC'),
                                                  ('ovary', 'Ovary'),
                                                  ('hcc', 'HCC'),
                                                  ('gallbladder', 'Gall Bladder'),
                                                  ('pancreas', 'Pancreas'),
                                                  ('colon', 'Colon'),
                                                  ('cervix', 'Cervix'),
                                                  ('gbm', 'GBM'),
                                                  ('braintumor', 'Brain Tumor'),
                                                  ('oralcavity', 'Oral Cavity'),
                                                  ('larynx', 'Larynx'),
                                                  ('pharynx', 'Pharynx'),
                                                  ('esophagin', 'Esophagin'),
                                                  ('stomach', 'Stomach'),
                                                  ('analcanal', 'Analcanal'),
                                                  ('rectum', 'Rectum'),
                                                  ('sarcoma', 'Sarcoma'),
                                                  ('gist', 'GIST'),
                                                  ('skin', 'Skin'),
                                                  ('rcc', 'RCC'),
                                                  ('others', 'Other Diagnosis')])
    other_diagnosis = StringField('Other Diagnosis')
    symptoms = StringField('Symptoms', validators=[DataRequired()])
    histopathology = StringField('Histopathology')
    ihc = StringField('IHC')
    genetic_mutation = StringField('Genetic Mutaion')
    ct_scan = StringField('CT Scan')
    wpet = StringField('WPET')
    ugie = StringField('UGIE')
    colonoscopy = StringField('Colonoscopy')
    mri = StringField('MRI')
    other_investigation = StringField('Other Investigation')
    remarks = TextAreaField('Remark')
    submit = SubmitField('Submit')
    cycle = FieldList(IntegerField('Cycle', validators=[DataRequired()]), min_entries=0, max_entries=9)
    chemotherapy = FieldList(StringField('Chemotherapy', validators=[DataRequired()]), min_entries=0, max_entries=9)
    description = FieldList(StringField('Description', validators=[DataRequired()]), min_entries=0, max_entries=9)
    response = FieldList(StringField('Response', validators=[DataRequired()]), min_entries=0, max_entries=9)
    side_effect = FieldList(StringField('Side Effect'), min_entries=0, max_entries=9)

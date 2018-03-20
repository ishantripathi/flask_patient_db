# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import PatientForm
from .. import db
from ..models import Patient_info
from ..models import Patient_chemo

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

# Patient Views

@admin.route('/patients', methods=['GET', 'POST'])
@login_required
def list_patients():
    """
    List all patients
    """
    check_admin()

    patients = Patient_info.query.all()

    return render_template('admin/patients/patients.html',
                           patients = patients, title="Patients")

@admin.route('/patients/add', methods=['GET', 'POST'])
@login_required
def add_patient():
    """
    Add a patient to the database
    """
    check_admin()
    add_patient = True

    form = PatientForm()

    if form.validate_on_submit():

        if form.diagnosis.data == 'others':
            diag = form.other_diagnosis.data
        else:
            diag = form.diagnosis.data



        patient = Patient_info(name=form.name.data,
                                mdtc=form.mdtc.data,
                                age=form.age.data,
                                sex=form.sex.data,
                                phone_no=form.phone_no.data,
                                diagnosis=diag,
                                symptoms=form.symptoms.data,
                                histopathology=form.histopathology.data,
                                ihc=form.ihc.data,
                                genetic_mutation=form.genetic_mutation.data,
                                ct_scan=form.ct_scan.data,
                                wpet=form.wpet.data,
                                ugie=form.ugie.data,
                                colonoscopy=form.colonoscopy.data,
                                mri=form.mri.data,
                                other_investigation=form.other_investigation.data,
                                remarks=form.remarks.data)


        no_chemo=len(form.cycle.data)
        patient_chemo = []
        for i in range(0, no_chemo):
            patient_chemo.append( Patient_chemo(
                                mdtc= form.mdtc.data,
                                cycle=form.cycle.data[i],
                                chemotherapy=form.chemotherapy.data[i],
                                description=form.description.data[i],
                                response=form.response.data[i],
                                side_effect=form.side_effect.data[i])
            )

        try:
        # add patient to the
            db.session.add(patient)

            for i in range(0, no_chemo):
                db.session.add(patient_chemo[i])
            db.session.commit()

            flash('You have successfully added a new patient.')

        except:
            # in case of error
            flash('Error: Error in inserting the patient.')

            # redirect to patients page
        return redirect(url_for('admin.list_patients'))
    # load patient template
    return render_template('admin/patients/patient.html', action="Add",
                           add_patient=add_patient, form=form,
                           title="Add Patient")

@admin.route('/patients/edit/<int:mdtc>', methods=['GET', 'POST'])
@login_required
def edit_patient(mdtc):
    """
    Edit a patient
    """
    check_admin()

    add_patient = False

    patient = Patient_info.query.get_or_404(mdtc)
    print  patient
    print("data")
    print patient.name
    print("data close")
    form = PatientForm(obj=patient)
    for chemo in patient.patient_chemo.all():
        form.cycle.append_entry(chemo.cycle)
        form.chemotherapy.append_entry(chemo.chemotherapy)
        form.description.append_entry(chemo.description)
        form.response.append_entry(chemo.response)
        form.side_effect.append_entry(chemo.side_effect)


    if form.validate_on_submit():

        if form.diagnosis.data == 'others':
            diag = form.other_diagnosis.data
        else:
            diag = form.diagnosis.data

        patient.name = form.name.data
        patient.mdtc = form.mdtc.data
        patient.age = form.age.data
        patient.sex = form.sex.data
        patient.phone_no = form.phone_no.data
        patient.diagnosis = diag
        patient.symptoms = form.symptoms.data
        patient.histopathology = form.histopathology.data
        patient.ihc = form.ihc.data
        patient.genetic_mutation = form.genetic_mutation.data
        patient.ct_scan = form.ct_scan.data
        patient.wpet = form.wpet.data
        patient.ugie = form.ugie.data
        patient.colonoscopy = form.colonoscopy.data
        patient.mri = form.mri.data
        patient.other_investigation = form.other_investigation.data
        patient.remarks = form.remarks.data
        db.session.commit()

        patient_chemo = Patient_chemo()
        no_chemo = len(form.cycle.data)
        for i in range(0, no_chemo):
            patient_chemo.mdtc = form.mdtc.data
            patient_chemo.cycle = form.cycle.data[i]
            patient_chemo.chemotherapy = form.chemotherapy.data[i]
            patient_chemo.description = form.description.data[i]
            patient_chemo.response = form.response.data[i]
            patient_chemo.side_effect = form.side_effect.data[i]
            db.session.commit()



        flash('You have successfully edited the Patient.')

        # redirect to the patients page
        return redirect(url_for('admin.list_patients'))


    form.mdtc.data = patient.mdtc
    form.name.data = patient.name
    return render_template('admin/patients/patient.html', action="Edit",
                           add_patient=add_patient, form=form,
                           patient=patient, title="Edit Patient")

@admin.route('/patients/delete/<int:mdtc>', methods=['GET', 'POST'])
@login_required
def delete_patient(mdtc):
    """
    Delete a Patient from the database
    """
    check_admin()

    patient = Patient_info.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    flash('You have successfully deleted the Patient.')

    # redirect to the patients page
    return redirect(url_for('admin.list_patients'))

    return render_template(title="Delete Patient")
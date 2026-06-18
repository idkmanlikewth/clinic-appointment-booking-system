from sqlalchemy.orm import Session
from models import Patient, Appointment


def create_patient(
    db: Session,
    patient
):
    db_patient = Patient(
        **patient.dict()
    )

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient


def create_appointment(
    db: Session,
    appointment
):
    db_appointment = Appointment(
        **appointment.dict()
    )

    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)

    return db_appointment
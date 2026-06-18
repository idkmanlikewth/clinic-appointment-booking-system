from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from database import (
    SessionLocal,
    Base,
    engine
)

from models import (
    User,
    Doctor,
    Appointment
)

from schemas import (
    UserSignup,
    DoctorSignup,
    AppointmentCreate
)

from auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_refresh_token
)

from auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_refresh_token,
    get_current_user
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Clinic Appointment Booking System"
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message":
        "Clinic Appointment Booking API"
    }


# ======================
# USER SIGNUP
# ======================

@app.post("/user/signup")
def user_signup(
    user: UserSignup,
    db: Session = Depends(get_db)
):

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(
            user.password
        )
    )

    db.add(new_user)
    db.commit()

    return {
        "message":
        "User registered successfully"
    }


# ======================
# USER LOGIN
# ======================

@app.post("/user/login")
def user_login(
    form_data:
    OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email ==
        form_data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="User not found"
        )

    if not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=400,
            detail="Wrong password"
        )

    return {
        "access_token":
        create_access_token(user.email),

        "refresh_token":
        create_refresh_token(user.email),

        "token_type":
        "bearer"
    }


# ======================
# DOCTOR SIGNUP
# ======================

@app.post("/doctor/signup")
def doctor_signup(
    doctor: DoctorSignup,
    db: Session = Depends(get_db)
):

    existing = db.query(
        Doctor
    ).filter(
        Doctor.email == doctor.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Doctor exists"
        )

    new_doctor = Doctor(
        username=doctor.username,
        email=doctor.email,
        specialization=
        doctor.specialization,

        password=get_password_hash(
            doctor.password
        )
    )

    db.add(new_doctor)
    db.commit()

    return {
        "message":
        "Doctor registered successfully"
    }


# ======================
# DOCTOR LOGIN
# ======================

@app.post("/doctor/login")
def doctor_login(
    form_data:
    OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    doctor = db.query(
        Doctor
    ).filter(
        Doctor.email ==
        form_data.username
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=400,
            detail="Doctor not found"
        )

    if not verify_password(
        form_data.password,
        doctor.password
    ):
        raise HTTPException(
            status_code=400,
            detail="Wrong password"
        )

    return {
        "access_token":
        create_access_token(
            doctor.email
        ),

        "refresh_token":
        create_refresh_token(
            doctor.email
        ),

        "token_type":
        "bearer"
    }


# ======================
# BOOK APPOINTMENT
# ======================


@app.post("/appointments/book")
def book_appointment(
    appointment: AppointmentCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    print("Current User:", current_user)

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    doctor = db.query(Doctor).filter(
        Doctor.id == appointment.doctor_id
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    new_appointment = Appointment(
        user_id=user.id,
        doctor_id=doctor.id,
        appointment_date=appointment.appointment_date,
        appointment_time=appointment.appointment_time
    )

    db.add(new_appointment)
    db.commit()

    return {
        "message": "Appointment booked successfully"
    }


# ======================
# VIEW APPOINTMENTS
# ======================

@app.get("/appointments/my")
def my_appointments(
    current_user:
    str = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email ==
        current_user
    ).first()

    return db.query(
        Appointment
    ).filter(
        Appointment.user_id ==
        user.id
    ).all()


# ======================
# CANCEL APPOINTMENT
# ======================

@app.delete(
    "/appointments/{appointment_id}"
)
def cancel_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):

    appointment = db.query(
        Appointment
    ).filter(
        Appointment.id ==
        appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail=
            "Appointment not found"
        )

    db.delete(appointment)
    db.commit()

    return {
        "message":
        "Appointment cancelled"
    }
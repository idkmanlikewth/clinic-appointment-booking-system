from pydantic import BaseModel
from pydantic import EmailStr


class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str


class DoctorSignup(BaseModel):
    username: str
    email: EmailStr
    specialization: str
    password: str


class AppointmentCreate(BaseModel):
    doctor_id: int
    appointment_date: str
    appointment_time: str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
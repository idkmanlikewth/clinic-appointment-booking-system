# Clinic Appointment Booking System

A secure and scalable Clinic Appointment Booking System built with **FastAPI**, **SQLAlchemy**, **SQLite**, and **JWT Authentication**.

The system enables patients and doctors to register, authenticate securely, and manage appointments through RESTful APIs. JWT-based authentication ensures protected access to appointment-related operations.

---

## Overview

This project demonstrates the implementation of a modern backend application using FastAPI. It follows REST API principles and incorporates authentication, database management, and CRUD operations.

### Key Capabilities

* Secure User Registration and Authentication
* Doctor Registration and Authentication
* JWT-Based Authorization
* Appointment Booking Management
* Appointment Cancellation
* Database Persistence using SQLite
* Interactive API Documentation

---

## System Architecture

```text
Client (Postman / Swagger UI)
            │
            ▼
        FastAPI
            │
            ▼
     Authentication
      (JWT Tokens)
            │
            ▼
       SQLAlchemy
            │
            ▼
         SQLite
```

---

## Features

### Patient Management

* Register a new patient account
* Secure login using JWT authentication
* View personal appointments

### Doctor Management

* Register doctor profiles
* Secure doctor authentication
* Manage specialization details

### Appointment Management

* Schedule appointments with doctors
* View booked appointments
* Cancel existing appointments

### Security

* Password hashing using BCrypt
* JWT Access Tokens
* Protected API endpoints
* Token-based authorization

---

## Technology Stack

| Component         | Technology       |
| ----------------- | ---------------- |
| Backend Framework | FastAPI          |
| Database          | SQLite           |
| ORM               | SQLAlchemy       |
| Authentication    | JWT              |
| Password Hashing  | Passlib (BCrypt) |
| API Testing       | Postman          |
| Documentation     | Swagger UI       |

---

## Project Structure

```text
clinic_management/
│
├── auth.py
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas.py
├── clinic.db
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<username>/clinic-appointment-booking-system.git

cd clinic-appointment-booking-system
```

### Create Virtual Environment

```bash
python -m venv clinic_management
```

### Activate Virtual Environment

**Windows**

```bash
clinic_management\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## Authentication Workflow

1. Register a User or Doctor account
2. Log in using valid credentials
3. Receive a JWT Access Token
4. Include the token in the Authorization header

Example:

```text
Authorization: Bearer <access_token>
```

Protected endpoints require a valid JWT token.

---

## API Endpoints

### User APIs

| Method | Endpoint       | Description         |
| ------ | -------------- | ------------------- |
| POST   | `/user/signup` | Register a new user |
| POST   | `/user/login`  | Authenticate user   |

### Doctor APIs

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| POST   | `/doctor/signup` | Register a doctor   |
| POST   | `/doctor/login`  | Authenticate doctor |

### Appointment APIs

| Method | Endpoint             | Description           |
| ------ | -------------------- | --------------------- |
| POST   | `/appointments/book` | Book an appointment   |
| GET    | `/appointments/my`   | Retrieve appointments |
| DELETE | `/appointments/{id}` | Cancel appointment    |

---

## Sample Workflow

```text
User Registration
        │
        ▼
User Login
        │
        ▼
Receive JWT Token
        │
        ▼
Doctor Registration
        │
        ▼
Book Appointment
        │
        ▼
View Appointments
        │
        ▼
Cancel Appointment
```

---

## Testing

The APIs can be tested using:

* Postman
* Swagger UI
* FastAPI Interactive Documentation

---

## Learning Objectives

This project demonstrates:

* RESTful API Design
* JWT Authentication and Authorization
* Database Integration with SQLAlchemy
* CRUD Operations
* Secure Password Management
* FastAPI Development
* API Documentation and Testing


## License

This project is intended for educational and academic purposes.

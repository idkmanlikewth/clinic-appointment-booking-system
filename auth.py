
from jose import jwt
import bcrypt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

# Hardcoded keys for college project
SECRET_KEY = "mysecretkey123"
REFRESH_SECRET_KEY = "myrefreshsecret123"

ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/user/login"
)


def get_password_hash(password):

    # bcrypt only supports secrets up to 72 bytes; truncate safely
    # instead of letting the bcrypt library raise a ValueError.
    password_bytes = password.encode("utf-8")[:72]

    hashed = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )

    return hashed.decode("utf-8")


def verify_password(
    plain_password,
    hashed_password
):
    try:
        plain_bytes = plain_password.encode("utf-8")[:72]
        hashed_bytes = hashed_password.encode("utf-8")

        return bcrypt.checkpw(
            plain_bytes,
            hashed_bytes
        )

    except ValueError:
        return False


def create_access_token(subject):

    expire = datetime.utcnow() + timedelta(
        minutes=30
    )

    return jwt.encode(
        {
            "sub": subject,
            "exp": expire
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def create_refresh_token(subject):

    expire = datetime.utcnow() + timedelta(
        days=7
    )

    return jwt.encode(
        {
            "sub": subject,
            "exp": expire
        },
        REFRESH_SECRET_KEY,
        algorithm=ALGORITHM
    )


def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return email

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

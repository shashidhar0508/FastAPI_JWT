from fastapi import FastAPI, Security, Request
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import datetime
import jwt

app = FastAPI()


class User(BaseModel):
    name: str
    password: str


JWT_SECRET_KEY = 'EvO>|3_LND_SeC123t'
JWT_ALGORITHM = 'HS512'

token_check = OAuth2PasswordBearer(tokenUrl="/")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    token1 = request.headers['authorization']
    token2 = token1.replace("Bearer ", "")
    validation_process(token2)
    response = await call_next(request)
    return response


def validation_process(token):
    if token != '' and token is not None:
        try:
            jwt_options = {
                'verify_signature': False,
                'verify_exp': True,
                'verify_nbf': False,
                'verify_iat': True,
                'verify_aud': False
            }
            user_details = jwt.decode(token.encode(), JWT_SECRET_KEY.encode(), algorithms=['HS512'], options=jwt_options)
            print("user_details : ",user_details)
            if user_details['sub'] == 'shashi123':
                return {"message": "valid user"}
            else:
                return {"message": "Invalid user"}
        except (jwt.DecodeError, jwt.ExpiredSignatureError) as msg:
            return {"message": "Token is invalid or Timeout"}
    else:
        return {"message": "Token required"}


@app.get("/protected_method")
def protected_method(token: str = Security(token_check)):
    """
            Valid token users can access this function,
            Used decorator to check if token is valid or not
    """
    print("protected_method")
    return {"message": "Valid users can only access this function"}


@app.get("/unprotected_method")
def unprotected_method():
    """
        Without any Token validation we can access this function
    """
    return {"message": "Anyone access this function"}


@app.post("/login")
def login(user: User):
    """
    For Creating Token after User Login
    """
    try:
        time = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
        payload = {"user_id": user.name, "password": user.password, "exp": time}
        token = jwt.encode(payload, JWT_SECRET_KEY, JWT_ALGORITHM).decode('utf-8')
        return {"token": token}
    except Exception:
        return {"message": "Error in creating Token"}

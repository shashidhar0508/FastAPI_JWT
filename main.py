from fastapi import FastAPI, Security
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import datetime
import jwt

app = FastAPI()


class User(BaseModel):
    name: str
    password: str


JWT_SECRET_KEY = 'shashi'
JWT_ALGORITHM = 'HS256'

token_check = OAuth2PasswordBearer(tokenUrl="/")


def token_validation(func):
    def validation_process(token):
        print("token in validation process : ", token)
        try:
            user_details = jwt.decode(token, JWT_SECRET_KEY, JWT_ALGORITHM)
            print("user details : ", user_details)
            if user_details.user_id == 'shashi' and user_details.password == 'shashi123':
                return {"message": "valid user"}
            else:
                return {"message": "Invalid user"}
        except Exception:
            return {"message": "Token is invalid or Timeout"}

    return validation_process


@app.get("/protected_method")
@token_validation
def protected_method(token: str = Security(token_check)):
    """
            Valid token users can access this function,
            Used decorator to check if token is valid or not
    """
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

# @app.get("/check")
# def user_ops(token: str = Security(token_check)):
#     print("Input token : ", token)
#     user_names = user_encode.decode_token(token)
#     print("user name after decode : ", user_names)
#     print("type of user_names : ", type(user_names))
#     name = user_names["name"]
#     print("name after decode : ", name)
#     if name == 'shashi':
#         return {"status": "success"}
#     else:
#         return {"Token Error": "Incorrect user name"}


# @app.get("/login/{username}/{password}")
# def login(username: str, password: str, token: str = Security(token_check)):
#     username = user_encode.decode_token(token)
#     print("user name after decode : ", username)
#     try:
#         if username == 'shashi' and password == 'shashi123':
#             times = datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
#             payload = {"user_id": username, "exp": times}
#             token = jwt.encode(payload, JWT_SECRET_KEY, JWT_ALGORITHM)
#             return {"token": token}
#     except ValueError:
#         return {"info": "wrong credentials"}

# FastAPI_JWT
# Python JWT Authorization

- Install all the dependecies using following command
```sh
pip3 install -r requirements.txt
```
- Run FastAPI application using following command
```sh
uvicorn main:app --reload
```
- From POSTMAN send the Token by selecting 'Bearer Token' in 'Authorization' and add the token in token field.
- As we used middleware in our project for every method the middleware will be executed first.

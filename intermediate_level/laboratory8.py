# Modulo. APIs web con FastAPI(Automatización)

from datetime import datetime, timedelta
from typing import List, Optional

import jwt
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

# Constants for JWT
SECRET_KEY = "mysecretkey"
ALGORITHM = "hs256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models for validation


class OrderItem(BaseModel):
    product_name: str
    quantity: int
    price: float


class Order(BaseModel):
    id: int
    user: str
    items: List[OrderItem]
    created_at: datetime


class OrderCreate(BaseModel):
    user: str
    items: List[OrderItem]


class Token(BaseModel):
    access_token: str
    token_type: str


# Base de datos
orders_db = {}
order_id_counter = 1

# Users dummy
users_db = {
    "Cecilia": {"username": "Cecilia", "password": "1234"},
}


# Funciones de autentificación
def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if not user or user["password"] != password:
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Ivalid authentication")
        return username
    except jwt.PyJWKTError:
        raise HTTPException(status_code=401, detail="Invalid authentication")


# Instancia api
app = FastAPI(title="Laboratory 8: Orders API")

# Rutas


@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_access_token(
        {"sub": user["username"]}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": token, "token_type": "bearer"}


# Nueva orden
@app.post("/orders", response_model=Order)
def create_order(order: OrderCreate, username: str = Depends(get_current_user)):
    global order_id_counter
    new_order = Order(
        id=order_id_counter,
        user=username,
        items=order.items,
        created_at=datetime.utcnow(),
    )
    orders_db[order_id_counter] = new_order
    order_id_counter += 1
    return new_order


# Listar las ordenes de usuarios
@app.get("/orders", response_model=List[Order])
def list_orders(username: str = Depends(get_current_user)):
    return [order for order in orders_db.values() if order.user == username]


# Obtener orden por id


@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int, username: str = Depends(get_current_user)):
    order = orders_db.get(order_id)
    if not order or order.user != username:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


if __name__ == "__main__":
    print("Laboratory 8: FastApi Orders ready")
    print("Run with uvicorn intermediate_level.laboratory8:app --reload")

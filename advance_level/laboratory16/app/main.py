# Modulo Empaquetado, distribucion y CI/CD

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Laboratory16: FastAPI running"}

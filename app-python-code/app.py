from pathlib import Path
import uvicorn
import os
from fastapi import FastAPI
from typing import Optional
from enum import Enum

class ModelOperacion(str, Enum):
    suma = "suma"
    resta = "resta"
    multiplicacion = "multiplicacion"
    division = "division"

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Bienvenidos a la prueba DevOps para la empresa EVERTEC"}

#devops-evertec
#llamada que va path items y que tome el item_id que estamos pasando como Path parameter /{value2}
@app.get("/devops-evertec/operation/{operacion}/{value1}/{value2}")
async def get_operation_basic(
                            operacion: ModelOperacion, 
                            value1: int = Path(min=1, description="Primer valor de la operacion"),
                            value2: int = Path(min=1, description="Segundo valor de la operacion")
                            ):

    if operacion=="division":
        resultado = value1/value2
    elif operacion=="multiplicacion":
        resultado = value1*value2
    elif operacion=="resta":
        resultado = value1-value2
    elif operacion=="suma":
        resultado = value1+value2

    return  {
                "operacion": operacion,
                "valor 1": value1,
                "valor 2": value2,
                "resultado de la operacion": resultado
            }


#if __name__ == "__main__":
    #uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

# Introduction 
El objetivo de este API es realizar las operaciones principales como lo es:
 - Suma
 - Resta
 - Multiplicacion
 - Division

# Getting Started
La aplicacion accede mediante el EndPoint:
http://127.0.0.1:8000/devops-evertec/operation/

Los parametros de esté EndPoint son 3 teniendo en cuenta el orden:

1.	Parametro de tipo de operacion se recibe como: suma / resta / multiplicacion / division
2.	Parametro valor 1; corresponde al primer valor para realizar la operacion
3.	Parametro valor 2; corresponde al segundo valor para realizar la operacion

# Build and Test
Dentro de las pruebas realizada para cada una de los opciones podemos tener:
- http://127.0.0.1:8000/devops-evertec/operation/suma/5/5
    Resultado:
    {
        "operacion": "suma",
        "valor 1": 5,
        "valor 2": 5,
        "resultado de la operacion": 10
    }

- http://127.0.0.1:8000/devops-evertec/operation/resta/15/8
    Resultado:
    {
        "operacion": "resta",
        "valor 1": 15,
        "valor 2": 8,
        "resultado de la operacion": 7
    }

- http://127.0.0.1:8000/devops-evertec/operation/multiplicacion/12/4
    Resultado:
    {
        "operacion": "multiplicacion",
        "valor 1": 12,
        "valor 2": 4,
        "resultado de la operacion": 48
    }

- http://127.0.0.1:8000/devops-evertec/operation/division/30/6
    Resultado:
    {
        "operacion": "division",
        "valor 1": 30,
        "valor 2": 6,
        "resultado de la operacion": 5
    }

# Contribute
Codigo realizado por Juan Carlos Manotas correo: jmanotas@gmail.com
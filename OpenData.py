from pathlib import Path
from pyexpat import features
import statistics
from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi import HTTPException
import requests
import csv
from fastapi.middleware.cors import CORSMiddleware
from io import StringIO

import uvicorn

app = FastAPI()

origins = [""]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)

API_URL = "https://services1.arcgis.com/nCKYwcSONQTkPA4K/arcgis/rest/services/TurismoPaisResid/FeatureServer/0/query"
static_dir = Path('./static')

app.mount("/static", StaticFiles(directory=static_dir), name="static")


class Comunidades(BaseModel):
    comunidad: str


class Pais(BaseModel):
    comunidad: str
    pais: str


class Area(BaseModel):
    tamañoMin: int
    tamañoMax: int
    comunidades: str


@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html", status_code=status.HTTP_302_FOUND)


@app.get("/autobuses")
async def autobuses():
    params = {
        "outFields": "*",
        "where": "1=1",
        "f": "geojson",
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    features = data["features"]

    return features


@app.post("/autobuses/aaaa")
async def autobuses(comunidades: Comunidades):
    comunidad = comunidades.comunidad

    print(comunidad)

    params = {
        "outFields": "*",
        "where": f"Texto = '{comunidad}'",
        "outSR": "4326",
        "f": "json",
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    features = data['features'][0]['attributes']

    return features


@app.post("/autobuses/bbbb")
async def autobuses(pais: Pais):
    paisElegido = pais.pais
    comunidad = pais.comunidad
    pais = pais.pais
    valorTotal = 0
    valorPais = 0

    print(comunidad)
    print(pais)

    params = {
        "outFields": "*",
        "where": f"Texto = '{comunidad}'",
        "outSR": "4326",
        "f": "json",
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    features = data['features'][0]['attributes']

    valorTotal = features["Total"]
    valorPais = features[f'{paisElegido}']

    return (valorPais/valorTotal) * 100


@app.post("/autobuses/cccc")
async def autobuses(comunidades: Comunidades):
    comunidad = comunidades.comunidad
    area = 0

    print(comunidad)

    params = {
        "outFields": "*",
        "where": f"Texto = '{comunidad}'",
        "outSR": "4326",
        "f": "json",
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    features = data['features'][0]['attributes']
    area = features['Shape__Area']

    return area


@app.post("/autobuses/dddd")
async def autobuses(comunidades: Comunidades):
    comunidad = comunidades.comunidad
    poblacionEspañola = 0
    poblacionTotal = 0

    print(comunidad)

    params = {
        "outFields": "*",
        "where": f"Texto = '{comunidad}'",
        "outSR": "4326",
        "f": "json",
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    features = data['features'][0]['attributes']

    poblacionTotal = features["Total"]
    poblacionEspañola = features["Residentes_en_España"]

    return poblacionTotal-poblacionEspañola

if __name__ == "__main__":
    print("-> Inicio integrado de servicIo web")
    uvicorn.run(app, host="52.41.36.82", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)

import pandas as pd
import numpy as np
import xgboost as xgb
from joblib import load
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Definir las condiciones del vuelo para realizar la predicci
class Opera(str):
    Aerolineas_Argentinas = "Aerolineas Argentinas"
    Aeromexico = "Aeromexico"
    Air_Canada = "Air Canada"
    Air_France = "Air France"
    Alitalia = "Alitalia"
    American_Airlines = "American Airlines"
    Austral = "Austral"
    Avianca = "Avianca"
    British_Airways = "British Airways"
    Copa_Air = "Copa Air"
    Delta_Air = "Delta Air"
    Gol_Trans = "Gol Trans"
    Grupo_LATAM = "Grupo LATAM"
    Iberia = "Iberia"
    JetSmart_SPA = "JetSmart SPA"
    KLM = "K.L.M."
    Lacsa = "Lacsa"
    Latin_American_Wings = "Latin American Wings"
    Oceanair_Linhas_Aereas = "Oceanair Linhas Aereas"
    Plus_Ultra_Lineas_Aereas = "Plus Ultra Lineas Aereas"
    Qantas_Airways = "Qantas Airways"
    Sky_Airline = "Sky Airline"
    United_Airlines = "United Airlines"


class Mes(int):
    Enero = 1
    Febrero = 2
    Marzo = 3
    Abril = 4
    Mayo = 5
    Junio = 6
    Julio = 7
    Agosto = 8
    Septiembre = 9
    Octubre = 10
    Noviembre = 11
    Diciembre = 12


class TipoVuelo(str):
    Internacional = "I"
    Nacional = "N"


class FlightInformation(BaseModel):
    OPERA: Opera = Opera.Grupo_LATAM
    MES: Mes = Mes.Enero
    TIPOVUELO: TipoVuelo = TipoVuelo.Internacional


# Create the Stack model

# Create the API
app = FastAPI(
    title="API de predicción de vuelos",
    description="API para predecir la probabilidad de que un vuelo se retrase",
    version="v1")

# Create the endpoint

model = load("./models/modelxgb_smote_RandomCV_final.pkl")


@app.get("/")
async def root():
    """
    Endpoint que devuelve un mensaje de bienvenida.
    """
    return {"message": "Welcome to the Flight Delay Prediction API"}


@app.post("/predict")
async def predict(flight_info: FlightInformation):
    """
    Endpoint que devuelve un valor float con la predicción de la probabilidad de que un vuelo se retrase.
    """
    data = pd.DataFrame(vars(flight_info), index=[0])
    probability = model.predict_proba(data).tolist()
    return {"Probabilidad de retraso": round(probability[0][1], 2)}

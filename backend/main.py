from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
import mqtt_sensor

database.criar_tabela()
mqtt_sensor.iniciar_mqtt()

app = FastAPI(title="API Medições IoT")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "API rodando com sucesso"}

@app.get("/api/medicoes")
def obter_historico(limite: int = 50):
    return database.listar_medicoes(limite)

@app.post("/api/medicoes")
def registrar_medicao(distancia: float):
    database.salvar_medicao(distancia)
    return {"status": "sucesso", "distancia": distancia}
from fastapi import FastAPI
from Requests.Fund.Inference import Observation
from Processors.DDGNProcessor import DDGNProcessor
import pendulum
import json

## Initialize
app   = FastAPI()
agent = DDGNProcessor()
agent.loadBrain()




@app.get("/")
async def root():
    return {"message": "Welcome to The Sainpse Institute API Service"}

@app.post("/plutusinference")
async def predict(observation: Observation):
    print(Observation)
    choice = agent.decide(observation.observation)

    return {"choice": choice, "time":"now"}


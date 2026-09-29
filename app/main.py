from fastapi import FastAPI
from contextlib import asynccontextmanager
from .schema import Freight_rate_input, Freight_rate_output
from .model_service import load_artifact, freight_rate_prediction



# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    
    # Starting the process...
    load_artifact()
    
    # Shoutdow the process and clean it
    yield
    
    
app = FastAPI(
    title= "Freight Rate Predictor",
    version = '2.2',
    lifespan= lifespan
) 


@app.get('/')
def home_page():
    return {
        'Status': "Success",
        'message': "Welcome to our app"
    }
    
    
@app.post("/predict", response_model= Freight_rate_output)
def prediction(data: Freight_rate_input):
    
    result = freight_rate_prediction(data.model_dump())
    
    return Freight_rate_output(
        posted_rate= result["posted_rate"]
    )
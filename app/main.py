from fastapi import FastAPI
from pydantic import BaseModel
from app.Models.ModelPrediction import predictIrisFlower
from app.Models.ModelPrediction import __version__ as modelVersion

app = FastAPI()


# Inheresit from BaseModel, this is a Pydantic model that defines the input data structure for the prediction endpoint.
class FloatIn(BaseModel):
    sepalLength: float
    sepalWidth: float
    petalLength: float
    petalWidth: float


# Inherits from BaseModel, this is a Pydantic model that defines the output data structure for the prediction endpoint.
class PredictionOut(BaseModel):
    species: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": modelVersion}


@app.post("/predict", response_model=PredictionOut)
def predict(dimensions: FloatIn):
    """
    Predict the species of an iris flower based on its sepal and petal dimensions.
    """
    prediction = predictIrisFlower(
        dimensions.sepalLength,
        dimensions.sepalWidth,
        dimensions.petalLength,
        dimensions.petalWidth,
    )
    return {"species": prediction}

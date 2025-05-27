from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.Models.ModelPrediction import predictIrisFlower
from app.Models.ModelPrediction import __version__ as modelVersion

app = FastAPI()

# Adding CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for development; restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Inherits from BaseModel, this is a Pydantic model that defines the input data structure for the prediction endpoint.
class FloatIn(BaseModel):
    sepalLength: float
    sepalWidth: float
    petalLength: float
    petalWidth: float


# Inherits from BaseModel, this is a Pydantic model that defines the output data structure for the prediction endpoint.
class PredictionOut(BaseModel):
    species: str


@app.get("/health")
def healthCheck():
    return {"status": "Ok"}


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

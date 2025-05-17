"""
Title: Iris Flower Classification Prediction

Description: This script loads a pre-trained logestic regression model for iris flower classification
and uses it to make predictions based on user input.
The model is saved in a pickle file, and the script includes functions for loading the model, making predictions, and validating user input.

Author: Danielle Moore
Date: 2025-05-15
"""

import pandas as pd
import pickle
import re
from pathlib import Path

__version__: str = "0.1.0"

BASE_DIR: Path = Path(__file__).resolve(strict=True).parent

with open(BASE_DIR / f"irisLogRegModel-{__version__}.pkl", "rb") as modelFile:
    model = pickle.load(modelFile)


def predictIrisFlower(
    sepalLength: float, sepalWidth: float, petalLength: float, petalWidth: float
) -> str:
    """
    Predict the species of an iris flower based on its sepal and petal dimensions.

    Args:
        sepalLength (float): Length of the sepal in cm.
        sepalWidth (float): Width of the sepal in cm.
        petalLength (float): Length of the petal in cm.
        petalWidth (float): Width of the petal in cm.

    Returns:
        str: Predicted species of the iris flower.
    """
    inputDF: pd.DataFrame = pd.DataFrame(
        [
            {
                "sepal length (cm)": sepalLength,
                "sepal width (cm)": sepalWidth,
                "petal length (cm)": petalLength,
                "petal width (cm)": petalWidth,
            }
        ]
    )

    prediction = model.predict(inputDF)
    return prediction[0]


# prediction: str = predictIrisFlower(5.1, 3.5, 1.4, 0.2)
# print(prediction)
# print(model.feature_names_in_)

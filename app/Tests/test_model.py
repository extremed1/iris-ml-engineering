import pytest
from Models.ModelPrediction import predictIrisFlower


def test_PredictIrisSetosa():
    """Test prediction for Iris Setosa."""
    result = predictIrisFlower(5.1, 3.5, 1.4, 0.2)
    assert result == "setosa", f"Expected 'setosa', got {result}"


def test_PredictIrisVersicolor():
    """Test prediction for Versicolor"""
    result = predictIrisFlower(6.0, 2.2, 4.0, 1.0)
    assert result == "versicolor", f"Expected 'versicolor, got {result}"


def test_PredictIrisVirginica():
    """Test prediction for Virginica"""
    result = predictIrisFlower(6.5, 3.0, 5.2, 2.0)
    assert result == "virginica", f"Expected 'virginica', got {result}"

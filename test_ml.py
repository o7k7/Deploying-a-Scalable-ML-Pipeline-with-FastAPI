import numpy as np
import pytest
from sklearn.exceptions import NotFittedError

from ml.model import train_model, compute_model_metrics


@pytest.fixture
def sample_training_data():
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 1, 0, 1])
    return X_train, y_train

def test_train_model_returns_model(sample_training_data):
    X_train, y_train = sample_training_data
    model = train_model(X_train, y_train)
    assert model is not None
    assert hasattr(model, "predict")

def test_train_model_is_fitted(sample_training_data):
    X_train, y_train = sample_training_data
    model = train_model(X_train, y_train)
    assert hasattr(model, "coef_")
    try:
        model.predict(X_train)
    except NotFittedError:
        pytest.fail("Model training was incomplete")
    except Exception as e:
        pytest.fail(f"Model.predict(): {e}")

def test_compute_model_metrics_perfect_prediction():
    y_true = np.array([0, 1, 0, 1])
    y_preds = np.array([0, 1, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y_true, y_preds)
    assert precision == 1.0
    assert recall == 1.0
    assert fbeta == 1.0

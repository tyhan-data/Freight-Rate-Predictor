from pathlib import Path
import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models"/ "Linear_Regression.pkl"
PREPROCESSOR_DIR = BASE_DIR / "models"/ "preprocessor.pkl"


_model = None
_preprocessor = None


def load_artifact():
    global _model, _preprocessor
    
    if _model is None:
        _model = joblib.load(MODEL_PATH)
        
    if _preprocessor is None:
        _preprocessor = joblib.load(PREPROCESSOR_DIR)
        
        
def freight_rate_prediction(payload: dict):
    
    load_artifact()
    
    # Convert the data into dataframe
    data = pd.DataFrame([payload])
    
    # Preprocess the data into numeric
    data = _preprocessor.transform(data)
    
    # Prediction
    prediction = _model.predict(data)[0]
    
    return {
        "posted_rate": float(prediction)
    }
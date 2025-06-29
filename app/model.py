import joblib
import numpy as np

model, feature_names = joblib.load("saved_models/model.pkl")

def predict_price(features: dict):
    # Map features vào đúng thứ tự
    input_data = np.array([features[feat] for feat in feature_names]).reshape(1, -1)
    prediction = model.predict(input_data)
    return float(prediction[0])

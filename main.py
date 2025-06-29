from fastapi import FastAPI
from app.model import predict_price
from app.schemas import HouseFeatures, PricePrediction

app = FastAPI(
    title="🏠 House Price Prediction API",
    description="API dự đoán giá nhà bằng mô hình học máy",
    version="1.0.0"
)


@app.get("/")
def root():
  return {"message": "Chào mừng đến với House Price Prediction API 🎉"}


@app.post("/predict", response_model=PricePrediction)
def predict(data: HouseFeatures):
  prediction = predict_price(data.dict(by_alias=True))
  return {"SalePrice": round(prediction, 2)}

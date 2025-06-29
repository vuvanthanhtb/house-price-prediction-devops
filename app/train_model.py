import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Load dữ liệu
df = pd.read_csv("data/train.csv")

# Lấy các cột số
df = df.select_dtypes(include=["number"])
df = df.dropna()

# X, y
selected_features = [
    "OverallQual", "GrLivArea", "GarageCars", "GarageArea",
    "TotalBsmtSF", "1stFlrSF", "FullBath", "TotRmsAbvGrd", "YearBuilt"
]

X = df[selected_features]
y = df["SalePrice"]

# Huấn luyện mô hình
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Lưu mô hình và danh sách feature
os.makedirs("saved_models", exist_ok=True)
joblib.dump((model, list(X.columns)), "saved_models/model.pkl")
print("✅ Đã lưu mô hình vào saved_models/model.pkl")

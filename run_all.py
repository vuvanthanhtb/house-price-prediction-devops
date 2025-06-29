import os
import subprocess

# Huấn luyện mô hình
print("🔧 Huấn luyện mô hình...")
subprocess.run(["python", "app/train_model.py"], check=True)

# Chạy FastAPI
print("🚀 Khởi động FastAPI tại http://127.0.0.1:8000 ...")
subprocess.run(["uvicorn", "main:app", "--reload"])

from pydantic import BaseModel, Field


class HouseFeatures(BaseModel):
  OverallQual: int
  GrLivArea: int
  GarageCars: int
  GarageArea: int
  TotalBsmtSF: int
  FirstFlrSF: int = Field(..., alias="1stFlrSF")
  FullBath: int
  TotRmsAbvGrd: int
  YearBuilt: int

  class Config:
    validate_by_name = True


class PricePrediction(BaseModel):
  SalePrice: float

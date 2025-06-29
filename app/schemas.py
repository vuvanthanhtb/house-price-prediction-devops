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
    allow_population_by_field_name = True


class PricePrediction(BaseModel):
  SalePrice: float

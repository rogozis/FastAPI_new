from pydantic import BaseModel, Field

class CartAddOrDelete(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)

    class Config:
        from_attributes = True

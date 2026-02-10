from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=4, max_length=20)

class ProductSchema(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=4, max_length=20)
    price: int = Field(gt=0)
    category_id: int = Field(gt=0)

class CartAddOrDelete(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)

class CategorySchema(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=4, max_length=20)

    class Config:
        from_attributes = True

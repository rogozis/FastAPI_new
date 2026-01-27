from database import Base, engine
from sqlalchemy import Column, Integer, String, create_engine

class UserCart(Base):
    __tablename__ = 'UserCart'

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    quantity = Column(Integer)

class ShopGoods(Base):
    __tablename__ = 'Goods'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)

Base.metadata.create_all(bind=engine)

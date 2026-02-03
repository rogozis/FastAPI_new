from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///db_recs"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    avg_check = Column(Integer)
    last_category_id = Column(Integer)
    loyalty_score = Column(Float)

class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    category_id = Column(Integer)

class Order(Base):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    product_id = Column(Integer, ForeignKey('Product.id'))
    total = Column(Float)
    created_at = Column(DateTime)

class Cart(Base):
    __tablename__ = 'Cart'

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, ForeignKey('Product.name'))
    user_id = Column(Integer, ForeignKey('User.id'))
    product_id = Column(Integer, ForeignKey('Product.id'))
    quantity = Column(Integer, default=1)

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
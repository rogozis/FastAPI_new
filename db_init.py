from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
# from sqlalchemy import text

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

class Category(Base):
    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('Category.id'))

    category = relationship('Category')

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
    user_id = Column(Integer, ForeignKey('User.id'))
    product_id = Column(Integer, ForeignKey('Product.id'))
    quantity = Column(Integer, default=1)

    product = relationship('Product')

"""Mechanisms for adding data to DB ⬇️"""

# add_cat = [
#     {'id': 1, 'name': 'Dairy'},
#     {'id': 2, 'name': 'Bakery'},
#     {'id': 3, 'name': 'Drinks'},
#     {'id': 4, 'name': 'Grocery'}]
# for cat in add_cat:
#     session.add(Category(**cat))
#
# change_prods_dairy = session.query(Product).filter(Product.id.in_([1, 3, 4, 5])).update(
#     {'category_name': 'Dairy'}, synchronize_session="evaluate"
# )
#
# change_prods_bakery = session.get(Product, 2)
# change_prods_bakery.category_name = 'Bakery'
#
# change_prods_drinks = session.get(Product, 10)
# change_prods_drinks.category_name = 'Drinks'
#
# change_prods_grocery = session.query(Product).filter(Product.id.in_([6, 7, 8, 9])).update(
#     {'category_name': 'Grocery'}, synchronize_session="evaluate"
# )
# session.commit()
#
# Base.metadata.drop_all(bind=engine)

# with engine.connect() as conn:
#     conn.execute(text('ALTER TABLE "Cart" DROP COLUMN product_name'))
#     conn.commit()

Base.metadata.create_all(bind=engine)
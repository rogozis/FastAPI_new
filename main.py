from fastapi import FastAPI, HTTPException

from db_init import User, session, Cart, Product
from est_model import estimation_model
from pydantic_schemas import CartAddOrDelete

app = FastAPI(title='Recommendation System and Loyalty Estimation API')

"""
Endpoint to estimate user loyalty
It gets user id and returns score through model calculations
"""
@app.get('/loyalty/{user_id}')
def estimate_user_loyalty(user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    features = [user.avg_check, user.last_category_id, user.loyalty_score]
    score = estimation_model.predict(features)

    # print({'user': user.id, 'score': score})
    return {'user': user.id, 'score': score}


"""Endpoint to add product to user cart (implemented using simple DB)"""
@app.post('/add_to_cart/{user_id}/{product_id}')
def add_to_cart(user_id: int, cart_data: CartAddOrDelete):
    product = session.query(Product).filter(Product.id == cart_data.product_id).first()
    user_check = session.query(User).filter(User.id == user_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if not user_check:
        raise HTTPException(status_code=404, detail="User not found")

    existing = session.query(Cart).filter(
        Cart.user_id == user_id,
        Cart.product_id == cart_data.product_id,
    ).first()

    if existing:
        existing.quantity += cart_data.quantity
    else:
        cart_item = (Cart(user_id=user_id, quantity=cart_data.quantity, product_id=cart_data.product_id))
        session.add(cart_item)
    session.commit()
    return {'status': 'added',
            'quantity': cart_data.quantity,
            'product_name': product.name,
            'category_name': product.category.name,
            'product_id': cart_data.product_id}


"""Endpoint to remove product from user cart (implemented using simple DB)"""
@app.delete('/remove_from_cart/{user_id}/{product_id}')
def remove_from_cart(user_id: int, cart_data: CartAddOrDelete):
    user_check = session.query(User).filter(User.id == user_id).first()
    existing = session.query(Cart).filter(Cart.product_id == cart_data.product_id, Cart.quantity == cart_data.quantity).first()
    product = session.query(Product).filter(Product.id == cart_data.product_id).first()

    if not existing:
        return {'status': 'have nothing to remove'}
    if not user_check:
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(existing)
    session.commit()
    return {'status': 'removed', 'user_id': user_id, 'product_id': cart_data.product_id, 'product_name': product.name, 'quantity': cart_data.quantity}


"""Endpoint to clear whole cart"""
@app.delete('/clear_cart/')
def clear_cart():
    if not session.query(Cart).all():
        return {'status': 'nothing to clear'}

    session.query(Cart).delete()
    session.commit()
    return {'status': 'cleared'}


"""Endpoint to recommend nearest products to user according to his last added product"""
@app.get('/recommend_nearest/{user_id}')
def recommend_nearest_products(user_id: int):
    session.query(Cart).filter(Cart.product_id == user_id).all()


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
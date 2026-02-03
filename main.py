from fastapi import FastAPI, HTTPException
from db_init import User, session, Cart, Product
from est_model import estimation_model

app = FastAPI(title='Recommendation System and Loyalty Estimation API')

"""Endpoint to estimate user loyalty"""
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
def add_to_cart(user_id: int, product_id: int, quantity: int = 1):
    existing = session.query(Cart).filter(Cart.user_id == user_id, Cart.product_id == product_id).first()
    product = session.get(Product, product_id)

    if existing:
        existing.quantity += quantity
    else:
        cart_item = (Cart(user_id=user_id, product_id=product_id, quantity=quantity, product_name=product.name))
        session.add(cart_item)
    session.commit()
    return {'status': 'added', 'product_id': product_id, 'quantity': quantity, 'product_name': product.name}


"""Endpoint to remove product from user cart (implemented using simple DB)"""
@app.delete('/remove_from_cart/{user_id}/{product_id}')
def remove_from_cart(user_id: int, product_id: int, quantity: int = 1):
    existing = session.get(Cart, product_id)
    if not existing:
        return {'status': 'have nothing to remove'}

    session.delete(existing)
    session.commit()
    return {'status': 'removed', 'user_id': user_id, 'product_id': product_id, 'quantity': quantity}


"""Endpoint to clear whole cart"""
@app.delete('/clear_cart/')
def clear_cart():
    session.query(Cart).delete()
    session.commit()
    return {'status': 'cleared'}


"""Endpoint to recommend nearest products to user according to his last added product"""
@app.get('/recommend_nearest/{user_id}')
def recommend_nearest_products(user_id: int):
    session.query(Cart).filter(Cart.product_id == user_id).all()
# Need to add products relations

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
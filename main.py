from fastapi import FastAPI

app = FastAPI(title='Recommendation System for User Cart')


@app.get("/user_cart")
def get_user_cart():
    return {"cart": ["item1", "item2", "item3"]}

# @app.post("/requests")
# def send_prompt(
#     prompt: str = Body(embed=True)
# ):
#     answer = get_answer_from_gemini(prompt)
#     return {"answer": answer}
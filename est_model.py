import numpy as np

class Estimator:
    def __init__(self):
        # Scores for features avg_check, last_category_id, loyalty_score
        self.weights = np.array([0.475, 0.05, 0.475])

    def predict(self, features: list):
        # Fast matrix multiplication (Dot product)
        score = np.dot(features, self.weights)
        return float(score)


estimation_model = Estimator()

"""
This model contains two functions - init and predict
Init creates self object with weights variable, which can be used as method
Weights contain floats referring to columns in class User
Model predicts loyalty score based on features. Digits have no context, it's just work instance
"""
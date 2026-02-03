import numpy as np

class Estimator:
    def __init__(self):
        # Веса для фичей: avg_check, last_category_id, loyalty_score
        self.weights = np.array([0.475, 0.05, 0.475])

    def predict(self, features: list):
        # Быстрое матричное умножение (Dot product)
        score = np.dot(features, self.weights)
        return float(score)


estimation_model = Estimator()
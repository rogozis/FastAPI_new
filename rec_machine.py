import datetime
from typing import List, Dict, Any


class WeightMachine:
    def __init__(self, db_data: List[Dict[str, Any]]):
        self.db = {item['id']: item for item in db_data}
        self.current_seasob = self._get_season()

    def _get_season(self) -> str:
        month = datetime.date.today().month
        if month in [12, 1, 2]: return 'winter'
        elif month in [6, 7, 8]: return 'summer'
        return 'all'

    def get_recommendations(self, cart_ids: List[int]) -> List[Dict[str, Any]]:
        scores = {}
        for p_id in cart_ids:
            product = self.db.get[p_id]
            if not product: continue


        recommendations = []

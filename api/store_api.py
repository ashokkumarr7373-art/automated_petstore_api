import requests
from utils.config import Config

class StoreAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # ── Get inventory ──────────────────────────────────────────────
    def get_inventory(self):
        return requests.get(f"{self.base_url}/store/inventory", headers=self.headers)

    # ── Place an order ─────────────────────────────────────────────
    def place_order(self, payload):
        return requests.post(f"{self.base_url}/store/order", json=payload, headers=self.headers)

    # ── Get order by ID ────────────────────────────────────────────
    def get_order_by_id(self, order_id):
        return requests.get(f"{self.base_url}/store/order/{order_id}", headers=self.headers)

    # ── Delete order by ID ─────────────────────────────────────────
    def delete_order(self, order_id):
        return requests.delete(f"{self.base_url}/store/order/{order_id}", headers=self.headers)

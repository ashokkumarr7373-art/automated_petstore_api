import requests
from utils.config import Config

class UserAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # ── Create user ────────────────────────────────────────────────
    def create_user(self, payload):
        return requests.post(f"{self.base_url}/user", json=payload, headers=self.headers)

    # ── Create users with array ────────────────────────────────────
    def create_users_with_array(self, payload):
        return requests.post(f"{self.base_url}/user/createWithArray", json=payload, headers=self.headers)

    # ── Create users with list ─────────────────────────────────────
    def create_users_with_list(self, payload):
        return requests.post(f"{self.base_url}/user/createWithList", json=payload, headers=self.headers)

    # ── Login ──────────────────────────────────────────────────────
    def login(self, username, password):
        return requests.get(f"{self.base_url}/user/login",
                            params={"username": username, "password": password},
                            headers=self.headers)

    # ── Logout ─────────────────────────────────────────────────────
    def logout(self):
        return requests.get(f"{self.base_url}/user/logout", headers=self.headers)

    # ── Get user by username ───────────────────────────────────────
    def get_user_by_username(self, username):
        return requests.get(f"{self.base_url}/user/{username}", headers=self.headers)

    # ── Update user ────────────────────────────────────────────────
    def update_user(self, username, payload):
        return requests.put(f"{self.base_url}/user/{username}", json=payload, headers=self.headers)

    # ── Delete user ────────────────────────────────────────────────
    def delete_user(self, username):
        return requests.delete(f"{self.base_url}/user/{username}", headers=self.headers)

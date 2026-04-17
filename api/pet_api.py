import requests
from utils.config import Config

class PetAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # ── Add a new pet ──────────────────────────────────────────────
    def add_pet(self, payload):
        return requests.post(f"{self.base_url}/pet", json=payload, headers=self.headers)

    # ── Update an existing pet ─────────────────────────────────────
    def update_pet(self, payload):
        return requests.put(f"{self.base_url}/pet", json=payload, headers=self.headers)

    # ── Find pets by status ────────────────────────────────────────
    def get_pets_by_status(self, status):
        return requests.get(f"{self.base_url}/pet/findByStatus", params={"status": status}, headers=self.headers)

    # ── Find pet by ID ─────────────────────────────────────────────
    def get_pet_by_id(self, pet_id):
        return requests.get(f"{self.base_url}/pet/{pet_id}", headers=self.headers)

    # ── Update pet with form data ──────────────────────────────────
    def update_pet_with_form(self, pet_id, name=None, status=None):
        data = {}
        if name:
            data["name"] = name
        if status:
            data["status"] = status
        return requests.post(f"{self.base_url}/pet/{pet_id}",
                             data=data,
                             headers={"Accept": "application/json"})

    # ── Delete a pet ───────────────────────────────────────────────
    def delete_pet(self, pet_id, api_key="special-key"):
        return requests.delete(f"{self.base_url}/pet/{pet_id}",
                               headers={"api_key": api_key, "Accept": "application/json"})

    # ── Upload pet image ───────────────────────────────────────────
    def upload_pet_image(self, pet_id, file_path, additional_metadata=None):
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if additional_metadata:
                data["additionalMetadata"] = additional_metadata
            return requests.post(f"{self.base_url}/pet/{pet_id}/uploadFile",
                                 files=files, data=data,
                                 headers={"Accept": "application/json"})

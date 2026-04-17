import pytest
from api.pet_api import PetAPI
from api.store_api import StoreAPI
from api.user_api import UserAPI


# ── Pet Fixtures ───────────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def pet_api():
    return PetAPI()


@pytest.fixture(scope="session")
def new_pet_payload():
    return {
        "id": 100101,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Tommy",
        "photoUrls": ["https://example.com/tommy.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }


@pytest.fixture(scope="session")
def created_pet(pet_api, new_pet_payload):
    response = pet_api.add_pet(new_pet_payload)
    assert response.status_code == 200
    return response.json()


# ── Store Fixtures ─────────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def store_api():
    return StoreAPI()


@pytest.fixture(scope="session")
def new_order_payload():
    return {
        "id": 500501,
        "petId": 100101,
        "quantity": 1,
        "shipDate": "2026-04-15T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }


@pytest.fixture(scope="session")
def placed_order(store_api, new_order_payload):
    response = store_api.place_order(new_order_payload)
    assert response.status_code == 200
    return response.json()


# ── User Fixtures ──────────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def user_api():
    return UserAPI()


@pytest.fixture(scope="session")
def new_user_payload():
    return {
        "id": 700701,
        "username": "testuser_ashok",
        "firstName": "Ashok",
        "lastName": "Gannisetti",
        "email": "ashok@test.com",
        "password": "Test@1234",
        "phone": "9999999999",
        "userStatus": 1
    }


@pytest.fixture(scope="session")
def created_user(user_api, new_user_payload):
    response = user_api.create_user(new_user_payload)
    assert response.status_code == 200
    return new_user_payload

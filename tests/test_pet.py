import allure
import pytest


@allure.feature("Pet")
class TestPet:

    @allure.story("Add Pet")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC001 - Add a new pet")
    def test_add_pet(self, pet_api, new_pet_payload):
        with allure.step("Send POST /pet with valid payload"):
            response = pet_api.add_pet(new_pet_payload)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify response contains correct pet details"):
            data = response.json()
            assert data["id"] == new_pet_payload["id"]
            assert data["name"] == new_pet_payload["name"]
            assert data["status"] == new_pet_payload["status"]

    @allure.story("Get Pet")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC002 - Get pet by ID")
    def test_get_pet_by_id(self, pet_api, new_pet_payload):
        with allure.step(f"Send GET /pet/{new_pet_payload['id']}"):
            response = pet_api.get_pet_by_id(new_pet_payload["id"])
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify pet ID and name in response"):
            data = response.json()
            assert data["id"] == new_pet_payload["id"]
            assert data["name"] == new_pet_payload["name"]

    @allure.story("Get Pet by Status")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC003 - Get pets by status - available")
    def test_get_pets_by_status_available(self, pet_api):
        with allure.step("Send GET /pet/findByStatus?status=available"):
            response = pet_api.get_pets_by_status("available")
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify response is a non-empty list of available pets"):
            data = response.json()
            assert isinstance(data, list)
            assert len(data) > 0
            for pet in data:
                assert pet["status"] == "available"

    @allure.story("Get Pet by Status")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC004 - Get pets by status - pending")
    def test_get_pets_by_status_pending(self, pet_api):
        with allure.step("Send GET /pet/findByStatus?status=pending"):
            response = pet_api.get_pets_by_status("pending")
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify response is a list"):
            data = response.json()
            assert isinstance(data, list)

    @allure.story("Get Pet by Status")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC005 - Get pets by status - sold")
    def test_get_pets_by_status_sold(self, pet_api):
        with allure.step("Send GET /pet/findByStatus?status=sold"):
            response = pet_api.get_pets_by_status("sold")
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify response is a list"):
            data = response.json()
            assert isinstance(data, list)

    @allure.story("Update Pet")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC006 - Update an existing pet")
    def test_update_pet(self, pet_api, new_pet_payload):
        updated_payload = new_pet_payload.copy()
        updated_payload["name"] = "Tommy Updated"
        updated_payload["status"] = "sold"
        with allure.step("Send PUT /pet with updated payload"):
            response = pet_api.update_pet(updated_payload)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify updated name and status in response"):
            data = response.json()
            assert data["name"] == "Tommy Updated"
            assert data["status"] == "sold"

    @allure.story("Update Pet")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC007 - Update pet with form data")
    def test_update_pet_with_form(self, pet_api, new_pet_payload):
        with allure.step("Send POST /pet/{petId} with form data"):
            response = pet_api.update_pet_with_form(
                pet_id=new_pet_payload["id"],
                name="Tommy Form Updated",
                status="pending"
            )
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Get Pet")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC008 - Get pet by invalid ID expects 404")
    def test_get_pet_by_invalid_id(self, pet_api):
        with allure.step("Send GET /pet/999999999 (non-existent ID)"):
            response = pet_api.get_pet_by_id(999999999)
        with allure.step("Verify status code is 404"):
            assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @allure.story("Delete Pet")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC009 - Delete a pet")
    def test_delete_pet(self, pet_api, new_pet_payload):
        with allure.step(f"Send DELETE /pet/{new_pet_payload['id']}"):
            response = pet_api.delete_pet(new_pet_payload["id"])
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Delete Pet")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC010 - Get deleted pet expects 404")
    def test_get_deleted_pet(self, pet_api, new_pet_payload):
        with allure.step("Send GET /pet/{id} for already deleted pet"):
            response = pet_api.get_pet_by_id(new_pet_payload["id"])
        with allure.step("Verify status code is 404"):
            assert response.status_code == 404, f"Expected 404 for deleted pet, got {response.status_code}"

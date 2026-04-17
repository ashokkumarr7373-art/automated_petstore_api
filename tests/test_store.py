import allure
import pytest


@allure.feature("Store")
class TestStore:

    @allure.story("Inventory")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC001 - Get store inventory")
    def test_get_inventory(self, store_api):
        with allure.step("Send GET /store/inventory"):
            response = store_api.get_inventory()
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify response is a non-empty dict"):
            data = response.json()
            assert isinstance(data, dict)
            assert len(data) > 0

    @allure.story("Place Order")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC002 - Place a new order")
    def test_place_order(self, store_api, new_order_payload):
        with allure.step("Send POST /store/order with valid payload"):
            response = store_api.place_order(new_order_payload)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify order details in response"):
            data = response.json()
            assert data["id"] == new_order_payload["id"]
            assert data["petId"] == new_order_payload["petId"]
            assert data["status"] == new_order_payload["status"]

    @allure.story("Get Order")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC003 - Get order by ID")
    def test_get_order_by_id(self, store_api, new_order_payload):
        with allure.step(f"Send GET /store/order/{new_order_payload['id']}"):
            response = store_api.get_order_by_id(new_order_payload["id"])
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify order ID and petId in response"):
            data = response.json()
            assert data["id"] == new_order_payload["id"]
            assert data["petId"] == new_order_payload["petId"]

    @allure.story("Get Order")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC004 - Get order by invalid ID expects 404")
    def test_get_order_by_invalid_id(self, store_api):
        with allure.step("Send GET /store/order/999999 (non-existent order)"):
            response = store_api.get_order_by_id(999999)
        with allure.step("Verify status code is 404"):
            assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @allure.story("Place Order")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC005 - Place order with minimal payload")
    def test_place_order_minimal_payload(self, store_api):
        minimal_payload = {
            "id": 500502,
            "petId": 100101,
            "quantity": 2,
            "status": "placed"
        }
        with allure.step("Send POST /store/order with minimal payload"):
            response = store_api.place_order(minimal_payload)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Delete Order")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC006 - Delete an order")
    def test_delete_order(self, store_api, new_order_payload):
        with allure.step(f"Send DELETE /store/order/{new_order_payload['id']}"):
            response = store_api.delete_order(new_order_payload["id"])
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Delete Order")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC007 - Get deleted order expects 404")
    def test_get_deleted_order(self, store_api, new_order_payload):
        with allure.step("Send GET /store/order/{id} for already deleted order"):
            response = store_api.get_order_by_id(new_order_payload["id"])
        with allure.step("Verify status code is 404"):
            assert response.status_code == 404, f"Expected 404 for deleted order, got {response.status_code}"

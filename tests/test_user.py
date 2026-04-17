import allure
import pytest


@allure.feature("User")
class TestUser:

    @allure.story("Create User")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC001 - Create a new user")
    def test_create_user(self, user_api, new_user_payload):
        with allure.step("Send POST /user with valid payload"):
            response = user_api.create_user(new_user_payload)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Get User")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC002 - Get user by username")
    def test_get_user_by_username(self, user_api, new_user_payload):
        with allure.step(f"Send GET /user/{new_user_payload['username']}"):
            response = user_api.get_user_by_username(new_user_payload["username"])
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify username and email in response"):
            data = response.json()
            assert data["username"] == new_user_payload["username"]
            assert data["email"] == new_user_payload["email"]

    @allure.story("Login")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("TC003 - Login with valid credentials")
    def test_login_valid(self, user_api, new_user_payload):
        with allure.step("Send GET /user/login with valid username and password"):
            response = user_api.login(
                username=new_user_payload["username"],
                password=new_user_payload["password"]
            )
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify message is present in response"):
            data = response.json()
            assert "message" in data

    @allure.story("Login")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC004 - Login with invalid credentials")
    def test_login_invalid(self, user_api):
        with allure.step("Send GET /user/login with invalid credentials"):
            response = user_api.login(username="invaliduser", password="wrongpass")
        with allure.step("Verify status code is 200 (Petstore mock always returns 200)"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Verify message key exists in response"):
            data = response.json()
            assert "message" in data

    @allure.story("Logout")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC005 - Logout user")
    def test_logout(self, user_api):
        with allure.step("Send GET /user/logout"):
            response = user_api.logout()
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Update User")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC006 - Update user details")
    def test_update_user(self, user_api, new_user_payload):
        updated_payload = new_user_payload.copy()
        updated_payload["firstName"] = "Ashok Updated"
        updated_payload["email"] = "ashok_updated@test.com"
        with allure.step(f"Send PUT /user/{new_user_payload['username']} with updated payload"):
            response = user_api.update_user(new_user_payload["username"], updated_payload)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Create User")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC007 - Create users with array")
    def test_create_users_with_array(self, user_api):
        payload = [
            {
                "id": 700702,
                "username": "arrayuser1",
                "firstName": "Array",
                "lastName": "User1",
                "email": "arrayuser1@test.com",
                "password": "Test@1234",
                "phone": "8888888881",
                "userStatus": 1
            },
            {
                "id": 700703,
                "username": "arrayuser2",
                "firstName": "Array",
                "lastName": "User2",
                "email": "arrayuser2@test.com",
                "password": "Test@1234",
                "phone": "8888888882",
                "userStatus": 1
            }
        ]
        with allure.step("Send POST /user/createWithArray with 2 users"):
            response = user_api.create_users_with_array(payload)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Create User")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC008 - Create users with list")
    def test_create_users_with_list(self, user_api):
        payload = [
            {
                "id": 700704,
                "username": "listuser1",
                "firstName": "List",
                "lastName": "User1",
                "email": "listuser1@test.com",
                "password": "Test@1234",
                "phone": "7777777771",
                "userStatus": 1
            }
        ]
        with allure.step("Send POST /user/createWithList with 1 user"):
            response = user_api.create_users_with_list(payload)
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Get User")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC009 - Get non-existent user expects 404")
    def test_get_nonexistent_user(self, user_api):
        with allure.step("Send GET /user/nonexistentuser_xyz_999"):
            response = user_api.get_user_by_username("nonexistentuser_xyz_999")
        with allure.step("Verify status code is 404"):
            assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @allure.story("Delete User")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC010 - Delete a user")
    def test_delete_user(self, user_api, new_user_payload):
        with allure.step(f"Send DELETE /user/{new_user_payload['username']}"):
            response = user_api.delete_user(new_user_payload["username"])
        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    @allure.story("Delete User")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC011 - Get deleted user expects 404")
    def test_get_deleted_user(self, user_api, new_user_payload):
        with allure.step("Send GET /user/{username} for already deleted user"):
            response = user_api.get_user_by_username(new_user_payload["username"])
        with allure.step("Verify status code is 404"):
            assert response.status_code == 404, f"Expected 404 for deleted user, got {response.status_code}"

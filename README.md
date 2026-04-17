# Swagger Petstore API Automation

A fully structured Python pytest framework for automating the [Swagger Petstore API](https://petstore.swagger.io/).

---

## 📁 Project Structure

```
api_swaggerpet/
├── api/
│   ├── pet_api.py          # All Pet endpoints
│   ├── store_api.py        # All Store endpoints
│   └── user_api.py         # All User endpoints
├── conftest.py             # Shared pytest fixtures
├── tests/
│   ├── test_pet.py         # 10 Pet test cases
│   ├── test_store.py       # 7 Store test cases
│   └── test_user.py        # 11 User test cases
├── utils/
│   └── config.py           # Base URL config via .env
├── reports/                # HTML test reports output
├── .env                    # Environment variables
├── pytest.ini              # Pytest configuration
└── requirements.txt        # Dependencies
```

---

## ⚙️ Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure environment
The `.env` file already has:
```
BASE_URL=https://petstore.swagger.io/v2
```

---

## ▶️ Run Tests

### Run all tests
```bash
pytest
```

### Run specific module
```bash
pytest tests/test_pet.py
pytest tests/test_store.py
pytest tests/test_user.py
```

### Run with verbose output
```bash
pytest -v
```

### Run and generate HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 🧪 Test Coverage

| Module      | Test Cases | Endpoints Covered |
|-------------|-----------|-------------------|
| Pet         | 10        | POST, GET, PUT, DELETE, Form Update |
| Store       | 7         | GET Inventory, POST Order, GET Order, DELETE Order |
| User        | 11        | POST, GET, PUT, DELETE, Login, Logout, Bulk Create |
| **Total**   | **28**    | All Petstore endpoints |

---

## 📊 HTML Report
After running tests, open:
```
reports/report.html
```

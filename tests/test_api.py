import requests

def test_api_login_success():
    """
    POST /api/login: kiểm tra status 200 và có token trả về.
    """
    url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url, json=payload)
    
    # Kiểm tra status code là 200
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Kiểm tra response chứa trường 'token' và không rỗng
    response_data = response.json()
    assert "token" in response_data, "Response does not chứa 'token'"
    assert response_data["token"], "Token bị rỗng"

def test_api_get_users_success():
    """
    GET /api/users: kiểm tra status 200 và mảng dữ liệu không rỗng.
    """
    url = "https://reqres.in/api/users"
    response = requests.get(url)
    
    # Kiểm tra status code là 200
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Kiểm tra mảng dữ liệu 'data' không rỗng
    response_data = response.json()
    assert "data" in response_data, "Response không chứa trường 'data'"
    assert isinstance(response_data["data"], list), "Dữ liệu trả về không phải là một danh sách"
    assert len(response_data["data"]) > 0, "Danh sách người dùng trống"

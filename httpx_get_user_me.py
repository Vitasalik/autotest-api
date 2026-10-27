import httpx

login_payload = {
    "email": "vitalya@mail.ru",
    "password": "qwerty123"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("\nStatus code:", login_response.status_code)
print("Login response: ", login_response_data)

access_token = login_response_data['token']['accessToken']
headers = {"Authorization": f"Bearer {access_token}"}


user_me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)

user_me_response_data = user_me_response.json()

print("\nStatus code:", user_me_response.status_code)
print("User me response: ", user_me_response_data)
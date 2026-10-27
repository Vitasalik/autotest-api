import httpx
from tools.fakers import get_random_email

create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_data = create_user_response.json()

print("\nStatus code:", create_user_response.status_code)
print("Create user:", create_user_data)


login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_data = login_response.json()

print("\nStatus code:", login_response.status_code)
print("Login user:", login_data)

access_token = login_data['token']['accessToken']
headers = {"Authorization": f"Bearer {access_token}"}

update_user_payload = {
    "email": get_random_email()
}

update_user_response = httpx.patch(
    f"http://127.0.0.1:8000/api/v1/users/{create_user_data['user']['id']}",
        headers=headers,
        json=update_user_payload
)
update_user_data = update_user_response.json()

print("\nStatus code:", update_user_response.status_code)
print("Login user:", update_user_data)


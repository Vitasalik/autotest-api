import httpx

responce = httpx.get("https://postman-echo.com/get")

print(responce.status_code)
print(responce.json())
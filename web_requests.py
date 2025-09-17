import requests
import json
# GET request
response = requests.get("https://jsonplaceholder.typicode.com/users")

# Convert response to JSON
users = response.json()

# Print info for first 3 users
for user in users[:3]:
    print("Name:",  user["name"])
    print("Email:", user["email"])
    print("Company:", user["company"]["name"])
    print("-" * 30)


with open("new_user.json", "r") as file:
    user_data = json.load(file)

posting = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=user_data   # requests will send as JSON automatically
)

print("Status Code:", posting.status_code)
print("Response:", posting.json())
import requests

url = "https://api.cpicpgx.org/v1/allele"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    count = 0

    for version in data:
        if version.get("version") == 26:
            count += 1

    print("Count of objects with version 26 :", count)

else:
    print("Error: Failed to retrieve data from the API.")

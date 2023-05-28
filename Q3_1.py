import requests

# Make the API request
url = "https://api.cpicpgx.org/v1/allele"
params = {
    "genesymbol": "eq.CYP2D6"
}
response = requests.get(url, params=params)

# Parse the JSON response
data = response.json()

# Iterate through each allele
for allele in data:
    allele_id = allele["id"]
    frequency = allele.get("frequency")

    if frequency is not None:
        # Check each ethnicity frequency
        for ethnicity, value in frequency.items():
            if value is not None and value >= 1:
                # Frequency is not lower than 1 or null, handle the condition not being met
                print(f"Condition not met for allele {allele_id}, ethnicity {ethnicity}")
    else:
        # Handle the case where 'frequency' is null or missing
        print(f"No frequency data found for allele {allele_id}")

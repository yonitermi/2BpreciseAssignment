import requests

# Make the API request
url = "https://api.cpicpgx.org/v1/allele"
params = {
    "genesymbol": "eq.CYP2D6"
}
response = requests.get(url, params=params)

# Parse the JSON response
data = response.json()

# Create a dictionary to store the sum of frequencies for each ethnicity
ethnicity_sums = {}

# Iterate through each allele
for allele in data:
    frequency = allele.get("frequency")
    if frequency is not None:
        # Iterate through each ethnicity frequency
        for ethnicity, value in frequency.items():
            if value is not None:
                if ethnicity in ethnicity_sums:
                    ethnicity_sums[ethnicity] += value
                else:
                    ethnicity_sums[ethnicity] = value

# Check the sum of frequencies for each ethnicity
for ethnicity, sum_value in ethnicity_sums.items():
    if sum_value >= 1:
        print(f"Sum of frequencies for ethnicity {ethnicity} is not lower than 1")

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
    findings = allele.get("findings")
    citations = allele.get("citations")
    evidence_strength = allele.get("strength")

    if findings:
        if citations or evidence_strength == "No Evidence":
            # The condition is met
            print(f"Condition met for allele {allele_id}")
        else:
            # The condition is not met
            print(f"Condition not met for allele {allele_id}")
    else:
        # There are no findings, so the condition is trivially met
        print(f"Condition met for allele {allele_id} (No findings)")

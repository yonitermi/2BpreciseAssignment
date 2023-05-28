import requests

url = "https://api.cpicpgx.org/v1/allele"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Extract the types of gene symbols
    gene_symbol_types = set()

    for entry in data:
        gene_symbol = entry.get("genesymbol")
        if gene_symbol:
            gene_symbol_types.add(gene_symbol)

    print("Gene Symbol Types:")
    for gene_symbol_type in gene_symbol_types:
        print(gene_symbol_type)

else:
    print("Error: ", response.status_code)

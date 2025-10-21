from Bio import Entrez
import pandas as pd

# Recolha e Pré-processamento de Artigos Científicos

Entrez.email = "conhecimentolinguagem@gmail.com"
term = '("disease"[MeSH Terms]) AND ("symptom"[Title/Abstract] OR "treatment"[Title/Abstract]) AND ("2020"[Date - Publication] : "2025"[Date - Publication])'


handle = Entrez.esearch(db="pubmed", term=term, retmax=100000)
record = Entrez.read(handle)
ids = record["IdList"]

articles = []
for pmid in ids:
    fetch = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="text")
    text = fetch.read()
    articles.append({"pmid": pmid, "text": text})

df = pd.DataFrame(articles)

print(df.head()) 
print(f"Total articles fetched: {len(df)}")
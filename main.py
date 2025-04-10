from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(title="API de Conversão de Moedas", version="1.0")

# Valores simulados de conversão
taxas = {
    "USD": {"BRL": 5.0975, "EUR": 0.91},
    "BRL": {"USD": 0.196, "EUR": 0.18},
    "EUR": {"USD": 1.10, "BRL": 5.55}
}

@app.get("/converter")
def converter_moeda(valor: float = Query(...), de: str = Query(...), para: str = Query(...)):
    de = de.upper()
    para = para.upper()
    
    if de not in taxas or para not in taxas[de]:
        return {"erro": "Conversão não suportada"}

    taxa = taxas[de][para]
    convertido = round(valor * taxa, 2)

    return {
        "de": de,
        "para": para,
        "valor_original": valor,
        "valor_convertido": convertido
    }

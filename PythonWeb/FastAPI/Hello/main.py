from fastapi import FastAPI

app = FastAPI()

vendas = {
    1:{"item": "lata", "preco": 5.5, "quantidade": 5},
    2:{"item": "Garrafa", "preco": 10, "quantidade": 1},
    3:{"item": "Mini Lata", "preco": 2.5, "quantidade": 1}
}

@app.get("/")
def home():
    return {"Vendas ": len(vendas)}

@app.get("/vendas/{id}")
def pegar_venda(id: int):
    return vendas[id]
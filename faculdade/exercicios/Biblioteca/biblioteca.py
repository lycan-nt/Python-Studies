from livro import Livro
from dataclasses import asdict
import matplotlib.pyplot as plt

biblioteca = []

def adicionar_livro(titulo, autor, genero, quantidade=1):
    titulo_norm = titulo.strip().lower()
    autor_norm = autor.strip().lower()
    for livro in biblioteca:
        if livro.titulo.strip().lower() == titulo_norm and livro.autor.strip().lower() == autor_norm:
            livro.quantidade += quantidade
            return livro
    novo = Livro(titulo=titulo.strip(), autor=autor.strip(), genero=genero.strip(), quantidade=quantidade)
    biblioteca.append(novo)
    return novo

def listar_livros():
    return [asdict(l) for l in biblioteca]

def buscar_por_titulo(titulo):
    termo = titulo.strip().lower()
    return [asdict(l) for l in biblioteca if termo in l.titulo.lower()]

def gerar_grafico_por_genero():
    if not biblioteca:
        raise ValueError("Nenhum livro cadastrado para gerar o gráfico.")
    
    genero_counts = {}
    for l in biblioteca:
        genero = l.genero.strip()
        genero_counts[genero] = genero_counts.get(genero, 0) + l.quantidade

    generos = list(genero_counts.keys())
    quantidades = [genero_counts[g] for g in generos]

    fig, ax = plt.subplots()
    ax.bar(generos, quantidades)
    ax.set_title('Quantidade de livros por gênero')
    ax.set_xlabel('Gênero')
    ax.set_ylabel('Quantidade')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

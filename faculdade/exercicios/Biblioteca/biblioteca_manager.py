"""Versão em um único arquivo: biblioteca_manager.py para rodar no colab ou similar."""

"""Sistema simples de gerenciamento de livros.
Implementa:
 - Classe Livro
 - Lista para armazenar livros
 - Funções: adicionar_livro, listar_livros, buscar_por_titulo, gerar_grafico_por_genero
 - Função de demonstração que popula alguns livros e exibe o gráfico usando matplotlib.
"""

from dataclasses import dataclass, asdict
import matplotlib.pyplot as plt

@dataclass
class Livro:
    titulo: str
    autor: str
    genero: str
    quantidade: int = 1

# Lista que armazena os livros
biblioteca = []

def adicionar_livro(titulo, autor, genero, quantidade=1):
    """Adiciona um livro à biblioteca. 
    Se já existir um livro com o mesmo título e autor, incrementa a quantidade."""
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
    """Retorna a lista de livros cadastrados."""
    return [asdict(l) for l in biblioteca]

def buscar_por_titulo(titulo):
    """Busca livros cujo título contenha a palavra informada (ignora maiúsculas/minúsculas)."""
    termo = titulo.strip().lower()
    return [asdict(l) for l in biblioteca if termo in l.titulo.lower()]

def gerar_grafico_por_genero():
    """Gera e exibe um gráfico de barras com a quantidade de livros por gênero."""
    if not biblioteca:
        raise ValueError("Nenhum livro cadastrado para gerar o gráfico.")
    
    # Contagem por gênero
    genero_counts = {}
    for l in biblioteca:
        genero = l.genero.strip()
        genero_counts[genero] = genero_counts.get(genero, 0) + l.quantidade

    # Preparar dados
    generos = list(genero_counts.keys())
    quantidades = [genero_counts[g] for g in generos]

    # Gerar gráfico
    fig, ax = plt.subplots()
    ax.bar(generos, quantidades)
    ax.set_title('Quantidade de livros por gênero')
    ax.set_xlabel('Gênero')
    ax.set_ylabel('Quantidade')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # 👇 Mostra o gráfico na tela
    plt.show()

def demonstracao_popular_e_gerar():
    """Popula a biblioteca com dados de exemplo e exibe o gráfico."""
    biblioteca.clear()
    adicionar_livro('Fundamentos de Python', 'João Silva', 'Programação', 3)
    adicionar_livro('Introdução à Matemática', 'Ana Pereira', 'Ciência', 2)
    adicionar_livro('Algoritmos e Estruturas', 'Carlos Lima', 'Programação', 4)
    adicionar_livro('História do Brasil', 'Mariana Souza', 'História', 1)
    adicionar_livro('Poemas Escolhidos', 'L. Branco', 'Literatura', 2)

    lista = listar_livros()
    busca = buscar_por_titulo('python')

    # Exibir gráfico diretamente
    gerar_grafico_por_genero()

    return {'lista': lista, 'busca_python': busca}

# Execução principal
if __name__ == '__main__':
    resultado = demonstracao_popular_e_gerar()
    print("Lista completa de livros:")
    for l in resultado['lista']:
        print(l)
    print("\nBusca por 'python':")
    for b in resultado['busca_python']:
        print(b)

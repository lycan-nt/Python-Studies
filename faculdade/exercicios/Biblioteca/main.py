from biblioteca import adicionar_livro, listar_livros, buscar_por_titulo, gerar_grafico_por_genero, biblioteca

"""Popula a biblioteca com dados de exemplo e exibe o gráfico."""
def demonstracao_popular_e_gerar():
    biblioteca.clear()
    adicionar_livro('Fundamentos de Python', 'João Silva', 'Programação', 3)
    adicionar_livro('Introdução à Matemática', 'Ana Pereira', 'Ciência', 2)
    adicionar_livro('Algoritmos e Estruturas', 'Carlos Lima', 'Programação', 4)
    adicionar_livro('História do Brasil', 'Mariana Souza', 'História', 1)
    adicionar_livro('Poemas Escolhidos', 'L. Branco', 'Literatura', 2)

    lista = listar_livros()
    busca = buscar_por_titulo('python')

    gerar_grafico_por_genero()

    return {'lista': lista, 'busca_python': busca}

if __name__ == '__main__':
    resultado = demonstracao_popular_e_gerar()
    print("Lista completa de livros:")
    for l in resultado['lista']:
        print(l)
    print("\nBusca por 'python':")
    for b in resultado['busca_python']:
        print(b)

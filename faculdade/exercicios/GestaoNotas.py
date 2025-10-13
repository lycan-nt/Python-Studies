"""Sistema de gestão de notas de alunos.
Funções:
 - cadastro de notas (lista)
 - cálculo de média
 - determinação de situação (aprovado/reprovado, média >= 7)
 - exibição de relatório final
 - função principal com interação opcional e exemplos de teste
"""

def adicionar_notas():
    """Permite ao usuário inserir notas
    """
    notas = []
    print("Insira as notas. Digite 'sair' para encerrar.")
    while True:
        entrada = input("Digite uma nota (0-10) ou 'sair': ").strip()
        if entrada.lower() in ('sair','exit','q','quit'):
            break
        try:
            nota = float(entrada.replace(',','.'))
            if nota < 0 or nota > 10:
                print("Nota inválida: deve ser entre 0 e 10.")
                continue
            notas.append(nota)
        except ValueError:
            print("Entrada inválida. Digite um número ou 'sair'.")
    return notas

def calcular_media(notas):
    """Calcula e retorna a média das notas. Se lista vazia, retorna None."""
    if not notas:
        return None
    return sum(notas) / len(notas)

def determinar_situacao(media, limite=7.0):
    """Retorna 'Aprovado' se media >= limite, caso contrário 'Reprovado'.
       Se media for None retorna 'Sem notas'."""
    if media is None:
        return "Sem notas"
    return "Aprovado" if media >= limite else "Reprovado"

def relatorio_final(nome_aluno, notas):
    """Gera uma string com o relatório contendo notas, média e situação."""
    media = calcular_media(notas)
    situacao = determinar_situacao(media)
    linhas = []
    linhas.append(f"Relatório do aluno: {nome_aluno}")
    linhas.append("-" * 40)
    if notas:
        linhas.append("Notas: " + ", ".join(f"{n:.2f}" for n in notas))
    else:
        linhas.append("Notas: (nenhuma nota registrada)")
    if media is not None:
        linhas.append(f"Média: {media:.2f}")
    else:
        linhas.append("Média: -")
    linhas.append(f"Situação: {situacao}")
    linhas.append("-" * 40)
    return "\n".join(linhas)

# Função de demonstração automática com dados de teste (Aprovado)
def demonstracao_aprovado(nome_aluno='Felipe D. Santos', notas_exemplo=None):
    if notas_exemplo is None:
        notas_exemplo = [8.5, 7.0, 9.0]
    texto = relatorio_final(nome_aluno, notas_exemplo)
    print(texto)
    return texto

# Função de demonstração automática com dados de teste (Reprovado)
def demonstracao_reprovado(nome_aluno='Felipe D. Santos', notas_exemplo=None):
    if notas_exemplo is None:
        notas_exemplo = [5.5, 4.0, 7.0]
    texto = relatorio_final(nome_aluno, notas_exemplo)
    print(texto)
    return texto

if __name__ == '__main__':
    # Se executado diretamente, rodar a demonstração (não entrar no modo interativo automaticamente).
    demonstracao_aprovado()
    demonstracao_reprovado()

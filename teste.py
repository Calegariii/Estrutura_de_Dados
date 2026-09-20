# ==============================================================================
# FUNÇÕES DO SISTEMA
# ==============================================================================

# Função: exibir_listagem
# Descrição: Percorre as listas paralelas e exibe todos os alunos cadastrados 
#            com suas respectivas três notas (AV1, AV2, AV3) formatadas.
# Parâmetros:
#   - alunos (list): Lista com os nomes dos alunos.
#   - av1 (list): Lista com as notas da Avaliação 1.
#   - av2 (list): Lista com as notas da Avaliação 2.
#   - av3 (list): Lista com as notas da Avaliação 3.
def exibir_listagem(alunos, av1, av2, av3):
    # VALIDAÇÃO: Verifica se existem alunos cadastrados antes de tentar iterar
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado. Utilize a opção 1 primeiro.")
        return

    # Cabeçalho da listagem
    print("--- Listagem geral de alunos ---")

    # Laço for para percorrer os vetores/listas paralelas sincronizadas pelo índice
    # O limite do laço é exatamente a quantidade atual de alunos cadastrados (len(alunos))
    for i in range(len(alunos)):
        # Formatação do número sequencial (i + 1) e notas com 1 casa decimal (:.1f)
        print(f"{i + 1} - {alunos[i]} | AV1: {av1[i]:.1f} | AV2: {av2[i]:.1f} | AV3: {av3[i]:.1f}")

    # Exibe o total de alunos cadastrados ao final do laço
    print(f"Total de alunos cadastrados: {len(alunos)}")


# ==============================================================================
# ESTRUTURA DO MENU / EXECUÇÃO DO SISTEMA
# ==============================================================================

# Listas paralelas (vetores) para armazenar os dados do sistema
alunos = []
av1 = []
av2 = []
av3 = []

# Exemplo de laço do menu principal
while True:
    print("\n--- MENU DE GERENCIAMENTO ---")
    print("1 - Cadastrar aluno e notas")
    print("2 - Exibir listagem geral de alunos e notas")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        # (Lógica da opção 1 - Cadastrar aluno)
        pass

    elif opcao == '2':
        # Chamada da função passando os vetores paralelos como argumento
        exibir_listagem(alunos, av1, av2, av3)

    elif opcao == '0':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
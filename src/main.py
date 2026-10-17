"""
TaskTracker - Gerenciador de Tarefas via Linha de Comando (CLI)

Bootcamp II - Fase 2 (Entrega Intermediaria)
Implementacao em Python 3 da receita logica definida na Fase 1.
"""

# Constantes e regras de negocio

# Prioridades aceitas (chave = o que o usuario digita; valor = como e salvo)
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

# Ordem usada na listagem: Alta -> Média -> Baixa
ORDEM_PRIORIDADE = {"Alta": 1, "Média": 2, "Baixa": 3}

STATUS_INICIAL = "Pendente"


# Funcoes de validacao de entrada

def ler_titulo():
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O título é obrigatório e não pode ficar vazio. Tente novamente.\n")


def ler_prioridade():
    while True:
        entrada = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("[ERRO] Prioridade inválida. Digite apenas Alta, Média ou Baixa.\n")


def ler_descricao():
    descricao = input("Descrição (opcional): ").strip()
    return descricao if descricao else "Sem descrição"


def ler_data_limite():
    data = input("Data limite (DD/MM/AAAA): ").strip()
    return data if data else "Não informada"


# Funcionalidades do sistema


def cadastrar_tarefa(tarefas):
    print("\n- CADASTRAR NOVA TAREFA -")

    titulo = ler_titulo()
    descricao = ler_descricao()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_INICIAL,  # definido automaticamente
    }

    tarefas.append(tarefa)
    print(f"\n[OK] Tarefa \"{titulo}\" cadastrada com sucesso! (ID {tarefa['id']})")


def listar_tarefas(tarefas):
    print("\n- TAREFAS CADASTRADAS -")

    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    ordenadas = sorted(tarefas, key=lambda t: ORDEM_PRIORIDADE[t["prioridade"]])

    for tarefa in ordenadas:
        print("-" * 40)
        print(f"ID:          {tarefa['id']}")
        print(f"Título:      {tarefa['titulo']}")
        print(f"Descrição:   {tarefa['descricao']}")
        print(f"Prioridade:  {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status:      {tarefa['status']}")
    print("-" * 40)
    print(f"Total de tarefas: {len(tarefas)}")


# Menu e loop principal

def exibir_menu():
    print("\n TASKTRACKER ")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("==XXXXXXXXX==")


def main():
    tarefas = []  # lista de tarefas mantida em memoria

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nAplicação encerrada pelo usuário.")

"""
TaskTracker - Gerenciador de Tarefas via Linha de Comando (CLI)

Bootcamp II - Fase 2 (Entrega Intermediaria)
Versao inicial: menu e loop principal (validacoes no proximo commit).
"""


def cadastrar_tarefa(tarefas):
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = input("Título da tarefa: ").strip()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = input("Prioridade (Alta / Média / Baixa): ").strip()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f"\n[OK] Tarefa \"{titulo}\" cadastrada com sucesso!")


def listar_tarefas(tarefas):
    print("\n--- TAREFAS CADASTRADAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return
    for tarefa in tarefas:
        print("-" * 40)
        for campo, valor in tarefa.items():
            print(f"{campo}: {valor}")
    print("-" * 40)


def exibir_menu():
    print("\n========== TASKTRACKER ==========")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=================================")


def main():
    tarefas = []
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
    main()

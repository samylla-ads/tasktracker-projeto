# TaskTracker

Gerenciador de tarefas via linha de comando (CLI), desenvolvido em Python 3 como parte do **Bootcamp II — Fase 2 (Entrega Intermediária)** do curso de Análise e Desenvolvimento de Sistemas (UniCEUB).

## Descrição

O TaskTracker ajuda o usuário a organizar suas tarefas diárias, permitindo cadastrar tarefas com prioridade e data limite e visualizá-las de forma organizada no terminal. Esta versão implementa a receita lógica planejada na Fase 1 (disponível em `docs/planejamento_logico.pdf`).

## Funcionalidades

- **Cadastrar nova tarefa** com título, descrição, prioridade e data limite
- **Visualizar tarefas cadastradas**, ordenadas por prioridade (Alta → Média → Baixa)
- **Sair da aplicação**

### Regras de negócio

| Campo | Regra |
|---|---|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e o sistema pede novamente. |
| Descrição | Livre (opcional). |
| Prioridade | Aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`. Qualquer outro valor gera erro e nova solicitação. |
| Data limite | Formato livre (sugestão: DD/MM/AAAA). |
| Status | Definido automaticamente como `Pendente` no cadastro. |

Se não houver tarefas cadastradas, a listagem informa que não existem registros no momento.

## Tecnologias

- Python 3 (sem bibliotecas externas)
- Git e GitHub para versionamento

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Instalação e execução

1. Tenha o **Python 3** instalado (`python --version` ou `python3 --version`).
2. Clone o repositório:
```bash
   git clone https://github.com/samylla-ads/tasktracker-projeto.git
   cd tasktracker-projeto
```
3. Execute a aplicação:
```bash
   python src/main.py
```
   (no Linux/macOS, use `python3 src/main.py`)

## Próximos passos (Fase 3)

Empacotamento da aplicação, containerização com Docker, testes e deploy.

## Autora

Sâmylla Lohana de Paiva — Análise e Desenvolvimento de Sistemas, UniCEUB (Polo Asa Norte)

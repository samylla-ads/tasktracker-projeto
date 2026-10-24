# TaskTracker

Gerenciador de tarefas via linha de comando (CLI), desenvolvido em Python 3 e empacotado com Docker como parte do **Bootcamp II** do curso de Análise e Desenvolvimento de Sistemas (UniCEUB).

## Descrição

O TaskTracker ajuda o usuário a organizar suas tarefas diárias, permitindo cadastrar tarefas com prioridade e data limite e visualizá-las de forma organizada no terminal. O projeto foi construído em três fases:

| Fase | Entrega |
|---|---|
| 1 | Planejamento lógico (`docs/planejamento_logico.pdf`) |
| 2 | Implementação em Python e versionamento com Git/GitHub (`src/main.py`) |
| 3 | Conteinerização e orquestração com Docker (`Dockerfile` e `docker-compose.yml`) |

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

- Python 3.11 (sem bibliotecas externas)
- Docker e Docker Compose
- Git e GitHub para versionamento

## Estrutura do projeto

```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
├── src/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Execução com Docker

Pré-requisito: ter o **Docker** instalado (Docker Desktop no Windows/macOS ou Docker Engine no Linux).

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/samylla-ads/tasktracker-projeto.git
cd tasktracker-projeto
```

### 1. Como construir a imagem

```bash
docker build -t tasktracker-app .
```

### 2. Como rodar o container em modo isolado

```bash
docker run -it --rm tasktracker-app
```

O parâmetro `-it` abre o modo interativo com terminal, necessário para usar o menu. O `--rm` remove o container ao sair.

### 3. Como rodar via orquestração (recomendado)

```bash
docker compose run --rm tasktracker
```

O `docker-compose.yml` já define `stdin_open: true` e `tty: true`, que mantêm o teclado e o terminal conectados ao container. Se a imagem ainda não existir, ela é construída automaticamente.

## Execução sem Docker (opcional)

Com o Python 3 instalado:

```bash
python src/main.py
```

## Autora

Sâmylla Lohana de Paiva — Análise e Desenvolvimento de Sistemas, UniCEUB (Polo Asa Norte)

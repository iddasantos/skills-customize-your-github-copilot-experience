# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprenda a criar uma API REST simples utilizando o framework FastAPI em Python. Você irá construir endpoints para manipular dados de uma lista de tarefas (to-do list).

## 📝 Tasks

### 🛠️ Criar Estrutura Básica da API

#### Description
Implemente uma API com FastAPI que permita listar, adicionar e remover tarefas de uma lista.

#### Requirements
Completed program should:

- Inicializar um projeto FastAPI
- Criar endpoint GET `/tasks` para listar todas as tarefas
- Criar endpoint POST `/tasks` para adicionar uma nova tarefa
- Criar endpoint DELETE `/tasks/{id}` para remover uma tarefa pelo id

### 🛠️ Adicionar Validação e Documentação

#### Description
Inclua validação dos dados recebidos e utilize os recursos de documentação automática do FastAPI.

#### Requirements
Completed program should:

- Validar que a tarefa possui um campo `title` não vazio
- Utilizar modelos Pydantic para definir os dados das tarefas
- Garantir que a documentação interativa (Swagger UI) está disponível

# Sistema de Registro de Alunos

Este é um projeto de aplicação Desktop completa para gerenciamento de estudantes, permitindo realizar todas as operações de um CRUD (Create, Read, Update, Delete).

Projeto desenvolvido com base no tutorial do canal **Nomada João**.

## Tecnologias Utilizadas
- **Python**: Linguagem base.
- **Tkinter**: Para a construção da interface gráfica.
- **SQLite**: Banco de dados relacional para armazenamento das informações.
- **Pillow (PIL)**: Processamento e exibição de imagens na interface.
- **Tkcalendar**: Widget para seleção de datas.

## Funcionalidades
- **Cadastrar**: Registro de novos alunos com foto e informações detalhadas.
- **Visualizar**: Listagem em tempo real de todos os alunos no banco de dados.
- **Atualizar**: Edição de dados de alunos já cadastrados.
- **Deletar**: Remoção segura de registros.
- **Banco de Dados**: Persistência de dados local com arquivo `.db`.

## Estrutura do Projeto
- `main.py`: Contém a lógica de conexão com o banco de dados e as funções de CRUD.
- `interface.py`: Gerencia a parte visual (frames, botões e tabelas).
- `Estudante.db`: Arquivo de banco de dados SQLite.

## Como Executar
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o arquivo da interface: `python interface.py`

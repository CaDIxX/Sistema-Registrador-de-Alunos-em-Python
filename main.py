import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('Estudante.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       email TEXT NOT NULL,
                       tel TEXT NOT NULL,
                       sexo TEXT NOT NULL,
                       data_nascimento TEXT NOT NULL,
                       endereco TEXT NOT NULL,
                       curso TEXT NOT NULL,
                       picture TEXT NOT NULL)''')


    def register_student(self, lista_estudantes):
        self.c.execute(f'INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                    (lista_estudantes))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro com sucesso!')


    def view_all_students(self):
        self.c.execute(f'SELECT * FROM estudantes')
        dados = self.c.fetchall()
        return dados


    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id = ?", (id,))
        dados = self.c.fetchone()
        return dados


    def update_student(self, novos_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?,sexo=? , data_nascimento=?, endereco=?, curso=?, picture=? WHERE id =?"
        self.c.execute(query,novos_valores)
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'O estudante com ID: {novos_valores[8]} foi atualizado!')


    def delete_student(self, id):
        self.c.execute('DELETE FROM estudantes WHERE id=?', (id,))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'O estudante com ID: {id} foi deletado!')

# Criando um instancia do registro do sistema de registro
sistema_de_registro = SistemaDeRegistro()

# # informações
# estudante = ('Helena3', 'helena@gmail.com', '465621213131', 'F', '5/10/2005', 'Angola, Canbinda', 'Medicina', 'imagem2.png')
# sistema_de_registro.register_student(estudante)
# ver estudantes
todos_alunos = sistema_de_registro.view_all_students()
print(todos_alunos)

# # # procurar aluno
# # aluno = sistema_de_registro.search_student(1)

# atualizar aluno
# estudante = ('Helena', 'helena@gmail.com', '465621213131', 'F', '5/10/2005', 'São Paulo, SP', 'Medicina', 'imagem2.png', 3)
# aluno = sistema_de_registro.update_student(estudante)

# sistema_de_registro.delete_student(2)
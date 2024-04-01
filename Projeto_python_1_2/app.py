import sqlite3
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, template_folder='templates')

conexao = sqlite3.connect('cadastros.db')

#criando variaveis para inserir no bando do dados
nome = "luiz eduardo"
cpf = "333.333.333.33"

#criando cursos para inserir os dados
# cursor = conexao.cursor()
# sql_insert = "insert into tabela_cadastro (nome, cpf) values (?, ?)"

# cursor.execute(sql_insert, (nome, cpf))

# id_pessoa = cursor.lastrowid
# conexao.commit()
# print(f"O ultimo codigo inserido foi {id_pessoa}")


#criando cursor para selecionar dados do banco
# print("pessoa  id 2 ")
# cursor = conexao.cursor()
# sql_select_unico = "SELECT * FROM tabela_cadastro WHERE  id_pessoa = ?"

# cursor.execute(sql_select_unico, (2, ))
# id_pessoa, nome, cpf = cursor.fetchone()
# print(f"{id_pessoa}----------{nome}-----------{cpf}")


# criando cursor para selecionar todo o banco
# cursor = conexao.cursor()
# sql_select_full = "SELECT * FROM tabela_cadastro"

# cursor.execute(sql_select_full)
# lista_cadastro = cursor.fetchall()
# for item in lista_cadastro:
#     print(item)


# criando cursor para atualizar um dado especifico atraves do ID
# cursor = conexao.cursor()
# sql_update = "UPDATE tabela_cadastro SET NOME = ? WHERE id_pessoa = ?"
# cursor.execute(sql_update, ("Virginia aparecida", 2))
# conexao.commit()


# criando cursor para deletar um dado especifico atraves do ID
cursor = conexao.cursor()
sql_delete = "DELETE FROM tabela_cadastro WHERE id_pessoa = ? "
cursor.execute(sql_delete, (2, ))
conexao.commit()








# Lista para armazenar os dados das pessoas cadastradas
# TESTE 3 qual arquivo usar

pessoas = []

# Rota para exibir a página inicial com a lista de pessoas cadastradas e opções CRUD
@app.route('/')
def index():
    return render_template('index.html', pessoas=pessoas)

# Rota para cadastrar uma nova pessoac
@app.route('/cadastrar', methods=['POST'])
def cadastrar_pessoa():
    nome = request.form['nome']
    cpf = request.form['cpf']
    pessoas.append({'nome': nome, 'cpf': cpf})
    return redirect(url_for('index'))

# Rota para editar uma pessoa
@app.route('/editar/<cpf>', methods=['GET', 'POST'])
def editar_pessoa(cpf):
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            if request.method == 'POST':
                pessoa['nome'] = request.form['nome']
                pessoa['cpf'] = request.form['cpf']
                return redirect(url_for('index'))
            return render_template('editar.html', pessoa=pessoa)
    return "Pessoa não encontrada."

# Rota para excluir uma pessoa
@app.route('/excluir/<cpf>')
def excluir_pessoa(cpf):
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            pessoas.remove(pessoa)
            return redirect(url_for('index'))
    return "Pessoa não encontrada."

if __name__ == '__main__':
    app.run(debug=True)

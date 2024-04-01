import sqlite3
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__, template_folder='templates')

#conexao = sqlite3.connect('cadastros.db')

#criando variaveis para inserir no bando do dados

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
def listar_pessoas():
    try:
        conexao = sqlite3.connect('cadastros.db')
        cursor = conexao.cursor()
        sql_select_full = "SELECT * FROM tabela_cadastro"
        cursor.execute(sql_select_full)
        pessoas = cursor.fetchall()
        conexao.close()
        return pessoas
    except :
        return False
    
    
    


# criando cursor para atualizar um dado especifico atraves do ID
# cursor = conexao.cursor()
# sql_update = "UPDATE tabela_cadastro SET NOME = ? WHERE id_pessoa = ?"
# cursor.execute(sql_update, ("Virginia aparecida", 2))
# conexao.commit()


# criando cursor para deletar um dado especifico atraves do ID
# cursor = conexao.cursor()
# sql_delete = "DELETE FROM tabela_cadastro WHERE id_pessoa = ? "
# cursor.execute(sql_delete, (2, ))
# conexao.commit()


#gerar id ou recuperar ultimo id usado
def gerar_id():
    conexao = sqlite3.connect('cadastros.db')
    cursor = conexao.cursor()
    cursor.execute("select seq from sqlite_sequence where name = 'tabela_cadastro'")
    next_id = cursor.fetchone()[0]
    return next_id + 1


# Lista para armazenar os dados das pessoas cadastradas


#pessoas = []

# Rota para exibir a página inicial com a lista de pessoas cadastradas e opções CRUD
@app.route('/')
def index():
   
    return render_template('index.html', pessoas=listar_pessoas())

# Rota para cadastrar uma nova pessoac
@app.route('/cadastrar', methods=['POST'])

#função de cadastrar pessoas
def cadastrar_pessoa():
    try:
        conexao = sqlite3.connect('cadastros.db')
        cursor = conexao.cursor()
        sql_insert = "insert into tabela_cadastro (nome, cpf) values (?, ?)"
        cursor.execute(sql_insert, (nome, cpf))
        id_pessoa = cursor.lastrowid
        conexao.commit()
        conexao.close()
        return id_pessoa
    except Exception as ex:
        print(ex)
        return False
    
    # nome = request.form['nome']
    # cpf = request.form['cpf']
    # pessoas.append({'nome': nome, 'cpf': cpf})
    # return redirect(url_for('index'))





# Rota para editar/atualizar uma pessoa
@app.route('/editar/<id_pessoa>', methods=['GET', 'POST'])

def editar_pessoa(id_pessoa:int, nome, cpf):
    try:
        conexao = sqlite3.connect('cadastros.db')
        cursor = conexao.cursor()
        sql_update = "UPDATE tabela_cadastro SET NOME = ? WHERE id_pessoa = ?"
        cursor.execute(sql_update, (nome, cpf))
        conexao.commit()
        conexao.close()
        return True
    except Exception as ex:
        print(ex)
        return False
        
        # for pessoa in pessoas:
        #     if pessoa['id_pessoa'] == id_pessoa:
        #         if request.method == 'POST':
        #             pessoa['nome'] = request.form['nome']
        #             pessoa['cpf'] = request.form['cpf']
        #             return redirect(url_for('index'))
        #         return render_template('editar.html', pessoa=pessoa)
        # return "Pessoa não encontrada."

# Rota para excluir uma pessoa
@app.route('/excluir/<id_pessoa>')
def excluir_pessoa(id_pessoa:int):
    try:
        conexao = sqlite3.connect('cadastros.db')
        cursor = conexao.cursor()
        sql_delete = "DELETE FROM tabela_cadastro WHERE id_pessoa = ? "
        cursor.execute(sql_delete, (id_pessoa, ))
        conexao.commit()
        conexao.close()
        return True
    except Exception as ex:
        print(ex)
        return False


    # for pessoa in pessoas:
    #     if pessoa['cpf'] == cpf:
    #         pessoas.remove(pessoa)
    #         return redirect(url_for('index'))
    # return "Pessoa não encontrada."

if __name__ == '__main__':
    app.run(debug=True)

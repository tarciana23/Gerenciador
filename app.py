from flask import Flask, render_template, request, jsonify,redirect
import json
import os

app = Flask(__name__)

# Obtenha o diretório base do aplicativo Flask
base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, 'verificarUsuarios.json')

# Função para verificar as credenciais do usuário
def verificar_credenciais(email, senha):
    with open(json_path, 'r') as file:
        usuarios = json.load(file)['usuarios']
        for usuario in usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                return True
        return False

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/logout', methods=['POST'])
def logout():
    # Implemente aqui a lógica para finalizar a sessão do usuário, se necessário
    # Por exemplo, você pode limpar os dados da sessão ou fazer outras tarefas de limpeza
    return jsonify({'message': 'Logout realizado com sucesso'})

"""
@app.route('/projeto_planilhas')
def projeto_planilhas():
    return render_template('/Gerenciador/projetoPlanilhas/index.html')

@app.route('/estado_nutricional')
def estado_nutricional():
    return render_template('/Gerenciador/estadonutricional/index.html')"""

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # Obter os dados do formulário
        login = request.form['email']
        senha = request.form['password']
        print(login,senha)
        # Verificar as credenciais do usuário
        if verificar_credenciais(login, senha):
            resultado_login = 'Login efetuado com sucesso'
        else:
            resultado_login = 'Credenciais inválidas' 
        print("Resultado do login: ",resultado_login)
        return jsonify({'resultado': resultado_login})

if __name__ == '__main__':
    app.run(debug=True)

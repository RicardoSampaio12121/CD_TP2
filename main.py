from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    with open("WebPages/index.html") as file:
        return file.read()


@app.route("/Register")
def register():
    with open("WebPages/register.html") as file:
        return file.read()


@app.route("/Register", methods=['POST'])
def get_register_data():
    firstname = request.form['text']
    lastname = request.form['text2']
    processed_text = f"Olá {firstname} {lastname}, bem vindo!"
    return processed_text


# @app.route("/Register/Save")
# def register_save():



if __name__ == '__main__':
    app.run(debug=True)

# TODO: Criar index
# TODO: Criar pagina de registo de utilizadores
# TODO: Criação de utilizadores
# TODO: Autenticação de utilizadores
# TODO: Criar caixa de mensagens por utilizador
# TODO: Enviar mensagem persistente a utilizador
# TODO: Criação de grupos
# TODO: Enviar mensagem persistente a grupo
# TODO: Notificar ao aparecimento de uma nova mensagem
# TODO: Listar número de mensagens na caixa de mensagens
# TODO: Remover mensagem da caixa de mensagens

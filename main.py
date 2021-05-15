from flask import Flask, session, make_response, render_template, redirect, url_for, request
from auth import auth

app = Flask(__name__)

app.register_blueprint(auth)


@app.route('/')
def index():
    user_id = request.cookies.get('user_id')
    if user_id:
        return render_template("index.html")
    else:

        mensagens_teste = [("Sent", "Ola"), ("Received", "Boas"), ("Received", "Está tudo?"), ("Sent", "Tá")]
        print(mensagens_teste)
        return render_template("messengerForm.html", teste=15, mensagens=mensagens_teste)
        # return redirect(url_for("auth.login"))


if __name__ == '__main__':
    app.secret_key = "2862"
    app.run(debug=True)

# TODO: Criar caixa de mensagens por utilizador
# TODO: Enviar mensagem persistente a utilizador
# TODO: Criação de grupos
# TODO: Enviar mensagem persistente a grupo
# TODO: Notificar ao aparecimento de uma nova mensagem
# TODO: Listar número de mensagens na caixa de mensagens
# TODO: Remover mensagem da caixa de mensagens

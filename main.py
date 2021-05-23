from flask import Flask, session, render_template, redirect, url_for
from auth import auth
from admin import admin
from messenger import messenger
from fts import fts

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(messenger)
app.register_blueprint(admin)
app.register_blueprint(fts)


@app.route('/')
def index():
    if session.get('user_id'):
        return render_template("index.html")
    else:
        return redirect(url_for("auth.login"))


if __name__ == '__main__':
    app.secret_key = "2862"
    app.run(debug=True)

# TODO: Criação de grupos
# TODO: Enviar mensagem persistente a grupo

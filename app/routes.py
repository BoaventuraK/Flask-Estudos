from app import app 
from flask import render_template

@app.route("/")
@app.route("/index/", defaults={"nome":"User", "idade":"sua idade"})
@app.route("/index/<nome>/<idade>")
def index(nome, idade):
    return render_template('index.html', nome=nome, idade=idade)

@app.route("/contato")
def contato():
    return render_template('contato.html')
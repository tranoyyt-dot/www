from flask import (Blueprint, render_template, session, abort)

sistema = Blueprint("sistema", __name__)

@sistema.route("/home")
def home():
    return render_template("home.html")

@sistema.route("/produtos")
def produtos():
    if session["usuario"]["permissao"] == "produtos":
        return render_template("produto.html")
    else:
        abort(403)


sistema = Blueprint("sistema", __name__)

@sistema.route("/home")
def home():
    return render_template("home.html")

@sistema.route("/relatorios")
def produtos():
    if session["usuario"]["permissao"] == "relatorios":
        return render_template("relatorio.html")
    else:
        abort(403)
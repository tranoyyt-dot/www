from flask import request, render_template
from models.aluno import Aluno
def formulario():
    return render_template("formulario.html")

def cadastrar():
    nome = request.form["nome"]
    idade = request.form["idade"]
    aluno = Aluno(nome, idade)
    aluno.salvar()
    return render_template(
        "sucesso.html",
        nome=nome
    )


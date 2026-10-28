from flask import request, render_template, render_template_string
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

def lista():
    alunos = Aluno.lista()
    return render_template(
        "lista.html", alunos=alunos
        )
def apagar():
   id_aluno =  request.args["id"]
   Aluno.apagar(id_aluno)
   return render_template_string("<h1>Excluído</h1>")

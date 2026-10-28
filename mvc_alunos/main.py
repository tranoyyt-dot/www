from flask import Flask 
from controllers.aluno_controller import formulario
from controllers.aluno_controller import cadastrar
from controllers.aluno_controller import lista
from controllers.aluno_controller import apagar


app = Flask(__name__)

@app.route("/")
def inicio():
    return  formulario()
@app.route("/aluno", methods=["POST"])
def salvar_aluno():
    return cadastrar()
@app.route("/alunos", methods=["GET"])
def lista_alunos():
    return lista()
@app.route("/excluir")
def excluir_aluno():
    return apagar()



app.run(debug=True)
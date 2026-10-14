from flask import Flask 
from controllers.aluno_controller import formulario
from controllers.aluno_controller import cadastrar


app = Flask(__name__)

@app.route("/")
def inicio():
    return  formulario()
@app.route("/aluno", methods=["POST"])
def salvar_aluno():
    return cadastrar()

app.run(debug=True)
from mvc_alunos.models.model import Aluno
import mvc_alunos.views.view as view

class AlunoController:
    def cadastrar(self):
        nome = view.pedir_nome()
        idade = view.pedir_idade()
        aluno = Aluno(nome, idade)
        aluno.matricular_aluno() 
        view.mostrar_aluno(aluno)
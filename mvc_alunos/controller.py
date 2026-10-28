from mvc_alunos.models.aluno import Aluno
import view

class AlunoController:
    def cadastrar(self):
        nome = view.pedir_nome()
        idade = view.pedir_idade()
        aluno = Aluno(nome, idade)
        aluno.matricular_aluno() 
        view.mostrar_aluno(aluno)

    
        
        
from database import conectar
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.matriculado = False
        self.maior = False

    def matricular_aluno(self):
        if (self.maior):
            self.matriculado = True


    def verificar_maioridade(self):
        if self.idade >= 18:
            return "Maior de Idade"
        else:
            return "Menor de Idade"

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """INSERT INTO aluno (nome, idade) VALUES (%s, %s)"""
        valores = (self.nome, self.idade)        
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def lista():
        conexao = conectar()
        cursor = conexao.cursor()       
        cursor.execute("SELECT * FROM aluno")
        lista_alunos = cursor.fetchall()
        cursor.close()
        conexao.close()
        return lista_alunos

    def apagar():
        conexao = conectar()
        cursor= conexao.cursor()
        cursor.execute("DELETE  FROM aluno WHERE id = %s", (id,))
        deletar_alunos = cursor.fetchall()
        cursor.close()
        conexao.close()
        return deletar_alunos
class Aluno:
    def _init_(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

Aluno1 = Aluno("Carlos", 8.5, 7.2)
MediaAluno1 = Aluno1.calcular_media()
print(f"A média do aluno {Aluno1.nome} é: {MediaAluno1:.2f}")
from dataclasses import dataclass
@dataclass
class RegShopping:
    idade: int
    frequencia: int
    Nota: list
    Media: float

Aluno = [None]*3
for i in range(4):
    Aluno[i] = RegEstudante('','',[0.0,0.0,0.0,0.0,],0.0)
for i in range(4):
    Aluno[i].Nome = input("Digite o nome: ")
for j in range(3):
    Aluno[i].Nota[j] = float(input(f"Nota{j+1}:"))
    Aluno[i].Media = Aluno[i].Media + Aluno[i].Nota[j]*(j+1)/10
print(f"{Aluno[i].Nome} tem média = {Aluno[i].Media}")
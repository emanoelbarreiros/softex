# quantos foram aprovados em cada turma
# maior nota de cada turma
# aluno com a maior nota geral

turmas = ["A", "B", "C", "D"]
maioresNotas = {"A": 0, "B": 0, "C": 0, "D": 0}
alunosMaioresNotas = {"A": "", "B": "", "C": "", "D": ""}
aprovadosPorTurma = {"A": 0, "B": 0, "C": 0, "D": 0}
for turma in turmas:
    print(f"Turma {turma}:")
    for n in range(25):
        nome = input('Informe o nome: ')
        nota = float(input("Informe a nota: "))
        maiorNotaAtual = maioresNotas[turma]

        if nota > maiorNotaAtual:
            maioresNotas[turma] = nota
            alunosMaioresNotas[turma] = nome

        if nota >= 7:
            aprovadosPorTurma[turma] += 1

# nome do aluno com a maior nota e de que turma ele é
# a maior nota de todas
maiorNotaGeral = 0
turmaMaiorNotaGeral = 0
alunoMaiorNota = ""
for turma,nota in maioresNotas.items():
    if nota > maiorNotaGeral:
        maiorNotaGeral = nota
        turmaMaiorNotaGeral = turma

alunoMaiorNota = alunosMaioresNotas[turmaMaiorNotaGeral]

for turma,aprovados in aprovadosPorTurma.items():
    print(f"Aprovados na Turma {turma}: {aprovados}")
    print(f"Maior nota da turma {turma}: {maioresNotas[turma]}")

print(f"Aluno com a maior nota: {alunoMaiorNota}")

print(f"Maior nota geral: {maiorNotaGeral}")
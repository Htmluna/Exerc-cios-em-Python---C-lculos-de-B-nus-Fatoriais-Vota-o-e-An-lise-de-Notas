# Inicializar listas para armazenar as notas dos alunos ímpares e pares
notas_impares = []
notas_pares = []

# Solicitar as notas dos alunos ímpares
print("Você está digitando as notas dos 25 primeiros alunos ímpares.")
for i in range(1, 50, 2):
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
    notas_impares.append(nota)

# Solicitar as notas dos alunos pares
print("Agora você está digitando as notas dos 25 primeiros alunos pares.")
for i in range(2, 51, 2):
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
    notas_pares.append(nota)

# Calcular as médias
media_impares = sum(notas_impares) / len(notas_impares)
media_pares = sum(notas_pares) / len(notas_pares)

# Determinar qual metade teve a maior nota
if media_impares > media_pares:
    print("A metade dos alunos ímpares teve a maior média.")
elif media_pares > media_impares:
    print("A metade dos alunos pares teve a maior média.")
else:
    print("As duas metades tiveram médias iguais.")

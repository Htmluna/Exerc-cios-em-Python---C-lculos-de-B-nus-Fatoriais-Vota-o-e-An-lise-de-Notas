# Solicitar os minutos atuais
minutos = int(input("Digite os minutos atuais: "))

# Calcular o fatorial
fatorial = 1
for i in range(1, minutos + 1):
    fatorial *= i

# Construir a senha
senha = "LIBERDADE" + str(fatorial)

# Exibir a senha
print("A senha necessária para desbloqueio é:", senha)

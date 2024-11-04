# Solicitar informações do usuário
assinatura = input("Digite o tipo de assinatura (Basic/Silver/Gold/Platinum): ")
faturamento_anual = float(input("Digite o faturamento anual do cliente: "))

# Calcular o bônus com base no tipo de assinatura
if assinatura == "Basic":
    porcentagem = 0.30
elif assinatura == "Silver":
    porcentagem = 0.20
elif assinatura == "Gold":
    porcentagem = 0.10
elif assinatura == "Platinum":
    porcentagem = 0.05
else:
    print("Tipo de assinatura inválido.")
    porcentagem = 0

# Calcular e exibir o valor do bônus
bonus = faturamento_anual * porcentagem
print(f"O valor do bônus a ser pago é: R${bonus:.2f}")

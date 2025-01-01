# Saldo Inicial
saldo = 0.0

# Depositos e Saques
depositos = []
saques = []

# Limitaçoes de saques
LIMITE_SAQUES_DIARIOS = 3
saques_realizados = 0

# Funçao de saque
def realizar_saque(valor):
    global saldo, saques_realizados

    if saques_realizados >= LIMITE_SAQUES_DIARIOS:
        print("Limite de saque diário atingido. Você só pode realizar 3 saques por dia.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque")
    elif valor > 500:
        print("O valor do saque não pode ultrapassar R$ 500")
    else:
        saldo -= valor
        saques.append(valor) # Armazenando o saque
        saques_realizados += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

# Funçao de deposito
def realizar_deposito(valor):
    global saldo

    if valor <= 0:
        print("O valor do deposito dever ser maior que zero")
    else:
        saldo += valor 
        depositos.append(valor)
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")

# Funçao de Extrato
def exibir_extrato():
    print(f"\n Seu saldo atual é: R${saldo:.2f}")
    print("\n Depositos realizados:")
    for deposito in depositos:
        print(f"\nR${deposito:.2f}")
    print("\n Saques realizados:")
    for saque in saques:
        print(f"R${saque:.2f}")
    
# Funçao principal
def menu():
    global saldo, saques_realizados
    
    while True:
        print("""
              Selecione uma opção:
              --------------------
              [1] Saque
              [2] Deposito
              [3] Extrato
              [0] Sair
              """
            )
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            valor_saque = input("Digite o valor do Saque: R$")
            if not valor_saque.replace('.', '', 1).isdigit():  # Verifica se é um número válido
                print("Valor inválido! Tente novamente.")
                continue
            realizar_saque(float(valor_saque))
        elif opcao == 2:
            valor_deposito = input("Digite o valor do deposito: R$")
            if not valor_deposito.replace('.', '', 1).isdigit():  # Verifica se é um número válido
                print("Valor inválido! Tente novamente.")
                continue
            realizar_deposito(float(valor_deposito))
        elif opcao == 3:
            exibir_extrato()
        elif opcao == 0:
            print("Saindo... Obrigado por usar nosso sistema!")
            break
        else:
            print("Opção invalida! Tente novamente")

menu()
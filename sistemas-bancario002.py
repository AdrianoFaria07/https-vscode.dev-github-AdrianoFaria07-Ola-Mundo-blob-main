def menu():
    print("\n===== MENU =====")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")
    return input("Escolha uma opção: ")

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("✅ Depósito realizado com sucesso.")
    else:
        print("❌ Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, extrato, limite, saques_realizados, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    if saques_realizados >= limite_saques:
        print("❌ Limite de saques diários atingido.")
    elif valor > limite:
        print("❌ Valor do saque excede o limite por operação.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        saques_realizados += 1
        print("✅ Saque realizado com sucesso.")
    else:
        print("❌ Valor inválido para saque.")
    return saldo, extrato, saques_realizados

def exibir_extrato(saldo, extrato):
    print("\n📄 EXTRATO")
    if not extrato:
        print("Nenhuma movimentação.")
    else:
        for item in extrato:
            print(item)
    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")

def sistema_bancario():
    saldo = 0
    extrato = []
    limite = 500
    saques_realizados = 0
    limite_saques = 3

    while True:
        opcao = menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, saques_realizados = sacar(
                saldo, extrato, limite, saques_realizados, limite_saques
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "0":
            print("👋 Saindo do sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Executar o sistema
sistema_bancario()

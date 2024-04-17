menu = """
Bem vindo(a) ao app bank! O que deseja fazer?

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 0
extrato = """"""
saques_realizados = 0
LIMITE_SAQUES = 3

def depositar(saldo, extrato):
    valor_deposito = float(input("Insira o valor a ser depositado: "))
    if (valor_deposito <= 0):
        print("Esse valor não é válido.")
        valor_deposito = 0
        return saldo, extrato
    saldo += valor_deposito
    extrato += f"""
Deposito realizado no valor de R${valor_deposito:.2f},""" 
    return saldo, extrato

def sacar(saldo, extrato):
    global saques_realizados
    valor_saque = float(input("Insira o valor que deseja sacar: "))
    if (valor_saque <= 0 or valor_saque >= 500):
        print("Valor de saque maior que o limite permitido ou inválido.")
        valor_saque = 0
        return saldo, extrato
    if (valor_saque > saldo):
        print("Saldo insuficiente na conta")
        return saldo, extrato
    saldo -= valor_saque
    extrato += f"""
Saque realizado no valor de R${valor_saque:.2f},"""
    saques_realizados += 1
    return saldo, extrato

while True:
    opcao = input(menu)
    match opcao:
        case "d":
            saldo, extrato = depositar(saldo, extrato)
        case "s":
            saques_realizados
            if (saques_realizados == LIMITE_SAQUES):
                print("Você já atingiu o limite de saque diário")
                continue
            saldo, extrato = sacar(saldo, extrato)
        case "e":
            print(extrato)
        case "q":
            break
        case _:
            print("Opcao inválida.")
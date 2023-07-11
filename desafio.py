import os
import time as t


def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')


saldo = 0

qtd_saque = 0
qtd_deposito = 0
LIMITE_SAQUE = 500
LIMITE_SAQUE_DIARIO = 3

menu = """  
===BANCO===
[0] Sacar
[1] Depósito
[2] Extrato
[3] Sair
"""

while True:
    # print(menu)

    opcao = int(input(menu))

    if opcao == 0:
        print(f"Quanto deseja sacar? (Saldo: R${saldo:.2f})")
        saque = float(input("R$ "))
        if saque > LIMITE_SAQUE:
            print("Você não pode sacar mais que R$ 500.00")
            print("aguarde...")
            t.sleep(2)
        elif saque > saldo:
            print(f"Saldo insuficiente. (Saldo atual: {saldo: .2f})")
            print("Aguarde..")
            t.sleep(2)
        elif LIMITE_SAQUE_DIARIO == 0:
            print("Você atingiu o limite de saques diários!")
            print("aguarde...")
            t.sleep(2)
        elif saque < 0:
            print("Você não pode depositar um valor negativo.")
        else:
            print(f"Você sacou: R${saque: .2f}")
            LIMITE_SAQUE_DIARIO -= 1
            qtd_saque += 1
            saldo -= saque
            print("aguarde...")
            t.sleep(2)
    elif opcao == 1:
        print("Quanto deseja depositar?")
        depositou = float(input("R$ "))
        if depositou < 0:
            print("Você não pode depositar um valor negativo")
            print("Aguarde..")
            t.sleep(2)
        else:
            print(f"Você depositou: R${depositou: .2f}")
            saldo += depositou
            qtd_deposito += 1
            print("Aguarde...")
            t.sleep(2)
    elif opcao == 2:
        print(f"""
===Extrato===
Quantidade de saques restante = {LIMITE_SAQUE_DIARIO}
Saques realizador = {qtd_saque}
Depósitos realizados = {qtd_deposito}

saldo = {saldo}
=================
        """)
        t.sleep(5)
    elif opcao == 3:
        break
    else:
        print("Opção inválida")
        t.sleep(1.5)

    limpar_console()

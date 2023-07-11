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
    #print(menu)
    
    opcao = int(input(menu))

    if opcao == 0:
        print("Quanto deseja sacar?")
        saque = int(input())
        print(f"Você sacou: {saque}")
        LIMITE_SAQUE_DIARIO -= 1
        t.sleep(3)


        print(LIMITE_SAQUE_DIARIO)
    elif opcao == 1:
        print("Quanto deseja depositar?")
    
    
    limpar_console()
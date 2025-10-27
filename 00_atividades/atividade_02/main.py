# importação das bibliotecas
import os
import time

try:
    n = int(input("Informe um Número Inteiro: ").strip())
    while n >= 0:

        # Limpa a tela
        os.system("cls")
        print(n)
        time.sleep(1)
        n -= 1
        print("BOOOMMM!!!!")

        # mensagen
except:
    print("Erro.")
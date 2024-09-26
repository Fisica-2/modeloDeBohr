from math import *
from decimal import Decimal, getcontext

#Velocidade da luz no vacuo
c = Decimal(3E8)

#Massa do eletron
me = Decimal(9.11E-31)

#Constante magnetica
𝜇0 = Decimal((4*pi)*10**-7)

#Constante de Planck em J x s
hJ = Decimal(6.626E-34)

#Constante de Planck em Ev

hEv = Decimal(4.136E-15)

Pi = Decimal(str(2*pi))



def main():
    print("""
     ______________________________________________
    | Artur Chaves Paiva       - RA: 22.223.023-7  |
    | Giovanni Antonio Moreira - RA: 22.223.010-4  |
    | Leonardo Souza de Castro - RA: 22.123.114-5  |
    |______________________________________________|                                       

Esse programa tem o intuito de calcular algumas propriedades de ondas e campos eletromagnéticos, e usa de diversas fórmulas para um cálculo preciso e eficiente. O programa aceita
como entrada números em notação cíentifica, usando a notação 1.23E2 (1.23²). Além disso, estamos utilizando a biblioteca decimal para maior precisão nas respostas e operações. 
""")
    while True:
        entrada = int(input("""
Informe sua entrada:
    [1] Em -> Bm, I
    [2] Bm -> Em, I
    [3] I  -> Em, Bm
--------------------------
    [4] f -> λ, k, w
    [5] λ -> f, k, w
    [6] w -> f, λ, k
    [7] k -> f, λ, w
--------------------------
    """))
        match entrada:
            case(1):
                em = input("Em: ")
                
            case(2):
                bm = input("Bm: ")
                
            case(3):
                i = input("i: ")
                
            case(4):
                f = input("f: ")
                
            case(5):
                l = input("λ: ")
                
            case(6):
                w = input("w: ")
                
            case(7):
                k = input("k: ")
                
                
#Entradas -------------------------


main()
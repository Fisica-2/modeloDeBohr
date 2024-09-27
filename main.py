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

conversaoJouleParaEv = Decimal(1.60218e-19) # ev pra joule multiplica, o contrario divide

# Formulas # 
'''
# Energia do atomo de hidrogênio no modelo de Bohr = -13.6/nivel**2
# Energia Foton = constPlanck * frequencia = (constPlanck * velocidadeLuz) / comprimento de onda = EnergiaFinal - EnergiaInicial



'''





def main():
    energiaFoton = 0.0 
    comp = 0.0 
    freq = 0.0
    print("""
     ______________________________________________
    | Artur Chaves Paiva       - RA: 22.223.023-7  |
    | Giovanni Antonio Moreira - RA: 22.223.010-4  |
    | Leonardo Souza de Castro - RA: 22.123.114-5  |
    |______________________________________________|                                       

""")
    while True:
        entrada = int(input(f"""
Informe sua entrada:
    [1] Energia do Fóton ({energiaFoton:.3} J)
    [2] Comprimento de onda do Fóton ({comp:.3} m)
    [3] Frequencia do Fóton ({freq:.3} Hz)
    [4] 
    [5] 
    [6] 
    [7] 
--------------------------
    """))
        match entrada:
            case(1):
                nInicial = int(input("Nivel inicial: "))
                nFinal = int(input("Nivel final: "))
                energiaFoton = calculoEnergiaFoton(nInicial, nFinal)
                
            case(2):
                energiaFoton = Decimal(input("Digite a energia do Fóton absorvido (em joules): "))
                comp = calculoComprimentoOnda(energiaFoton)
                
            case(3):
                energiaFoton = Decimal(input("Digite a energia do Fóton absorvido (em joules): "))
                freq = calculoFrequencia(energiaFoton)
                
            case(4):
                input()
                
            case(5):
                input()
                
            case(6):
                input()
                
            case(7):
                input()
                
                
#Entradas -------------------------



def calculoEnergiaFoton(nInicial, nFinal): # Calculo da energia do foton absorvido por meio de eFinal - eInicial
    energia = Decimal((-13.6/pow(nFinal, 2)) - (-13.6/pow(nInicial, 2)))
    energiaEmJ = Decimal(energia * conversaoJouleParaEv) # conversão de eV para joules
    print(f"Energia do foton: {energiaEmJ:.3e} J")
    return energiaEmJ


def calculoComprimentoOnda(energiaFoton): # Calculo do comprimento de onda por meio da formula: planck(j) * velocidLuz / energiaFoton
    comprimento = Decimal( (hJ * c) / energiaFoton )
    print(f"Comprimento de onda: {comprimento:.3e} m")
    return comprimento


def calculoFrequencia(energiaFoton):
    freq = Decimal(energiaFoton / hJ)
    print(f"Frequência: {freq:.3e} Hz")
    return freq

main()
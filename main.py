from math import *
from decimal import Decimal, getcontext
import sys

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
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Informe o que deseja calcular:

    [1] Energia do Fóton ({energiaFoton:.3} J)
        Comprimento de onda do Fóton ({comp:.3} m)
        Frequência de onda do Fóton ({freq:.3} Hz)
        
    [2] 
    [3] 
    [4] Conversor Joule/eV
    [5] Sair 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """))
        match entrada:
            case(1):
                nInicial = int(input("Nivel inicial: "))
                nFinal = int(input("Nivel final: "))
                energiaFoton = calculoEnergiaFoton(nInicial, nFinal)
                comp = calculoComprimentoOnda(energiaFoton)
                freq = calculoFrequencia(energiaFoton)
                confirma()
                
            case(2):
                input();
                
            case(3):
                input();
                
            case(4):
                conversorJoulesEV()
                confirma()
                
            case(5):
                break
                
                
                
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

def conversorJoulesEV():
    opc = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Informe a entrada:

    [1] Converter Joules em eVs.
    [2] Converter eVs em Joules.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """)
    if(opc == "1"):
        valor = Decimal(input("Digite o valor em Joules: "))
        valor *= conversaoJouleParaEv
        print(f"Resultado: {valor:.3e} eVs")
    elif(opc == "2"):
        valor = Decimal(input("Digite o valor em eV: "))
        valor /= conversaoJouleParaEv
        print(f"Resultado: {valor:.3e} Joules")
    else:
        print("Opção inválida, tente novamente!")
        
        
def confirma():
    while(True):
        print("")
        conf = input("Deseja continuar? (s/n): ")
        if(conf == "s"):
            break
        elif(conf == "n"):
            print("Saindo do programa...")
            sys.exit()
        else:
            print("Opção inválida, lembre-se de usar apenas 's/n'")
        
    

main()
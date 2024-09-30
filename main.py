from math import *
from decimal import Decimal, getcontext
import sys

#Velocidade da luz no vacuo
c = Decimal(3E8)

#Permitividade elétrica
pe = Decimal(8.85e-12)

#Carga elétrica do elétron
ce = Decimal(1.602e-19)

#Massa do eletron
me = Decimal(9.11E-31)

#Constante magnetica
𝜇0 = Decimal((4*pi)*10**-7)

#Constante de Planck em J x s
hJ = Decimal(6.626E-34)

#Constante de Planck em Ev

hEv = Decimal(4.136E-15)

Pi = Decimal(pi)

#Constante de Rydberg 
R = Decimal(1.097e7)

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

    [1] Energia do Fóton ({energiaFoton:.2} J)
        Comprimento de onda do Fóton ({comp:.2} m)
        Frequência de onda do Fóton ({freq:.2} Hz)
        
    [2] Digite um valor para n:
    [3] Nível final ou Inicial
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
                n = int(input("Digite o valor do nível: "))
                raio = raioAtomo(n)
                velocidade = velocidadeAtomo(n)
                k = energiaCineticaEletron(velocidade, n)
                u = energiaPotencialEletron(n)
                e = energiaTotalElétron(n)
                λ = comprimentoDeOnda(velocidade)
                confirma()
                
            case(3):
                calcN()
                
            case(4):
                conversorJoulesEV()
                confirma()
                
            case(5):
                break
                
                
                
#Entradas -------------------------



def calculoEnergiaFoton(nInicial, nFinal): # Calculo da energia do foton absorvido por meio de eFinal - eInicial
    energia = Decimal((-13.6/pow(nFinal, 2)) - (-13.6/pow(nInicial, 2)))
    energiaEmJ = Decimal(energia * conversaoJouleParaEv) # conversão de eV para joules
    print(f"Energia do foton: {energiaEmJ:.2e} J")
    return energiaEmJ


def calculoComprimentoOnda(energiaFoton): # Calculo do comprimento de onda por meio da formula: planck(j) * velocidLuz / energiaFoton
    comprimento = Decimal( (hJ * c) / energiaFoton )
    print(f"Comprimento de onda: {comprimento:.2e} m")
    return comprimento


def calculoFrequencia(energiaFoton):
    freq = Decimal(energiaFoton / hJ)
    print(f"Frequência: {freq:.2e} Hz")
    return freq

def raioAtomo(n):
    raio = Decimal((hJ**2) / (Pi * me * (ce**2)) * pe)
    raioatomo = raio * Decimal(n**2)
    print(f"Raio do átomo: {raioatomo:.2e} m")
    return raioatomo

def velocidadeAtomo(n):
    velocidade = Decimal(1/pe)*((ce**2)/(2*n*hJ))
    print(f"Velocidade do elétron: {velocidade:.2e} m/s")
    return velocidade

def energiaCineticaEletron(velocidade, n):
    K = (hEv * c * R) / n**2
    print(f"Energia Cinética do Elétron: {K:.2e} eV")
    return K

def energiaPotencialEletron(n):
    U = (-(hEv*c*R) * 2) / n**2
    print(f"Energia Potencial do Elétron: {U:.2e} eV")

def energiaTotalElétron(n):
    E = Decimal(-(hEv*c*R)/(n**2))
    print (f"Energia total do eletron {E:.2e} eV")
    return E

def comprimentoDeOnda(velocidade):
    λ = Decimal(hJ / (me * velocidade))
    print(f"Comprimento de onda: {λ:.2e} m")

def calcN():
    opcao = int(input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Informe os valores de entrada:
                              
[1] - Nível inicial e Frêquencia do fóton 
[2] - Nível inicial e Comprimento de onda do fóton
[3] - Nível final e Frêquencia do fóton 
[4] - Nível final e Comprimento de onda do fóton 

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

"""))
                
    match opcao:
        case(1):
            nInicial = int(input("Nível inicial: "))
            f = int(input("Frequência (Hz): "))
        case(2):
            nInicial = Decimal(input("Nível inicial: "))
            λ = Decimal(input("Comprimento de onda (nm): "))
            print(Decimal((R / (nInicial**2)) - (R * λ)))
        case(3):
            nFinal = int(input("Nível Final: "))
            f = int(input("Frequência (Hz): "))
        case(4):
            nFinal = int(input("Nível Final: "))
            λ = Decimal(input("Comprimento de onda (nm): "))
            print(Decimal(( (R * λ)) - (R / (nFinal ** 2))))


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
        print(f"Resultado: {valor:.2e} eVs")
    elif(opc == "2"):
        valor = Decimal(input("Digite o valor em eV: "))
        valor /= conversaoJouleParaEv
        print(f"Resultado: {valor:.2e} Joules")
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
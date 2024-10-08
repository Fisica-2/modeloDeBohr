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
Ondas de Rádio: Menor que 
# 1. Ondas de Rádio: Menor que 3 * 10e9 Hz
# 2. Micro-ondas: 3 * 10^9 Hz a 3 * 10e11 Hz
# 3. Infravermelho: 3 * 10^11 Hz a 4 * 10e14 Hz
# 4. Luz Visível: 4 * 10^14 Hz a 7.5 * 10e14 Hz
    # 1. Vermelho: 4.0 × 10^14 Hz
    # 2. Laranja: 4.8 × 10^14 Hz
    # 3. Amarelo: 5.1 × 10^14 Hz
    # 4. Verde: 5.5 × 10^14 Hz
    # 5. Azul: 6.3 × 10^14 Hz
    # 6. Violeta: 7.5 × 10^14 Hz
# 5. Ultravioleta: 7.5 * 10^14 Hz a 3 * 10e16 Hz
# 6. Raios-X: 3 * 10^16 Hz a 3 * 10e19 Hz
# 7. Raios Gama: Maior que 3 * 10e19 Hz


'''

def main():
    
    print("""
     ______________________________________________
    | Artur Chaves Paiva       - RA: 22.223.023-7  |
    | Giovanni Antonio Moreira - RA: 22.223.010-4  |
    | Leonardo Souza de Castro - RA: 22.123.114-5  |
    |______________________________________________|


O código implementa um simulador baseado no modelo de Bohr, que descreve
o comportamento de elétrons em átomos, especialmente no hidrogênio. 
As funções calculam propriedades como energia do fóton, comprimento de 
onda, frequência, raio do átomo e energia cinética do elétron, utilizando
constantes fundamentais da física.

As entradas incluem níveis quânticos, frequência ou comprimento de onda
de fótons, e permitem cálculos de transições entre estados energéticos.
As saídas apresentam resultados em unidades de energia (joules e eV), 
comprimento de onda e frequência. O modelo de Bohr, ao estabelecer que 
os elétrons orbitam em níveis discretos, explica a quantização da energia
e a emissão ou absorção de fótons durante as transições entre esses níveis.
          
""")
    while True:
        entrada = int(input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Informe a entrada:

    [1] Digite um valor para n.                     
    [2] Digite n inicial e n final.                 
    [3] Digite nível Final ou Inicial para absorção.   
    [4] Digite nível Final ou Inicial para emissão.                            
    [5] Digite F(Hz), λ(m) ou E(J ou eV).                             
    [6] Conversor Joule/eV   
    [7] Sair 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    """))
        match entrada:
            case(1):
                n = int(input("Digite o valor do nível: "))
                raio = raioAtomo(n)
                velocidade = velocidadeAtomo(n)
                k = energiaCineticaEletron(velocidade, n)
                u = energiaPotencialEletron(n)
                e = energiaTotalElétron(n)
                λ = comprimentoDeOnda(velocidade)
                confirma()
                
            case(2):
                nInicial = int(input("Nivel inicial: "))
                nFinal = int(input("Nivel final: "))
                energiaFoton = calculoEnergiaFoton(nInicial, nFinal)
                calculoComprimentoOnda(energiaFoton)
                calculoFrequencia(energiaFoton)
                confirma()
                
                
            case(3):
                absorcaoCalcN()
                confirma()
                
            case(4):
                transicaoCalcN()
                confirma()
                
            case(5):
                calculoEnergiaFreqCompr()
                confirma()
            case(6):
                conversorJoulesEV()
                confirma()               
                
                
                
#Entradas -------------------------



def calculoEnergiaFoton(nInicial, nFinal): # Calculo da energia do foton absorvido por meio de eFinal - eInicial
    energia = Decimal((-13.6/pow(nFinal, 2)) - (-13.6/pow(nInicial, 2)))
    energiaEmJ = Decimal(energia * conversaoJouleParaEv) # conversão de eV para joules
    if(energiaEmJ < 0):
        energia *= -1
        energiaEmJ *= -1
    print(f"Energia do foton: {energiaEmJ:.2e} J ou {energia:.2e} eV")
    return energiaEmJ

def calculoComprimentoOnda(energiaFoton): # Calculo do comprimento de onda por meio da formula: planck(j) * velocidLuz / energiaFoton
    comprimento = Decimal( (hJ * c) / energiaFoton )
    print(f"Comprimento de onda: {comprimento:.2e} m")


def calculoFrequencia(energiaFoton):
    freq = Decimal(energiaFoton / hJ)
    print(f"Frequência: {freq:.2e} Hz")

def raioAtomo(n):
    raio = Decimal((hJ**2) / (Pi * me * (ce**2)) * pe)
    raioatomo = raio * Decimal(n**2)
    print(f"Raio do átomo: {raioatomo:.2e} m")
    return raio

def velocidadeAtomo(n):
    velocidade = Decimal(1/pe)*((ce**2)/(2*n*hJ))
    print(f"Velocidade do elétron: {velocidade:.2e} m/s")
    return velocidade

def energiaCineticaEletron(velocidade, n):
    K = (hEv * c * R) / n**2
    print(f"Energia Cinética do Elétron: {K:.2e} eV")

def energiaPotencialEletron(n):
    U = (-(hEv*c*R) * 2) / n**2
    print(f"Energia Potencial do Elétron: {U:.2e} eV")

def energiaTotalElétron(n):
    E = Decimal(-(hEv*c*R)/(n**2))
    print (f"Energia total do eletron {E:.2e} eV")

def comprimentoDeOnda(velocidade):
    λ = Decimal(hJ / (me * velocidade))
    print(f"Comprimento de onda: {λ:.2e} m")

def absorcaoCalcN():
    opcao = int(input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
(Absorção de fótons)
Informe os valores de entrada:
                              
    [1] Nível inicial e Frequência do fóton 
    [2] Nível inicial e Comprimento de onda do fóton
    [3] Nível final e Frequência do fóton 
    [4] Nível final e Comprimento de onda do fóton 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    """))
                
    match opcao:
        case(1):
            nInicial = int(input("Nível inicial: "))
            f = Decimal(input("Frequência (Hz): "))
            energiaInicial = Decimal(-13.6/(nInicial**2))
            energiaAbsorvida = Decimal(hEv*f)
            energiaFinal = energiaInicial + energiaAbsorvida
            nFinal = Decimal(13.6)/energiaFinal
            if(nFinal < 0):
                nFinal *= -1
            
            nFinal = sqrt(nFinal)
        
            print(f"Nível final: {nFinal:.0f}")


        case(2):
            nInicial = Decimal(input("Nível inicial: "))
            λ = Decimal(input("Comprimento de onda (m): "))
            energia = (hEv*c)/λ
            energiaNivel = -(Decimal(13.6)/(nInicial**2))
            energiaFinal = energiaNivel+energia
            nFinalQuadrado = Decimal(13.6)/-energiaFinal

            if nFinalQuadrado < 0 :
                nFinalQuadrado = nFinalQuadrado*-1

            nFinal = sqrt(nFinalQuadrado)
            print(f"Nível Final: {nFinal:.0f}")   
                   
        case(3):
            nFinal = int(input("Nível Final: "))
            f = Decimal(input("Frequência (Hz): "))
            energiaFinal = Decimal(-13.6/(nFinal**2))
            energiaAbsorvida = Decimal(hEv*f)
            energiaInicial = energiaFinal - energiaAbsorvida
            nInicial = Decimal(13.6)/energiaInicial
            if(nInicial < 0):
                nInicial *= -1
            
            nInicial = sqrt(nInicial)
        
            print(f"Nível Inicial: {nInicial:.0f}")
            
        case(4):
            nFinal = int(input("Nível Final: "))
            λ = Decimal(input("Comprimento de onda (m): "))

            energiaAbsorvida = (hEv*c)/λ
            energiaFinal = -(Decimal(13.6)/(nFinal**2))
            energiaInicial = energiaFinal - energiaAbsorvida

            nInicial = Decimal(13.6)/energiaInicial
            if(nInicial < 0):
                nInicial *= -1

            nInicial = sqrt(nInicial)
            
            print(f"Nível Inicial: {nInicial:.0f}")

def transicaoCalcN():
    opcao = int(input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
(Emissão de fótons)
Informe os valores de entrada:
                              
    [1] Nível inicial e Frequência do fóton 
    [2] Nível inicial e Comprimento de onda do fóton
    [3] Nível final e Frequência do fóton 
    [4] Nível final e Comprimento de onda do fóton 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    """))
                
    match opcao:
        case(1):
            nFinal = int(input("Nível Inicial: "))
            f = Decimal(input("Frequência (Hz): "))
            energiaFinal = Decimal(-13.6/(nFinal**2))
            energiaAbsorvida = Decimal(hEv*f)
            energiaInicial = energiaFinal - energiaAbsorvida
            nInicial = Decimal(13.6)/energiaInicial
            if(nInicial < 0):
                nInicial *= -1
            
            nInicial = sqrt(nInicial)
        
            print(f"Nível Final: {nInicial:.0f}")

        case(2):
            nFinal = int(input("Nível Inicial: "))
            λ = Decimal(input("Comprimento de onda (m): "))

            energiaAbsorvida = (hEv*c)/λ
            energiaFinal = -(Decimal(13.6)/(nFinal**2))
            energiaInicial = energiaFinal - energiaAbsorvida

            nInicial = Decimal(13.6)/energiaInicial
            if(nInicial < 0):
                nInicial *= -1

            nInicial = sqrt(nInicial)
            
            print(f"Nível Final: {nInicial:.0f}")   
                   
        case(3):
            nInicial = int(input("Nível Final: "))
            f = Decimal(input("Frequência (Hz): "))
            energiaInicial = Decimal(-13.6/(nInicial**2))
            energiaAbsorvida = Decimal(hEv*f)
            energiaFinal = energiaInicial + energiaAbsorvida
            nFinal = Decimal(13.6)/energiaFinal
            if(nFinal < 0):
                nFinal *= -1
            
            nFinal = sqrt(nFinal)
        
            print(f"Nível Inicial: {nFinal:.0f}")
            
        case(4):
            nInicial = Decimal(input("Nível Final: "))
            λ = Decimal(input("Comprimento de onda (m): "))
            energia = (hEv*c)/λ
            energiaNivel = -(Decimal(13.6)/(nInicial**2))
            energiaFinal = energiaNivel+energia
            nFinalQuadrado = Decimal(13.6)/-energiaFinal

            if nFinalQuadrado < 0 :
                nFinalQuadrado = nFinalQuadrado*-1

            nFinal = sqrt(nFinalQuadrado)
            print(f"Nivel Inicial: {nFinal:.0f}")
            
def calculoEnergiaFreqCompr():
    opcao = int(input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Informe os valores de entrada:
                              
    [1] Frequência(Hz) -> Energia(J e eV).
    [2] λ(m) -> Energia(J e eV).
    [3] Energia(J ou eV) -> Frequência(Hz) e λ(m).
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    """))
                
    match opcao:
        case(1):
            f = Decimal(input("Frequência(Hz): "))
            energiaEmJ = hJ * f
            energiaEmEV = energiaEmJ / conversaoJouleParaEv
            print(f"Energia em Joules: {energiaEmJ:.2e} J")
            print(f"Energia em Elétron-Volts: {energiaEmEV:.2e} eV")
            
        case(2):
            λ = Decimal(input("Comprimento de onda(m): "))
            energiaEmJ = (hJ * c) / λ
            energiaEmEV = energiaEmJ / conversaoJouleParaEv
            print(f"Energia em Joules: {energiaEmJ:.2e} J")
            print(f"Energia em Elétron-Volts: {energiaEmEV:.2e} eV")
                   
        case(3):
            unidade = int(input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=                           
Informe a entrada: 
                               
    [1] Elétron-Volts.
    [2] Joules.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    """))
            match unidade:
                case(1):
                    energiaEmEV = Decimal(input("Energia(eV): "))
                    energiaJ = energiaEmEV * conversaoJouleParaEv
                    freq = energiaJ / hJ
                    λ = (hJ * c) / energiaJ
                    print(f"Frequência: {freq:.2e} Hz")
                    print(f"Comprimento de onda: {λ:.2e} m")
                
                case(2):
                    energiaJ = Decimal(input("Energia(J): "))
                    freq = energiaJ / hJ
                    λ = (hJ * c) / energiaJ
                    print(f"Frequência: {freq:.2e} Hz")
                    print(f"Comprimento de onda: {λ:.2e} m")
                
                case _:
                    print("Entrada inválida, tente novamente")
            
        case _:
            print("Entrada inválida, tente novamente!")

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
        valor /= conversaoJouleParaEv
        print(f"Resultado: {valor:.2e} eVs")
    elif(opc == "2"):
        valor = Decimal(input("Digite o valor em eVs: "))
        valor *= conversaoJouleParaEv
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
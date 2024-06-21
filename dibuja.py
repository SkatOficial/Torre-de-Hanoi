from time import sleep
import os 

def limpia_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def animacion_txt(texto,tiempo=0.05):
    for letra in texto:
        print(letra, end="")
        sleep(tiempo)
    print()

def Crea_disco(disc):
    if disc==0:
        return "|"
    else:
        return "-"*disc+"-"+"-"*disc

def Dibuja_torres(torres):

    #Busca disco mas grande
    disco_max=0
    for torre in torres:
        if max(torre)>disco_max:
            disco_max=max(torre)
    
    disco_max="-"*disco_max+"-"+"-"*disco_max#crea el disco mas grande primero para ocuaprlo de referencia en el center
   
    #imprimo las letras de las torres
    print(("[A]").center(len(disco_max)),end="      ")
    print(("[B]").center(len(disco_max)),end="      ")
    print(("[C]").center(len(disco_max)),end="\n\n")
    for fila in range(len(torres[0])):
        #Crea discos
        disco1=Crea_disco(torres[0][fila])
        disco2=Crea_disco(torres[1][fila]) 
        disco3=Crea_disco(torres[2][fila])
        #Dibuja Torre
        print((disco1).center(len(disco_max)),end="      ")
        print((disco2).center(len(disco_max)),end="      ")
        print((disco3).center(len(disco_max)))

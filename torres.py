from dibuja import *

def Crea_torres(nivel):
    torres=[[0],[0],[0]]
    for disco in range(1,nivel+2):
        torres[0].append(disco)
        torres[1].append(0)
        torres[2].append(0) 
    return torres

def Mueve_pieza(torres):
   
    disco_a_mover=""
    disco_destino=""
    torre_inicial=""
    torre_destino=""
    
    #-----------|INGRESA TORRE INICAL DONDE SE SACARA EL DISCO|-----------#
    while True:
        print("+===================================================+")
        Dibuja_torres(torres)
        print("+===================================================+")
        disco_a_mover=input("|Ingrese la pieza a mover: ").upper()
        limpia_consola()

        if(disco_a_mover!="A" and disco_a_mover!="B" and disco_a_mover!="C"):
            print("[ERROR][NO EXISTE ESA PIEZA]")
            continue
        elif(torres[ord(disco_a_mover)-ord("A")].count(0)==len(torres[0])):
            print("[ERROR][LA TORRE NO TIENE DISCOS PARA MOVER]")
            continue

        torre_inicial=ord(disco_a_mover)-ord("A")
        #-----------|BUSCA PRIMER DISCO EN LA TORRE|-----------#
        for disco in torres[torre_inicial]:
            if disco!=0:
                disco_a_mover=disco
                break
        break
    #-----------|INGRESA LA TORRE DONDE SE DEJARA EL DISCO ELEGIDO|-----------#
    limpia_consola()
    while True:
        disco_mayor=False
        print(f"[PIEZA A MOVER = {chr(torre_inicial+ord('A'))}]")
        print("+===================================================+")
        Dibuja_torres(torres)
        print("+===================================================+")
        disco_destino=input("|Ingrese donde movera la pieza: ").upper()
        limpia_consola()
        if(disco_destino!="A" and disco_destino!="B" and disco_destino!="C"):

            print("[ERROR][NO EXISTE ESA PIEZA]")
            continue
        torre_destino=ord(disco_destino)-ord("A")
        
        for disco in range(len(torres[torre_destino])-1):
            if torres[torre_destino][disco]==0 and torres[torre_destino][disco+1]!=0:
                disco_destino = disco #me guardo el indice para saber donde se movera la pieza
                if disco_a_mover > torres[torre_destino][disco_destino+1]:
                    disco_mayor=True
                    print("[ERROR][PIEZA A MOVER MAS GRANDE QUE PIEZA DESTINO]")                   
                break
            else:
                disco_destino=-1

        if disco_mayor==True:
            continue
        else:
            break    

    #-----------|MUEVE EL DISCO DE TORRE|-----------#
    if(torre_destino!=torre_inicial):#si mueve la pieza a la misma torre no se hacen cambios
        indice=torres[torre_inicial].index(disco_a_mover)
        torres[torre_inicial][indice]=0 #se saca el disco
        torres[torre_destino][disco_destino]=disco_a_mover 

def Evalua_juego(torres,forma_correcta):
    if torres[2]==forma_correcta:
        return True
    return False 


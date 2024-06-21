from dibuja import *
from torres import *

def Jugar(nivel):
    torres = Crea_torres(nivel)
    forma_correcta = torres[0].copy()
    while True:
        Mueve_pieza(torres)
        if(Evalua_juego(torres,forma_correcta) == True):
            print("+===================================================+")
            Dibuja_torres(torres)
            print("+===================================================+")
            animacion_txt("¡FELICIDADES! AVANZAS AL SIGUENTE NIVEL")
            animacion_txt("[PRESIONE CUALQUIER TECLA PARA CONTINUA]",0.01)
            input()
            limpia_consola()
            break

if __name__ == "__main__":
    limpia_consola()
    nivel=1
    while True:

        print(f"""               
            [NIVEL: {nivel}]
        +===============/Torre Hanoi\===============+    |
        |1.-JUGAR                                   |   ---
        |2.-SALIR                                   |  -----
        +===========================================+ -------
        """)
        opcion=input("|Eligue tu opcion :")
        limpia_consola()
        if(opcion=="1"):
            Jugar(nivel)
            nivel+=1
        elif(opcion=="2"):
            print("[SALIENDO...]")
            break
        else:
            print("[ERROR][OPCION INVALIDA]")
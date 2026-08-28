import time
from partido import PartidoEnVivo

partidos_activos= []
juego_1 = PartidoEnVivo("Chiefs", "Raiders", -250, 200)
juego_2 = PartidoEnVivo("cowboys", "eagles", -200, 150)
juego_3 = PartidoEnVivo("bills", "ravens", -105, 105)

partidos_activos.append(juego_1)
partidos_activos.append(juego_2)
partidos_activos.append(juego_3)


print("--- SISTEMA INICIADO: Lista de partidos creada ---")

while True:
    
    print("\n--- Buscando actualizaciones en vivo... ---")
    
    juego_1.actualizar_datos(0, 14, "Q2 05:00", 120, -150)
    juego_2.actualizar_datos(16, 7, "Q1 02:00", -150, 170)
    juego_3.actualizar_datos(7, 21, "Q2 06:57", 200, -250)
    

    for juego_actual in partidos_activos:
        detonada = juego_actual.verificar_alerta_valor()
    
        if detonada:
            print("alerta de valor encontrada")
            
    time.sleep(60)
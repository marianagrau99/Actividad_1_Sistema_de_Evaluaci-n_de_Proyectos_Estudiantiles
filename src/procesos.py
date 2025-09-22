import evaluaciones as e

def procesar_ronda(i, ronda, acumulado, mejores_equipos_ronda):
    """  
    Args:
        i (int): Número de ronda (índice).
        ronda (dict): Datos de evaluación de la ronda.
        acumulado (dict): Acumulado de datos por equipo.
        mejores_equipos_ronda (list): Lista donde se guarda el mejor equipo de cada ronda.
    """
    print(f"\nRonda {i+1}")
    
    # 1) Calcular puntajes por equipo
    puntajes = e.calcular_puntaje(ronda)

    # 2) Determinar mejor equipo de la ronda
    mer_equipo, mer_puntaje = e.obtener_mejor_equipo(puntajes)
    mejores_equipos_ronda.append((mer_equipo, mer_puntaje))

    # 3) Actualizar acumulado general
    e.actualizar_acumulado(acumulado, ronda, puntajes, mer_equipo)

    # 4) Mostrar mejor equipo
    print(f"Mejor Equipo de la Ronda: {mer_equipo} ({mer_puntaje} puntos)")

    # 5) Mostrar ranking actualizado
    print("Ranking Actualizado:")
    e.mostrar_tabla(acumulado)


def mostrar_resultados_finales(acumulado):
    """
    Args:
        acumulado (dict): Diccionario con los datos finales de todos los equipos.
    """
    
    # Equipo/s ganadores según puntaje total
    max_puntaje = max(d['puntos'] for d in acumulado.values())
    ganadores = [eq for eq, datos in acumulado.items() if datos['puntos'] == max_puntaje]
    
    print("\nResultados Finales")
    print(f"Equipos Ganadores: {', '.join(ganadores)} ({max_puntaje} puntos)")

    
    # tabla final ordenada por puntaje
    print("\nTabla Final de Resultados")
    e.mostrar_tabla(acumulado)


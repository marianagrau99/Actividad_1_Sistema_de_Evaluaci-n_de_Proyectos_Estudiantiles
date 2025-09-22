def calcular_puntaje(ronda):
    """
    Calcula el puntaje de cada equipo en una ronda según la fórmula:
    +3 * innovación + 1 * presentación - 1 si errores es True.
    
    Args:
        ronda (dict): Datos de los equipos en la ronda.
        
    Returns:
        dict: puntajes por equipo.
    """
    return {equipo: 3*datos['innovacion'] + 1*datos['presentacion'] - (1 if datos['errores'] else 0)
            for equipo, datos in ronda.items()}


def obtener_mejor_equipo(puntajes):
    """
    Encuentra el equipo con mayor puntaje en la ronda.
    
    Args:
        puntajes (dict): Puntajes por equipo.
        
    Returns:
        tuple: (nombre_equipo, puntaje)
    """
    mejor_equipo = max(puntajes, key=puntajes.get)
    return mejor_equipo, puntajes[mejor_equipo]


def actualizar_acumulado(acumulado, ronda, puntajes, mejor_equipo):
    """
    Actualiza el diccionario acumulado con la información de la ronda y puntajes.
    
    Args:
        acumulado (dict): Diccionario con datos acumulados por equipo.
        ronda (dict): Datos de la ronda actual.
        puntajes (dict): Puntajes calculados para la ronda.
        mejor_equipo (str): Equipo con mejor puntaje en la ronda.
    """
    for equipo, datos in ronda.items():
        if equipo not in acumulado:
            acumulado[equipo] = {
                'innovacion': 0,
                'presentacion': 0,
                'errores': 0,
                'mejores': 0,
                'puntos': 0
            }
        acumulado[equipo]['innovacion'] += datos['innovacion']
        acumulado[equipo]['presentacion'] += datos['presentacion']
        acumulado[equipo]['errores'] += 1 if datos['errores'] else 0
        acumulado[equipo]['puntos'] += puntajes[equipo]
    acumulado[mejor_equipo]['mejores'] += 1


def mostrar_tabla(acumulado):
    """
    Imprime la tabla ordenada de resultados.
    
    Args:
        acumulado (dict): Diccionario con datos acumulados por equipo.
    """
    print(f"{'Equipo':<10} {'Innovación':<10} {'Presentación':<13} {'Errores':<8} {'Mejores':<9} {'Puntos':<6}")
    
    # Ordenar equipos por puntos descendentes
    equipos_ordenados = sorted(acumulado.items(), key=lambda x: x[1]['puntos'], reverse=True)
    
    for equipo, datos in equipos_ordenados:
        print(f"{equipo:<10} {datos['innovacion']:<10} {datos['presentacion']:<13} {datos['errores']:<8} {datos['mejores']:<9} {datos['puntos']:<6}")

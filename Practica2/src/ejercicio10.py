def procesar_competencia(rounds):
    """
    Funcion para realizar la competencias de los chefs, en cada ronda mostrando
    el ganador y como acumulanm puntos
    """
    
    participantes = list(rounds[0]['scores'].keys())
    stats = {p: {'total': 0, 'wins': 0, 'mejor': 0, 'count': 0} for p in participantes}

    print("--- INICIO DE LA COMPETENCIA ---\n")
    
   
    for i, ronda in enumerate(rounds, 1):
        tema = ronda['theme']
        puntajes_ronda = {}
        

        for cocinero, jueces in ronda['scores'].items():
            
            puntos_actuales = sum(jueces.values())
            puntajes_ronda[cocinero] = puntos_actuales
            
            
            stats[cocinero]['total'] += puntos_actuales
            stats[cocinero]['count'] += 1

            if puntos_actuales > stats[cocinero]['mejor']:
                stats[cocinero]['mejor'] = puntos_actuales
                ganador_ronda = max(puntajes_ronda, key=puntajes_ronda.get)
        
        
        stats[ganador_ronda]['wins'] += 1
        
        print(f"Ronda {i} - {tema}:")
        print(f" Ganador: {ganador_ronda} ({puntajes_ronda[ganador_ronda]} pts)")

        
        ranking_progresivo = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True)
        
        print(f"{'Cocinero':<12} | {'Acumulado':<10}")
        print("-" * 25)

        for nombre, data in ranking_progresivo:
            print(f"{nombre:<12} | {data['total']:<10}")
        print("\n" + "."*30 + "\n")

    # Mostrar tabla de posiciones final
    print("=" * 65)
    print("TABLA DE POSICIONES FINAL".center(65))
    print("=" * 65)

    print(f"{'Cocinero':<10} {'Puntaje':<8} {'Rondas Ganadas':<12} {'Mejor Ronda':<8} {'Promedio':<8}")
    print("-" * 65)

    ranking_final = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True)

    for nombre, data in ranking_final:

        promedio = data['total'] / data['count']
        

        print(f"{nombre:<12} {data['total']:<12} {data['wins']:<12} {data['mejor']:<10} {promedio:<8.1f}")
    
    print("-" * 65)

 

def recorrer(rondas, ganadas) :
    numero = 1
    for ronda in rondas :
        total_Ronda = {"Valentina":0, "Mateo":0, "Camila":0, "Santiago":0, "Lucía":0}
        print(f"Ronda : {numero} -",ronda["theme"],":")
        for jugador,puntos in ronda["scores"].items() :
                total = sum(puntos.values())
                total_Ronda[jugador] = total
        ganador_Ronda = max(total_Ronda,key=total_Ronda.get)
        print(f"Ganador : {ganador_Ronda} ({total_Ronda[ganador_Ronda]} pts)")
        ganadas[ganador_Ronda] += 1
        for jug,pun in total_Ronda.items() :
            print(f"Participante : {jug} ({pun} pts)")
        print("-" * 20)
        numero += 1

def tablaFinal(rondas, ganadas) :
    datos= {"Valentina":{"Puntaje Total" : 0, "Mejor Ronda" : 0},
            "Mateo":{"Puntaje Total" : 0, "Mejor Ronda" : 0},
            "Camila":{"Puntaje Total" : 0, "Mejor Ronda" : 0},
            "Santiago":{"Puntaje Total" : 0, "Mejor Ronda" : 0},
            "Lucía":{"Puntaje Total" : 0, "Mejor Ronda" : 0}}
    for ronda in rondas : 
        for jugador,puntos in ronda["scores"].items() :
            total_Ronda = sum(puntos.values())
            datos[jugador]["Puntaje Total"] += total_Ronda
            if(total_Ronda  > datos[jugador]["Mejor Ronda"]) :
                datos[jugador]["Mejor Ronda"] = total_Ronda
    cuantasRondas = len(rondas)
    for jug in datos :
        datos[jug]["Promedio"] = datos[jug]["Puntaje Total"] / cuantasRondas
    datos_ordenados = sorted(datos.items(), key=criterio, reverse=True)
    for jug,info in datos_ordenados :
        print(f"Cocinero :  {jug}")
        print(f"Puntaje :  {info["Puntaje Total"]}")
        print(f"Rondas Ganadas :  {ganadas[jug]}")
        print(f"Mejor Ronda :  {info["Mejor Ronda"]}")
        print(f"Promedio :  {info["Promedio"]}")
        print("-" * 40)



def criterio(estructura):
    return estructura[1]["Puntaje Total"]
                
        
    


                
            
        
        
        
 

    
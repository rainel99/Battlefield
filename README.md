# Battlefield
 Proyecto de simulacion
## Integrantes:

- Rainel Fernández Abreu C-312
  
- Lázaro A. Castro Arango C-311

Nuestro proyecto tiene como objetivo simular una batalla entre dos ejércitos. Dichos ejércitos estarán conformados por soldados, soldados que tendrán algunas estadísticas como: 
- Ataque
- Defensa
- Vida
- Velocidad
- Alcance de ataque.

Cada una de estas estadísticas se definen al inicio de la simulación cuando es creado cada soldado y tienen valores predeterminados.
Además los soldados podrán vestir algunos tipos de armaduras que potenciarán sus estadisticas vitales, de modo que las mismas serán decisivas en el resultado final del enfrentamiento.
Estos soldados "pelearán" en un campo de batalla que estará representado por una matriz bidimensional. Los soldados en el momento que se crean se ubican en una posición válida de la matriz.
### Reglas de la simulación
- La simulación se llevará a cabo por rondas. 
- Cada ronda será una iteración de la simulacion. 
- En cada ronda, los soldados tendrán la posibilidad de atacara a un enemigo que se encuentre en su rango de ataque, de no cumplir esto el soldado se moverá para buscar un enemigo, en caso de que sea posible dicho movimiento. 
- Cada vez que un soldado muera no se ubica mas en el campo de batalla
- Un soldado muere cuando sus puntos de vida llegan a 0.
- Para finalizar la simualción se puede elegir entre alguno de estos criterios:
  - Un ejército perdió a todas sus tropas.
  - Luego de un número N de iteraciones algún ejército es el 20% del otro.
  - Luego de un número N de iteracones se detiene le simulación y el ejército ganador será el que tenga mayor cantidad de vida total, se define como vida total a la suma
   de los puntos de vidas de los soldados vivos en el momento que se detuvo la simulación.
 

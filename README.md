Battlefield

Propuesta para Proyecto de simulacion, asignatura del 3er año de la carrera Ciencia de la Computación, de la facultad de Matemática y Computación, MATCOM, Universidad de la Habana.

## Integrantes:

- Rainel Fernández Abreu C-312
  
- Lázaro A. Castro Arango C-311
  

Nuestro proyecto tiene como objetivo simular una batalla entre dos ejércitos. Dichos ejércitos estarán conformados por soldados, que tendrán algunas estadísticas que serán decisivas en el resultado de la batalla.

Cada una de estas estadísticas se definen al inicio de la simulación cuando es creado cada soldado y tienen valores predeterminados.
Además los soldados podrán vestir algunos tipos de armaduras que potenciarán sus estadisticas.
Estos soldados "pelearán" en un campo de batalla que estará representado por una matriz bidimensional. Los soldados en el momento que se crean se ubican en una posición válida de la matriz.

En dicho campo de batalla habrá "campamentos" donde los soldados podrán ir a alimentarse o reparar sus armaduras. Cada campamentos se creará en lugares arbitrarios al inico de la batalla.

### Reglas de la simulación

- La simulación se llevará a cabo por rondas. Donde cada ronda será una iteración de la simulación.
- En cada ronda, los soldados tendrán la posibilidad de atacar a un enemigo que se encuentre en su rango de ataque, de no cumplir esto el soldado se moverá para buscar un enemigo o moverse a alguno de sus campamentos.
- Cada vez que los puntos de vida de algún soldado llegue a 0, muere, este deja de existir en el campo de batalla.
- Para finalizar la simualción se puede elegir entre alguno de estos criterios:
  - Un ejército perdió a todas sus tropas.
  - Luego de un número N de iteraciones algún ejército es el 20% del otro.
  - Luego de un número N de iteracines se detiene la simulación y el ejército ganador será el que tenga mayor cantidad de vida total, se define como vida total a la suma de los puntos de vidas de los soldados vivos en el momento que se detuvo la simulación.
 

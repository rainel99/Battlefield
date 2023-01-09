Battlefield

Propuesta para Proyecto de simulacion, asignatura del 3er año de la carrera Ciencia de la Computación, de la facultad de Matemática y Computación, MATCOM, Universidad de la Habana.

## Integrantes:

- Rainel Fernández Abreu C-312
  
- Lázaro A. Castro Arango C-311
  
- Victor Amador C-312


  

Nuestro proyecto tiene como objetivo simular una batalla entre dos ejércitos. Dichos ejércitos estarán conformados por soldados, que tendrán algunas estadísticas que serán decisivas en el resultado de la batalla.

Cada una de estas estadísticas se definen al inicio de la simulación cuando es creado cada soldado y tienen valores predeterminados.
Además los soldados podrán vestir algunos tipos de armaduras que potenciarán sus estadísticas.
Estos soldados "pelearán" en un campo de batalla que estará representado por una matriz bidimensional. Los soldados en el momento que se crean se ubican en una posición válida de la matriz.

En dicho campo de batalla habrá "campamentos" donde los soldados podrán ir a alimentarse o reparar sus armaduras y armas. Cada campamentos se creará en lugares arbitrarios al inico de la batalla. En las batallas pueden ocurrir eventos relacionados con el tiempo, el cual se modeló haciendo
uso de una variable aleatoria con distribución normal apoyados en data-sets reales de datos climáticos. Otros factores como la edad también son generados de esta forma, por ejemplo se investigó que la edad media de las personas que participan en este tipo de conflictos es 32 y basado en eso se generan las edades de los soldados. Estos aspectos influyen en las estadísticas de los participantes y nos dan una idea de que importante son. 

### Reglas de la simulación

- La simulación se llevará a cabo por rondas. Donde cada ronda será una iteración de la simulación.
- En cada ronda, los soldados, en dependencia de su entorno, marcan un objetivo y ejecutarán las acciones necesarias para lograrlo. 
- Cada vez que los puntos de vida de algún soldado llegue a 0, muere, este deja de existir en el campo de batalla.
- Para finalizar la simualción se puede elegir entre alguno de estos criterios:
  - Un ejército perdió a todas sus tropas.
  - Luego de un número N de iteracines se detiene la simulación y el ejército ganador será el que tenga mayor cantidad de vida total, se define como vida total a la suma de los puntos de vidas de los soldados vivos en el momento que se detuvo la simulación.

### IA

GOAP o Goal Oriented Action Planning es una poderosa arquitectura de planificación diseñada para el control en tiempo real del comportamiento autónomo de los personajes en los juegos. Permite planificar dinámicamente una secuencia de acciones para satisfacer un objetivo establecido. La secuencia de acciones seleccionadas por el agente depende tanto del estado actual del agente como del estado actual del mundo, por lo tanto, a pesar de que a dos agentes se les asigne el mismo objetivo, ambos agentes podían seleccionar una secuencia de acciones completamente diferente.

El agente elabora un plan a partir de las condiciones iniciales y un objetivo. Los objetivos simplemente definen que condiciones deben cumplirse para satifacerlo. Un plan esta compuesto de acciones, que son solo un paso atómico dentro de un plan que hace que el agente haga algo. Cada acción definida es consciente de cuándo es válido ejecutarla, cuáles serán sus efectos en el mundo del juego y cuan costosa es.

El planificador es un pieza fundamental el GOAP, analiza las condiciones previas y efectos de cada acción para determinar una cola de acciones para satisfacer el objetivo. El planificador encuentra la solución construyendo un "árbol" y utilizando A*.

Otros contenidos de IA usados fueron BFS y un algoritmo génetico como alternativa a la asignacion de estadísticas y armaduras a los soldados. Este algoritmo crea en un principio una población y usa como función de fitnnes la propia simulación, elige los genes de la próxima generación mediante un ranking y se utiliza el cruce "one_point" para crear los nuevos indiviuos. Las poblaciones creadas a partir de este algoritmo génetico han tenido mucho más 'éxito en la simulación.



 
### DSL : BattleLanguage
**Dominio:**
Battle Language es un lenguaje diseñado con el fin de crear simulaciones
de batallas entre dos ejércitos de manera más sencilla.

**Características Generales:**
El lenguaje fue diseñado con un tipado estático, los tipos definidos fueron int, string, bool. Es un lenguaje de etiqueta inspirado en HTML, de manera que cada elemento necesario para arrancar una simulación entre
dos ejércitos lleva su etiqueta. Es posible definir funciones en el lenguaje que ayuden a la simulacón.

**Sintaxis:**
**Palabras claves**:
*simulation* ,*army*, *map*, *row*, *col*, *army_name*, *amount*, *if*,
*else*, *while*, *print*, *return*,*func*, *int*, *true*, *false*.

**Arquitectura:**
El compilador se puede divir en marcos:
* Léxer: este se llevo a cabo haciendo uso de la biblioteca
  ply.lex.
* Parser: se utiliza al igual que en el análisis léxico la libreria de python ply, específacamente el módulo ply.yacc. La construcción del AST se hace mediante el módulo nodes_ast.py que implementamos desde 0.
* Análisis Semántico: este se hace realiza haciendo un recorrido al AST.
  Luego se evalúa el AST.
* API : La API que se utiliza es el módulo que ejecuta la simualción.



**Ejecucion:**
El programa que se desee ejecutar para crear una nueva simulación debe
escribirse en el archivo test.txt. En el mismo hay un ejemplo de un
programa válido. Al compilar el archivo run.py el mismo se encargara de
leer este archivo para ejecutar el programa que su texto indica.

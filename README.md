Battlefield

Propuesta para Proyecto de simulacion, asignatura del 3er año de la carrera Ciencia de la Computación, de la facultad de Matemática y Computación, MATCOM, Universidad de la Habana.

## Integrantes:

- Rainel Fernández Abreu C-312
  
- Lázaro A. Castro Arango C-311
  

Nuestro proyecto tiene como objetivo simular una batalla entre dos ejércitos. Dichos ejércitos estarán conformados por soldados, que tendrán algunas estadísticas que serán decisivas en el resultado de la batalla.

Cada una de estas estadísticas se definen al inicio de la simulación cuando es creado cada soldado y tienen valores predeterminados.
Además los soldados podrán vestir algunos tipos de armaduras que potenciarán sus estadisticas.
Estos soldados "pelearán" en un campo de batalla que estará representado por una matriz bidimensional. Los soldados en el momento que se crean se ubican en una posición válida de la matriz.

En dicho campo de batalla habrá "campamentos" donde los soldados podrán ir a alimentarse o reparar sus armaduras. Cada campamentos se creará en lugares arbitrarios al inico de la batalla. En las batallas pueden ocurrir eventos relacionados con el tiempo, que se pretenden simular de manera aleatoria que pueden afectar a los ejércitos en cuestión.

### Reglas de la simulación

- La simulación se llevará a cabo por rondas. Donde cada ronda será una iteración de la simulación.
- En cada ronda, los soldados tendrán la posibilidad de atacar a un enemigo que se encuentre en su rango de ataque, de no cumplir esto el soldado se moverá para buscar un enemigo o moverse a alguno de sus campamentos.
- Cada vez que los puntos de vida de algún soldado llegue a 0, muere, este deja de existir en el campo de batalla.
- Para finalizar la simualción se puede elegir entre alguno de estos criterios:
  - Un ejército perdió a todas sus tropas.
  - Luego de un número N de iteraciones algún ejército es el 20% del otro.
  - Luego de un número N de iteracines se detiene la simulación y el ejército ganador será el que tenga mayor cantidad de vida total, se define como vida total a la suma de los puntos de vidas de los soldados vivos en el momento que se detuvo la simulación.

### IA

Se quiere que cada uno de los ejércitos, sea controlado por una inteligencia artificial que se encargará de tomar las decisiones que más beneficien al a su ejército en cada momento. Se definirán estados para lograr hacer búsqueda entre los posibles estados y obtener los mejores resultados posibles. La IA queremos se encargeue de mover a los soldados para busquen a los oponentes de una forma que minimicen el daño recibido y puedan causar mas bajas en el enemigos.
Se quiere además que la ubicación de los ejércitos asi como el balance de las estadísticas sea una tarea que la IA pueda resolver para mejorar el resultado de la batalla. 
 
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
*else*, *while*, *print*, *return*,*func*, *int*, *string*, *true*, *false*.

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
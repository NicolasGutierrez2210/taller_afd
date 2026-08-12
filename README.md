# Simulador de Autómata Finito Determinista (AFD)

Este proyecto implementa un reconocedor de lenguaje mediante un Autómata Finito Determinista (AFD) en Python. El programa recibe dinámicamente un archivo de configuración de transiciones y un archivo con cadenas de entrada.

El proyecto está diseñado con base en los 4 ejercicios del Ejemplo 3.16 (Página 149) del libro Compiladores: Principios, Técnicas y Herramientas (Aho, Sethi, Ullman).

---

## Expresiones Regulares Implementadas

1. Literal a) (a|b)* (conf_a.txt): Genera cualquier cadena formada por los símbolos 'a' y 'b'.
2. Literal b) (a*|b*)* (conf_b.txt): Equivalente a (a|b)*.
3. Literal c) ((ε|a)b*)* (conf_c.txt): Genera cualquier secuencia sobre el alfabeto {a, b}.
4. Literal d) (a|b)*abb (conf_d.txt): Reconoce cadenas sobre {a, b} que terminan estrictamente en la secuencia abb.

---

## Estructura de Archivos

* AFD.py: Script principal ejecutable en Python.
* cadenas.txt: Conjunto de cadenas de entrada a probar.
* conf_a.txt, conf_b.txt, conf_c.txt, conf_d.txt: Configuraciones del AFD.
* automata_a_b_c.dot, automata_d.dot: Código Graphviz para los autómatas.

---

## Instrucciones de Ejecución en Linux

Probar el literal a:
python3 AFD.py conf_a.txt cadenas.txt

Probar el literal d:
python3 AFD.py conf_d.txt cadenas.txt

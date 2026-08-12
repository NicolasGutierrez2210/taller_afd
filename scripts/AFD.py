import sys

def cargar_configuracion(archivo_conf):
    estados = set()
    alfabeto = set()
    estado_inicial = ""
    estados_aceptacion = set()
    transiciones = {}

    leyendo_transiciones = False

    with open(archivo_conf, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith('#'):
                continue

            if linea == 'transiciones:':
                leyendo_transiciones = True
                continue

            if leyendo_transiciones:
                if '->' in linea:
                    origen_simbolo, destino = linea.split('->')
                    origen, simbolo = origen_simbolo.split(',')
                    transiciones[(origen.strip(), simbolo.strip())] = destino.strip()
            else:
                if '=' in linea:
                    clave, valor = linea.split('=', 1)
                    clave = clave.strip()
                    valor = valor.strip()

                    if clave == 'estados':
                        estados = set(val.strip() for val in valor.split(','))
                    elif clave == 'alfabeto':
                        alfabeto = set(val.strip() for val in valor.split(','))
                    elif clave == 'inicial':
                        estado_inicial = valor
                    elif clave == 'aceptacion':
                        estados_aceptacion = set(val.strip() for val in valor.split(','))

    return estados, alfabeto, estado_inicial, estados_aceptacion, transiciones


def evaluar_cadena(cadena, estado_inicial, estados_aceptacion, transiciones, alfabeto):
    estado_actual = estado_inicial
    camino = [estado_actual]

    for simbolo in cadena:
        if simbolo not in alfabeto:
            return False, f"Simbolo '{simbolo}' no pertenece al alfabeto", camino
        
        clave = (estado_actual, simbolo)
        if clave in transiciones:
            estado_actual = transiciones[clave]
            camino.append(estado_actual)
        else:
            return False, f"Sin transicion desde {estado_actual} con '{simbolo}'", camino

    es_aceptada = estado_actual in estados_aceptacion
    return es_aceptada, estado_actual, camino


def main():
    if len(sys.argv) < 3:
        print("Uso correcto: python3 AFD.py <archivo_conf.txt> <archivo_cadenas.txt>")
        sys.exit(1)

    archivo_conf = sys.argv[1]
    archivo_cadenas = sys.argv[2]

    try:
        estados, alfabeto, inicial, aceptacion, transiciones = cargar_configuracion(archivo_conf)
        
        print("=" * 55)
        print(f"  CONFIGURACION DEL AFD: {archivo_conf}")
        print("=" * 55)
        print(f"Estados: {sorted(list(estados))}")
        print(f"Alfabeto: {sorted(list(alfabeto))}")
        print(f"Estado inicial: {inicial}")
        print(f"Estados de aceptacion: {sorted(list(aceptacion))}")
        print("=" * 55)
        print("\n--- EVALUACION DE CADENAS ---\n")

        with open(archivo_cadenas, 'r', encoding='utf-8') as f:
            for i, linea in enumerate(f, 1):
                cadena = linea.strip()
                if not cadena:
                    continue

                es_aceptada, estado_final, camino = evaluar_cadena(
                    cadena, inicial, aceptacion, transiciones, alfabeto
                )
                
                secuencia = " -> ".join(camino)
                resultado = "ACEPTADA" if es_aceptada else "RECHAZADA"
                
                print(f"Prueba #{i}: Cadena '{cadena}'")
                print(f"  Secuencia: {secuencia}")
                print(f"  Resultado: {resultado} (Estado final: {estado_final})\n")

    except FileNotFoundError as e:
        print(f"Error: No se pudo encontrar el archivo especificado -> {e}")
    except Exception as e:
        print(f"Ocurrio un error al ejecutar el AFD: {e}")


if __name__ == "__main__":
    main()

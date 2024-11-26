from datetime import datetime

listaDeExperimentos = [
    ["experimento1", "16/11/2024","quimica", [5,4,3,2,1]],
    ["experimento2", "16/11/2024","Fisica", [8,9,10,11]],
    ["experimento3", "17/11/2024","Ciencias Naturales", [7,6,5,4,3]],
    ["experimento4", "18/11/2024","Biologia", [9,8,7,6,5]],
]

class Experimentos:
    def __init__(self, nombre, fechaExperimento, tipo, resultados):
        self.nombre = nombre
        self.fechaExperimento = fechaExperimento
        self.tipo = tipo
        self.resultados = resultados
        
def agregar_experimento(listaDeExperimentos):
    try:
        nombre = input("Ingrese el nombre del experimento: ")
        fechaExperimento_str = input("Ingrese la fecha del experimento (dd/mm/yyyy): ")
        try:
            fechaExperimento = datetime.strptime(fechaExperimento_str, "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            print("Error: La fecha ingresada no es válida.")
            return

        tipo = input("Ingrese el tipo de experimento (quimica, Fisica, Biologia, Ciencias Naturales): ")

        resultados = list(map(int, input("Ingrese los resultados numéricos del experimento separados por comas: ").split(",")))

        listaDeExperimentos.append([nombre, fechaExperimento, tipo, resultados])
        print("Experimento agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar el experimento: {e}")

def eliminar_experimento(listaDeExperimentos):
   
    # Solicitar el nombre del experimento a eliminar
    nombre = input("Ingrese el nombre del experimento que desea eliminar: ")

    # Buscar el índice del experimento en la lista
    for experimento in listaDeExperimentos:
        if experimento[0] == nombre:  # Comparar el nombre del experimento
            listaDeExperimentos.remove(experimento)  # Eliminar el experimento usando su índice
            print(f"El experimento '{nombre}' ha sido eliminado correctamente.")
            return  # Salir de la función tras eliminar el experimento
    
    # Si no se encontró el experimento, informar al usuario
    print(f"Error: No se encontró un experimento con el nombre '{nombre}'.")

    #permite eliminar un experimento
    #dificultad 1: requiere la funcion agregar experimento

def visualizar_experimentos(listaDeExperimentos):
    
    # Verificar si la lista de experimentos está vacía
    if not listaDeExperimentos:
        print("No hay experimentos registrados. Agregue al menos uno antes de visualizar.")
        return

    # Mostrar los experimentos de forma organizada
    print("\nLista de experimentos registrados:")
    for i, experimento in enumerate(listaDeExperimentos, start=1):
        nombre, fecha, tipo, resultados = experimento
        print(f"\nExperimento {i}:")
        print(f"  Nombre: {nombre}")
        print(f"  Fecha: {fecha}")
        print(f"  Tipo: {tipo}")
        print(f"  Resultados: {resultados}")


# calcular estadisticas basicas (promedios, maximos y minimos de un experimento)
   #dificultad 2. requiere el uso de funciones agregar_experimeentos
    
def calcular_estadisticasExperimento(listaDeExperimentos):
    visualizar_experimentos(listaDeExperimentos)
    try:
        index = int(input("Ingrese el número del experimento: ")) - 1
        if 0 <= index < len(listaDeExperimentos):
            resultados = listaDeExperimentos[index][3]
            promedio = sum(resultados) / len(resultados)
            maximo = max(resultados)
            minimo = min(resultados)
            print(f"Estadísticas del experimento {listaDeExperimentos[index][0]}:")
            print(f"  Promedio: {promedio}")
            print(f"  Mínimo: {minimo}")
            print(f"  Máximo: {maximo}")
        else:
            print("Error: Número de experimento inválido.")
    except ValueError:
        print("Error: Entrada inválida.")

def comparar_experimentos(listaDeExperimentos):
    visualizar_experimentos(listaDeExperimentos)
    try:
        indices = list(map(int, input("Ingrese los índices de los experimentos que desea comparar, separados por comas: ").split(",")))
        resultados_comparados = []
        for index in indices:
            if 0 <= index - 1 < len(listaDeExperimentos):
                promedio = sum(listaDeExperimentos[index - 1][3]) / len(listaDeExperimentos[index - 1][3])
                resultados_comparados.append((index - 1, promedio))
            else:
                print(f"Índice {index} es inválido.")
        
        resultados_comparados.sort(key=lambda x: x[1])
        print("\nResultados comparados:")
        for index, promedio in resultados_comparados:
            print(f"{index + 1}. {listaDeExperimentos[index][0]} - Promedio: {promedio}")
    except ValueError:
        print("Error: Entrada inválida.")        
        
def generar_informe(listaDeExperimentos):
    if not listaDeExperimentos:
        print("No hay experimentos registrados. Agregue al menos uno antes de generar el informe.")
        return
    
     # Abrir un archivo txt para escribir el informe
    with open("informe_experimento.txt", "w") as archivo:
        # Escribir los detalles de la tarea en el archivo
        for tarea in listaDeExperimentos:
            archivo.write(f"Nombre: {tarea[0]}\n")
            archivo.write(f"Fecha: {tarea[1]}\n")
            archivo.write(f"Categoría: {tarea[2]}\n")
            archivo.write(f"Resultado: {tarea[3]}\n")
            archivo.write("\n")

    print("Informe generado como 'informe_experimento.txt'.")
       
    #gererar un infoeme resumen de los experimentos y sus estadisticas. difiultad 3
    #requiere el suso de funciones visualizar_experimentos y calcular_estadisticas
   

def mostrar_menu():
    listaExperimentos = []
    while True:
    #muestra el menu principal del programa. difiultad 1
        print("====menu principal=====")
        print("===gestios de experimentos===")
        print("1. Agregar experimento")
        print("2. Eliminar experimentos ")
        print("3. Visualizar experimentos")
        print("====analisis de datos=====")
        print("4. calcular estadisticas")
        print("5. comparar experimentos")
        print("====generar informe=====")
        print("6. generar informe")
        print("7. salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_experimento(listaExperimentos)
        elif opcion  == "2":
            eliminar_experimento(listaExperimentos)
        elif opcion == "3":
            visualizar_experimentos(listaExperimentos)
        elif opcion == "4":
            calcular_estadisticasExperimento(listaExperimentos)
        elif opcion == "5":
            comparar_experimentos(listaExperimentos)
        elif opcion == "6":
            generar_informe(listaExperimentos)  
        elif opcion == "7":     
            break
        else:
            print("Error: opción inválida.")


if __name__ == "__main__":
    mostrar_menu()
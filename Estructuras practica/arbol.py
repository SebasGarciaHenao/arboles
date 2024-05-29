class Paciente:
    def __init__(self, numeroid, nombre, edad, nivel_triaje, genero):
        self.numeroid = numeroid
        self.genero = genero
        self.nombre = nombre
        self.edad = edad
        self.nivel_triaje = nivel_triaje

    def __lt__(self, otro):
        if self.nivel_triaje == otro.nivel_triaje:
            return self.numeroid < otro.numeroid
        return self.nivel_triaje < otro.nivel_triaje

    def __str__(self):
        return f"El paciente con el número de llegada {self.numeroid} se llama {self.nombre} con la edad de {self.edad} años, porta un traje de nivel {self.nivel_triaje}, genero {self.genero}. "


class MinHeap:
    def __init__(self):
        self.heap = []

    def insertar(self, data):
        self.heap.append(data)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def consultar_proximo_paciente(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def atender_siguiente(self):
        if len(self.heap) > 1:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            min_element = self.heap.pop()
            self._heapify_down(0)
        elif len(self.heap) == 1:
            min_element = self.heap.pop()
        else:
            min_element = None
        return min_element

    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index > len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def consultar_pacientes_espera(self):
        return self.heap

    def consultar_pacientes_por_triaje(self, triaje):
        return [paciente for paciente in self.heap if paciente.nivel_triaje == triaje]

    def eliminar_paciente(self, numeroid):
        for index, paciente in enumerate(self.heap):
            if paciente.numeroid == numeroid:
                if index == len(self.heap) - 1:
                    self.heap.pop()
                else:
                    self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]
                    self.heap.pop()
                    self._heapify_down(index)
                    self._heapify_up(index)
                return f"Paciente con el número {numeroid} eliminado correctamente."
        return f"No se encontró ningún paciente con el número {numeroid}."

    def __str__(self):
        return str([str(paciente) for paciente in self.heap])


def ingresar_datos_paciente():
    numeroid = int(input("Número de llegada del paciente: "))
    nombre = input("Nombre del paciente: ")
    edad = int(input("Edad del paciente: "))
    nivel_triaje = int(input("Nivel de traje que portal el paciente: "))
    genero = input("Género del paciente: ")
    return Paciente(numeroid, nombre, edad, nivel_triaje, genero)


if __name__ == "__main__":
    heap = MinHeap()

    while True:
        print("\nMENU:")
        print("1. Agregar nuevo paciente.")
        print("2. Consultar próximo paciente.")
        print("3. Atender siguiente paciente.")
        print("4. Consultar pacientes en espera.")
        print("5. Consultar pacientes en espera por triaje.")
        print("6. Eliminar paciente.")
        print("7. Salir.")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            paciente = ingresar_datos_paciente()
            heap.insertar(paciente)
            print("Paciente registrado correctamente.")

        elif opcion == 2:
            proximo_paciente = heap.consultar_proximo_paciente()
            if proximo_paciente:
                print("El próximo paciente a atender es:")
                print(proximo_paciente)
            else:
                print("No hay pacientes en espera.")

        elif opcion == 3:
            atendido = heap.atender_siguiente()
            if atendido:
                print("Se ha atendido al siguiente paciente:")
                print(atendido)
            else:
                print("No hay pacientes para atender.")

        elif opcion == 4:
            pacientes_espera = heap.consultar_pacientes_espera()
            if pacientes_espera:
                print("Pacientes en espera:")
                for paciente in pacientes_espera:
                    print(paciente)
            else:
                print("No hay pacientes en espera.")

        elif opcion == 5:
            triaje = int(input("Ingrese el nivel de triaje para consultar pacientes en espera: "))
            pacientes_por_triaje = heap.consultar_pacientes_por_triaje(triaje)
            if pacientes_por_triaje:
                print(f"Pacientes en espera con triaje {triaje}:")
                for paciente in pacientes_por_triaje:
                    print(paciente)
            else:
                print(f"No hay pacientes en espera con triaje {triaje}.")

        elif opcion == 6:
            identificador_eliminar = int(input("Ingrese el número del paciente que desea eliminar: "))
            mensaje_eliminar = heap.eliminar_paciente(identificador_eliminar)
            print(mensaje_eliminar)

        elif opcion == 7:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

   

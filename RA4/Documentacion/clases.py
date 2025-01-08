# Definimos la clase Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def obtener_nombre(self):
        """Retorna el nombre del empleado."""
        return self.nombre
    
    def obtener_salario(self):
        """Retorna el salario del empleado."""
        return self.salario
    
    def aumentar_salario(self, porcentaje):
        """Aumenta el salario del empleado en un porcentaje dado."""
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento
        print(f"{self.nombre} ahora tiene un salario de {self.salario:.2f}")
    
    def mostrar_info(self):
        """Muestra la información del empleado."""
        return f"Empleado: {self.nombre}, Salario: {self.salario:.2f}"

# Definimos la clase Gerente que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    
    def obtener_departamento(self):
        """Retorna el departamento del gerente."""
        return self.departamento
    
    def asignar_tarea(self, tarea, empleado):
        """Asigna una tarea a un empleado."""
        print(f"{self.nombre} (Gerente del departamento {self.departamento}) ha asignado la tarea '{tarea}' a {empleado.obtener_nombre()}")
    
    def mostrar_info(self):
        """Sobrescribe el método de mostrar_info para incluir el departamento."""
        return f"Gerente: {self.nombre}, Departamento: {self.departamento}, Salario: {self.salario:.2f}"

# Crear instancias de las clases
empleado1 = Empleado("Juan Pérez", 3000)
gerente1 = Gerente("Ana Gómez", 5000, "Ventas")

# Mostrar la información de los empleados
print(empleado1.mostrar_info())
print(gerente1.mostrar_info())

# Aumentar salario de un empleado
empleado1.aumentar_salario(10)

# Asignar tarea al empleado por parte del gerente
gerente1.asignar_tarea("Preparar informe mensual", empleado1)


import heapq
import random

class Paciente:
    def __init__(self, nombre, nivel_urgencia, horas_espera):
        self.nombre = nombre
        self.nivel_urgencia = nivel_urgencia
        self.horas_espera = horas_espera

    def __lt__(self, other):
        # Define el orden de comparación para el montículo máximo (nivel de urgencia)
        return self.nivel_urgencia > other.nivel_urgencia

    def __gt__(self, other):
        # Define el orden de comparación para el montículo mínimo (horas de espera)
        return self.horas_espera < other.horas_espera

class SalaEmergencias:
    def __init__(self):
        self.max_heap = []  # Montículo máximo para el nivel de urgencia
        self.min_heap = []  # Montículo mínimo para el tiempo de espera

    def agregar_paciente(self, paciente):
        heapq.heappush(self.max_heap, paciente)
        heapq.heappush(self.min_heap, paciente)

    def atender_pacientes(self, num_pacientes):
        pacientes_atendidos = []
        for _ in range(num_pacientes):
            if not self.max_heap:
                break  # No hay más pacientes para atender

            paciente = heapq.heappop(self.max_heap)

            if paciente.nivel_urgencia == 10:
                # Atiende inmediatamente a los pacientes con urgencia máxima
                tiempo_espera = 0
            elif paciente.horas_espera > 5:
                # Atiende a los pacientes que han esperado más de 5 horas
                tiempo_espera = paciente.horas_espera
            else:
                # Atiende al paciente con la mayor urgencia
                tiempo_espera = paciente.horas_espera

            pacientes_atendidos.append((paciente.nombre, tiempo_espera))

        return pacientes_atendidos

# Simulación: Genera una lista de pacientes aleatorios
def generar_pacientes(num_pacientes):
    pacientes = []
    for i in range(num_pacientes):
        paciente = Paciente(f"Paciente {i+1}", random.randint(1, 10), random.randint(0, 10))
        pacientes.append(paciente)
    return pacientes

# Simulación: Atención de pacientes
def simulacion_atencion(sala_emergencias, pacientes):
    for paciente in pacientes:
        sala_emergencias.agregar_paciente(paciente)

    pacientes_atendidos = sala_emergencias.atender_pacientes(20)

    return pacientes_atendidos

# Ejecución de la simulación
sala_emergencias = SalaEmergencias()
pacientes_simulados = generar_pacientes(20)
pacientes_atendidos = simulacion_atencion(sala_emergencias, pacientes_simulados)

# Reporte de pacientes atendidos
print("Reporte de Pacientes Atendidos:")
for i, (nombre, tiempo_espera) in enumerate(pacientes_atendidos, start=1):
    print(f"{i}. {nombre} - Tiempo de Espera: {tiempo_espera} horas")

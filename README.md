# Montículos
"[GitHub Monticulos Repository](https://github.com/Gigabill/Mont-culos.git)"

El código fue estructurado de esta manera:

Clase Paciente con nombre, nivel de emergencia y horas de espera de cada paciente.

Un método __lt__ (menor que): se utiliza el montículo máximo para clasificar los pacientes con mayor nivel de emergencia.

Un método __gt__ (mayor que): se utiliza el montículo mínimo para clasoficar los pacientes con menor tiempo de espera.

Clase __SalaEmergencias__ definidos los montículos máximos y mínimos.

Un método __agregar_paciente__ para agregar los pacientes en cada montículo con la función headpush.

Un método __atender_pacientes__ que simula la atención de cada cliente según las reglas especificadas .

Una función __generar_pacientes__ para generar pacientes aleatorios.

Se ejecuta la simulación con 20 pacientes aleatorios.

Y por fin se mostra los pacientes atendidos.

Un código como este, estructurado con montículos, es extramademente útil para aplicar una prioridad, en este ejemplo cada paciente puede ser atendido de manera más eficiente de acuerdo con su nivel de emergencia y horas de espera, lo que en un hospital seria lo más conveniente tener un sistema con este.

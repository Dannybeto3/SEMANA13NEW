# Definir la matriz 3D con datos de ejemplo
temperaturas = [
    #Quito
    [
        [18, 22, 25, 27, 28, 29, 26],  # Semana 1
        [25, 26, 27, 28, 27, 26, 25],  # Semana 2
        [30, 30, 28, 27, 25, 25, 26],  # Semana 3
        [25, 27, 28, 28, 29, 28, 27]   # Semana 4
    ],
    #Guayaquil
    [
        [27, 32, 33, 28, 29, 29, 29],  # Semana 1
        [29, 28, 28, 30, 31, 31, 33],  # Semana 2
        [30, 32, 33, 29, 29, 30, 30],  # Semana 3
        [30, 31, 30, 32, 30, 28, 30]   # Semana 4
    ],
    #Cuenca
    [
        [25, 27, 26, 24, 23, 22, 21],  # Semana 1
        [26, 28, 25, 23, 22, 21, 20],  # Semana 2
        [27, 29, 26, 24, 23, 22, 21],  # Semana 3
        [28, 30, 27, 25, 24, 23, 22]   # Semana 4
    ]
]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for ciudad_index, ciudad in enumerate(temperaturas):
    print(f"Ciudad {ciudad_index + 1}:")
    for semana_index, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)
        print(f"  Semana {semana_index + 1}: Promedio de temperatura = {promedio:.2f}°C")

def promedio_temperatura(varias_temperaturas, ciudad, semana):
    promedio_temp = 0
    acumulador = 0
    for temp in range (len(varias_temperaturas[ciudad][semana])):
        acumulador += varias_temperaturas[ciudad][semana][temp]
    promedio_temp = acumulador/len(varias_temperaturas[ciudad][semana])
    return promedio_temp

print(promedio_temperatura(temperaturas,0,2))
print(promedio_temperatura(temperaturas, 1, 3))
print(promedio_temperatura(temperaturas, 2, 1))



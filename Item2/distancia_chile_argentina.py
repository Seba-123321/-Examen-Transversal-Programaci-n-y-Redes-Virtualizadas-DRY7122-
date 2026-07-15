print("=== Calculadora de distancia Chile - Argentina ===")

while True:

    print("\nEscriba 's' para salir")

    origen = input("Ciudad de Origen: ")

    if origen.lower() == "s":
        print("Programa finalizado")
        break


    destino = input("Ciudad de Destino: ")

    if destino.lower() == "s":
        print("Programa finalizado")
        break


    # Distancias de ejemplo entre ciudades principales

    viajes = {

        ("santiago", "buenos aires"): {
            "km": 1400,
            "horas": 2
        },

        ("valparaiso", "mendoza"): {
            "km": 400,
            "horas": 7
        },

        ("concepcion", "neuquen"): {
            "km": 900,
            "horas": 12
        }
    }


    clave = (
        origen.lower(),
        destino.lower()
    )


    if clave in viajes:

        distancia_km = viajes[clave]["km"]

        distancia_millas = distancia_km * 0.621371

        duracion = viajes[clave]["horas"]


        print("\nSeleccione transporte")
        print("1. Avion")
        print("2. Bus")
        print("3. Automovil")


        transporte = input("Opcion: ")


        if transporte == "1":
            medio = "avion"

        elif transporte == "2":
            medio = "bus"

        elif transporte == "3":
            medio = "automovil"

        else:
            medio = "transporte desconocido"



        print("\n===== Resultado =====")

        print(
            f"Viaje desde {origen} hasta {destino}"
        )

        print(
            f"Distancia: {distancia_km} kilometros"
        )

        print(
            f"Distancia: {distancia_millas:.2f} millas"
        )

        print(
            f"Duracion aproximada: {duracion} horas"
        )

        print(
            f"Medio seleccionado: {medio}"
        )

        print(
            f"Narrativa: El viaje inicia en {origen}, "
            f"recorriendo aproximadamente {distancia_km} km "
            f"hacia {destino} utilizando {medio}."
        )


    else:

        print(
            "No existe informacion para esas ciudades."
        )

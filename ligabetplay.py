import os

liga = []
fechas = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\n>> Presiona ENTER para continuar...")

def registrar_equipo():
    clear()
    nombre = input("Nombre del equipo: ").strip()
    equipo = {
        "nombre": nombre,
        "pj": 0,
        "pp": 0,
        "pe": 0,
        "gf": 0,
        "gc": 0,
        "plantel": []
    }
    liga.append(equipo)
    print(f"\n>>> Equipo '{nombre}' registrado.")
    pause()

def programar_fecha():
    clear()
    if len(liga) < 2:
        print("Debes registrar al menos 2 equipos.")
        pause()
        return

    print("Equipos disponibles:")
    for i, eq in enumerate(liga, start=1):
        print(f"  {i}. {eq['nombre']}")
    try:
        idxL = int(input("\nEquipo LOCAL (número): ")) - 1
        idxV = int(input("Equipo VISITANTE (número): ")) - 1
        fecha = input("Fecha del partido (ej: 2025-07-19): ").strip()
    except:
        print("Entrada inválida.")
        pause()
        return

    fechas.append({
        "eqL": liga[idxL],
        "eqV": liga[idxV],
        "fecha": fecha,
        "gfL": None,
        "gfV": None
    })
    print("\n>>> Partido programado.")
    pause()

def registrar_marcador():
    clear()
    pendientes = [f for f in fechas if f["gfL"] is None]
    if not pendientes:
        print("No hay partidos pendientes.")
        pause()
        return

    print("Partidos pendientes:")
    for i, f in enumerate(pendientes, start=1):
        print(f"  {i}. {f['fecha']} — {f['eqL']['nombre']} vs {f['eqV']['nombre']}")
    try:
        sel = int(input("\nSelecciona partido (número): ")) - 1
        partido = pendientes[sel]
        golL = int(input(f"Goles {partido['eqL']['nombre']}: "))
        golV = int(input(f"Goles {partido['eqV']['nombre']}: "))
    except:
        print("Entrada inválida.")
        pause()
        return

    partido["gfL"], partido["gfV"] = golL, golV

    eqL = partido["eqL"]
    eqL["pj"] += 1
    eqL["gf"] += golL
    eqL["gc"] += golV
    if golL < golV:
        eqL["pp"] += 1
    elif golL == golV:
        eqL["pe"] += 1

    eqV = partido["eqV"]
    eqV["pj"] += 1
    eqV["gf"] += golV
    eqV["gc"] += golL
    if golV < golL:
        eqV["pp"] += 1
    elif golV == golL:
        eqV["pe"] += 1

    print("\n>>> Marcador registrado.")
    pause()

def equipo_mas_goles_contra():
    clear()
    if not liga:
        print("No hay equipos registrados.")
        pause()
        return

    peor_equipo = liga[0]
    for equipo in liga:
        if equipo["gc"] > peor_equipo["gc"]:
            peor_equipo = equipo

    print(f"Equipo con MÁS goles en contra: {peor_equipo['nombre']} ({peor_equipo['gc']} GC)")
    pause()

def equipo_mas_goles_favor():
    clear()
    if not liga:
        print("No hay equipos registrados.")
        pause()
        return

    mejor_equipo = liga[0]
    for equipo in liga:
        if equipo["gf"] > mejor_equipo["gf"]:
            mejor_equipo = equipo

    print(f"Equipo con MÁS goles a favor: {mejor_equipo['nombre']} ({mejor_equipo['gf']} GF)")
    pause()

def registro_plantel():
    clear()
    if not liga:
        print("No hay equipos.")
        pause()
        return

    print("Selecciona equipo:")
    for i, eq in enumerate(liga, start=1):
        print(f"  {i}. {eq['nombre']}")
    try:
        eq = liga[int(input("\nEquipo (número): ")) - 1]
    except:
        print("Entrada inválida.")
        pause()
        return

    nombre = input("Nombre jugador: ").strip()
    try:
        edad = int(input("Edad: "))
    except:
        print("Edad inválida.")
        pause()
        return
    pos = input("Posición: ").strip()

    eq["plantel"].append({"nombre": nombre, "edad": edad, "pos": pos})
    print(f"\n>>> Jugador '{nombre}' agregado a {eq['nombre']}.")
    pause()

def main_menu():
    clear()
    print("=== LIGA BETPLAY ===")
    print("1. Registrar equipo")
    print("2. Programar fecha")
    print("3. Registrar marcador")
    print("4. Equipo más goles en contra")
    print("5. Equipo más goles a favor")
    print("6. Registro de plantel")
    print("7. Salir")
    try:
        op = int(input("\nElige una opción: "))
        if 1 <= op <= 7:
            return op
    except:
        pass
    return None

if __name__ == "__main__":
    while True:
        opcion = main_menu()
        if opcion == 1:
            registrar_equipo()
        elif opcion == 2:
            programar_fecha()
        elif opcion == 3:
            registrar_marcador()
        elif opcion == 4:
            equipo_mas_goles_contra()
        elif opcion == 5:
            equipo_mas_goles_favor()
        elif opcion == 6:
            registro_plantel()
        elif opcion == 7:
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción inválida.")
            pause()

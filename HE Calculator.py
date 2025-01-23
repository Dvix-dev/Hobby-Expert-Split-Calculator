'''
HE Split Price Calculator

Version: 1.4
Autor: David Escutia de Haro
'''

#### Declaración de Variables #######
carrito = {}  # Diccionario para almacenar las personas y los precios de objetos que han comprado
gastos_envio = 0
discount = 0

###### Funciones y Procedimientos ######
def main():
    global gastos_envio, discount

    print(r'''  
  _   _ _____   ____        _ _ _      ____      _            _       _             
 | | | | ____| / ___| _ __ | (_) |_   / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |_| |  _|   \___ \| '_ \| | | __| | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 |  _  | |___   ___) | |_) | | | |_  | |__| (_| | | (__| |_| | | (_| | || (_) | |   
 |_| |_|_____| |____/| .__/|_|_|\__|  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                     |_|                                                             
  By Dvix-dev - V1.4
''')

    try:
        gastos_envio = float(input("Introduzca el costo de los gastos de envío (0 si no hay): "))
    except ValueError:
        print("Entrada no válida. Se establece 0 por defecto.")
        gastos_envio = 0

    aritz5 = input("¿Ha introducido el código ARITZ5? (S/N): ").strip().lower()
    if aritz5 == "s":
        discount = 0.05
        print("Se aplicará un descuento del 5%.")
    else:
        discount = 0
        print("Sin descuento aplicado.")

    while True:
        option = menu()
        if option == 0:
            print("¡Gracias por usar el programa!")
            break
        elif option == 1:
            añadir_persona()
        elif option == 2:
            añadir_items()
        elif option == 3:
            mostrar_precio_detallado()
        elif option == 4:
            mostrar_totales_simplificados()
        else:
            print("Opción no válida. Intente de nuevo.")


def menu():
    print("\n--- Menú ---")
    print("1. Añadir persona")
    print("2. Añadir precios a una persona")
    print("3. Mostrar precio detallado de alguien")
    print("4. Mostrar el total acumulado (simplificado)")
    print("0. Salir")

    while True:
        try:
            option = int(input("Introduce una opción: "))
            return option
        except ValueError:
            print("Por favor, introduce un número válido.")


def añadir_persona():
    nombre = input("Introduce el nombre de la persona: ").strip()
    if nombre in carrito:
        print(f"{nombre} ya está en la lista.")
    else:
        carrito[nombre] = []
        print(f"Se ha añadido a {nombre}.")


def añadir_items():
    nombre = input("Introduce el nombre de la persona para añadir precios: ").strip()
    if nombre not in carrito:
        print(f"{nombre} no está en la lista. Usa la opción 1 para añadir a esta persona.")
        return

    while True:
        try:
            precio = float(input(f"Introduce el precio para {nombre} o 0 para terminar: "))
            if precio == 0:
                break
            carrito[nombre].append(precio)
            print(f"Se ha añadido un precio de {precio:.2f}€ a {nombre}.")
        except ValueError:
            print("Por favor, introduce un número válido para el precio.")


def calcular_totales_por_persona():
    """
    Calcula el subtotal de cada persona y reparte los gastos de envío proporcionalmente.
    """
    subtotales = {persona: sum(precios) for persona, precios in carrito.items()}
    total_general = sum(subtotales.values())
    reparto_envio = {persona: (subtotal / total_general) * gastos_envio for persona, subtotal in subtotales.items()}
    return subtotales, reparto_envio, total_general


def mostrar_precio_detallado():
    nombre = input("Introduce el nombre de la persona: ").strip()
    if nombre not in carrito:
        print(f"{nombre} no está en la lista.")
        return

    subtotales, reparto_envio, total_general = calcular_totales_por_persona()
    subtotal_persona = subtotales[nombre]
    envio_persona = reparto_envio[nombre]
    descuento_persona = (subtotal_persona / total_general) * (total_general * discount)

    print(f"\n-- {nombre} --")
    for idx, precio in enumerate(carrito[nombre], 1):
        print(f"{precio:.2f}€ | Item {idx}")
    
    if gastos_envio > 0:
        print(f"{envio_persona:.2f}€ | Gastos de envío")

    print("-" * 25)
    subtotal_con_envio = subtotal_persona + envio_persona
    print(f"{subtotal_con_envio:.2f}€ | Subtotal con envío")

    if discount > 0:
        print(f"- {descuento_persona:.2f}€ | Descuento aplicado")
        subtotal_con_envio -= descuento_persona

    print("-" * 25)
    print(f"{subtotal_con_envio:.2f}€ | Total a pagar")


def mostrar_totales_simplificados():
    """
    Muestra el total que debe pagar cada persona (simplificado).
    """
    subtotales, reparto_envio, total_general = calcular_totales_por_persona()

    print("\n--- Totales simplificados ---")
    total_final = 0
    for persona, subtotal in subtotales.items():
        envio_persona = reparto_envio[persona]
        descuento_persona = (subtotal / total_general) * (total_general * discount)
        total_persona = subtotal + envio_persona - descuento_persona
        print(f"{persona}: {total_persona:.2f}€")
        total_final += total_persona

    print("-" * 25)
    print(f"Total acumulado: {total_final:.2f}€")


###### Programa Principal #######
if __name__ == "__main__":
    main()

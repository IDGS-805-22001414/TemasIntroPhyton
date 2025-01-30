#Autor:Alondra Goretti Martinez Saldaña - IDGS805
class CinepolisPython:
    def __init__(self, nombre, cantidad_boletos, usa_tarjeta):
        self.nombre = nombre
        self.cantidad_boletos = cantidad_boletos
        self.usa_tarjeta = usa_tarjeta
        self.precio_boleto = 12
        self.total = 0

    def calcular_total(self):
        if self.cantidad_boletos > 7:
            return "Ups no puedes comprar más de 7 boletos. Por favor, inténtalo de nuevo."

        if self.cantidad_boletos > 5:
            descuento = 0.15
        elif 3 <= self.cantidad_boletos <= 5:
            descuento = 0.10
        else:
            descuento = 0

        self.total = self.cantidad_boletos * self.precio_boleto
        self.total -= self.total * descuento

        if self.usa_tarjeta:
            self.total -= self.total * 0.10

        return self.total

    def generar_tiket(self):
        with open("TiketBoletosCinePython.txt", "a") as archivo:
            archivo.write("----- TIKET CINEPOLIS PYTHON GRACIAS POR TU COMPRA :) -----\n")
            archivo.write(f"Nombre del comprador: {self.nombre}\n")
            archivo.write(f"Cantidad de boletos solicitados: {self.cantidad_boletos}\n")
            archivo.write(f"Total a pagar: ${self.total:.2f}\n")
            archivo.write("-----------------------------------------------------------\n\n")
        return "Tiket generado con éxito. Por favor, revisa tu tiket."

def realizar_compra():
    while True:
        print("\nBienvenido a CinepolisPython. Ten en cuenta lo siguiente:")
        print("Pueden comprar varias personas al mismo tiempo.")
        print("Se te aplicará descuento si compras entre 3 y 5 boletos: 10% de descuento.")
        print("Se te aplicará descuento si compras entre 6 y 7 boletos: 15% de descuento.")
        print("Si cuentas con tu tarjeta CINECO, se te añadirá un 10% de descuento adicional.")
        print("¡¡APROVECHA!!")

        nombre = input("Ingresa tu nombre: ")
        cantidad_boletos = int(input("Ingresa la cantidad de boletos que deseas comprar (máximo 7 por persona): "))
        if cantidad_boletos > 7:
            print("Has ingresado más de 7 boletos (recuerda que solo puedes comprar máximo 7 por persona). Por favor, intenta de nuevo.")
            continue

        usa_tarjeta = input("¿Pagarás con tu tarjeta de CINECO? (sí/no): ").strip().lower() == "sí"

        cinepolis = CinepolisPython(nombre, cantidad_boletos, usa_tarjeta)
        total = cinepolis.calcular_total()

        if isinstance(total, str):
            print(total)
            continue

        print(f"Tu total a pagar es: ${total:.2f}")
        confirmar = input("¿Estás seguro de tu compra? (si/no): ").strip().lower()
        if confirmar == "si":
            modificar = input("¿Deseas modificar los datos de tu compra? (modificar/no): ").strip().lower()
            if modificar == "modificar":
                print("Por favor, vuelve a ingresar tus datos.")
                continue
            elif modificar == "no":
                print(cinepolis.generar_tiket())
                return  # Termina la compra para esta persona
        else:
            print("Por favor vuelve a ingresar tus datos.")

def main():
    open("TiketBoletosCinePython.txt", "w").close()

    num_compradores = int(input("¿Cuántas personas comprarn boletos ?: "))

    for i in range(num_compradores):
        print(f"\nCompra para persona {i + 1}:")
        realizar_compra()
        print("\nCompra finalizada para esta persona.\n")

    print("¡Gracias por usar CinepolisPython! Hasta luego.")

main()
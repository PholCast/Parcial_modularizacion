def main():
    from Vehiculo import Vehiculo
    from Conductor import Conductor
    vehiculo1 = Vehiculo("Ford", "Mustang", 2022, 250.0)
    print("\n")
    vehiculo1.acelerar(10)
    print("\n")
    vehiculo1.mostrar_datos()  # salida esperada: "Marca: Ford, Modelo: Mustang, Año: 2022, Velocidad máxima: 250.0 km/h, Velocidad actual: 98.0 km/h"
    print("\n")
    vehiculo1.frenar(5)
    print("\n")
    vehiculo1.mostrar_datos()  # salida esperada: "Marca: Ford, Modelo: Mustang, Año: 2022, Velocidad máxima: 250.0 km/h, Velocidad actual: 49 km/h"
    print("\n")
    conductor1 = Conductor("Arnulfo")
    print("\n")
    conductor1.conducir_auto(vehiculo1) #salida esperada: "Marca: Ford, Modelo: Mustang, Año: 2022, Velocidad máxima: 250.0 km/h, Velocidad actual: 98.0 km/h"
main()
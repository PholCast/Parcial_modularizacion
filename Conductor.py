from dataclasses import dataclass

@dataclass
class Conductor:
    nombre:str

    def conducir_auto(self, auto) -> None:
        auto.acelerar(5)

        auto.mostrar_datos()
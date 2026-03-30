from models.habitacion import Habitacion, Suite, Master, SuitePresidencial


class HabitacionFactory:

    _tipos = {
        "suite": Suite,
        "master": Master,
        "presidencial": SuitePresidencial,
    }

    @staticmethod
    def build(tipo: str, numero: int, piso: int, precio: float | None = None) -> Habitacion:
        clase = HabitacionFactory._tipos.get(tipo.lower())

        if clase is None:
            tipos_validos = list(HabitacionFactory._tipos.keys())
            raise ValueError(f"Tipo '{tipo}' inválido. Tipos válidos: {tipos_validos}")

        if precio is not None:
            return clase(numero, piso, precio)

        return clase(numero, piso)
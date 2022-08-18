
class Cuota:

    contador_cuota = 0
    contador_prestamo = 0

    @classmethod
    def num_prestamo(cls):
        Cuota.contador_prestamo += 1
        return Cuota.contador_prestamo

    @classmethod
    def num_cuota(cls):
        Cuota.contador_cuota += 1
        return Cuota.contador_cuota

    def __init__(self, monto_cuota, fechas_pago, estado_pago) -> None:
        self._nu_cuota = Cuota.num_cuota()
        self._nu_prestamo = Cuota.num_prestamo()
        self._monto_cuota = monto_cuota
        self._fech_pago = list(fechas_pago)
        self._estado_pago = bool(estado_pago)


    @property
    def get_numero_cuota(self):
        return self._nu_cuota

    @property
    def get_numero_prestamo(self):
        return self._nu_prestamo

    @property
    def get_monto_cuota(self):
        return self._monto_cuota

    @get_monto_cuota.setter
    def set_monto_cuota(self, monto):
        self._monto_cuota = monto
        return self._monto_cuota

    @property
    def get_fecha_pago(self):
        return self._fech_pago

    @get_fecha_pago.setter
    def set_fecha_pago(self, fech_pago):
        self._fech_pago = fech_pago
        return self._fech_pago

    @property
    def get_estado_pago(self):
        return self._estado_pago

    @get_estado_pago.setter
    def set_estado_pago(self, estado):
        self._estado_pago = estado
        return self._estado_pago

    def __str__(self) -> str:
        return f"""
    N_cuota: {self.get_numero_cuota}
    N_prestatmo: {self.get_numero_prestamo}
    Monto_cuota: {self.get_monto_cuota}
    Fecha_pago: {self.get_fecha_pago}
    Estado_pago: {self.get_estado_pago}
    """

if __name__ == "__main__":
    cuota1 = Cuota(320000,["Enero","Febrero","Marzo","Abril","Mayo","Junio"],True)
    print(cuota1)
    
    print(cuota1.get_monto_cuota)

    cuota1.set_monto_cuota = "400000"
    print(cuota1)
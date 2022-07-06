class Prestamo:

    contador_prestamo = 0

    @classmethod
    def num_prestamo(cls):
        Prestamo.contador_prestamo += 1
        return Prestamo.contador_prestamo

    def __init__(self, num_identidad, valor_prestamo, fecha_autorizacion, fecha_tentativa) -> None:
        self._n_prestamo = Prestamo.num_prestamo()
        self._num_identidad = num_identidad
        self._valor_prestamo = valor_prestamo
        self._fecha_autorizacion = fecha_autorizacion
        self._fecha_tentativa = fecha_tentativa

    @property
    def get_num_prestamo(self):
        return self._n_prestamo

    @property
    def get_num_identidad(self):
        return self._num_identidad

    @get_num_identidad.setter
    def set_num_identidad(self, num_ident):
        self._num_identidad = num_ident
        return self._num_identidad

    @property
    def get_valor_prestamo(self):
        return self._valor_prestamo

    @get_valor_prestamo.setter
    def set_valor_prestamo(self, val_pres):
        self._valor_prestamo = val_pres
        return self._valor_prestamo

    @property
    def get_fecha_auto(self):
        return self._fecha_autorizacion

    @get_fecha_auto.setter
    def set_fecha_auto(self, fech_auto):
        self._fecha_autorizacion = fech_auto
        return self._fecha_autorizacion

    @property
    def get_fecha_tentativa(self):
        return self._fecha_tentativa

    @get_fecha_tentativa.setter
    def set_fecha_tentativa(self, fecha_tenta):
        self._fecha_tentativa = fecha_tenta
        return self._fecha_tentativa

    def __str__(self) -> str:
        return f"""
        N_prestamo: {self.get_num_prestamo}
        N_identidad: {self.get_num_identidad}
        Valor_prestamo: {self.get_valor_prestamo}
        Fecha_autorizacion: {self.get_fecha_auto}
        Fecha_tentativa: {self.get_fecha_tentativa}
        """

if __name__ == "__main__":
    prestamo1 = Prestamo(132,1300000,"12/07/2021","12/07/2022")
    print(prestamo1)
    prestamo2 = Prestamo(1432,2000000,"13/08/2020","13/08/2020")
    print(prestamo2)

class Persona:

    def __init__(self, num_identificacion,primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono_movil, telefono_personal):
        self._num_identificacion = num_identificacion
        self._primer_nombre = primer_nombre
        self._segundo_nombre = segundo_nombre
        self._primer_apellido = primer_apellido
        self._segundo_apellido = segundo_apellido
        self._telefono_movil = telefono_movil
        self._telefono_personal = telefono_personal

    @property
    def get_num_identificacion(self):
        return self._num_identificacion

    @get_num_identificacion.setter
    def set_num_identificacion(self, numero):
        self._num_identificacion = numero
        return self._num_identificacion

    @property
    def get_primer_nombre(self):
        return self._primer_nombre

    @get_primer_nombre.setter
    def set_primer_nombre(self, primer_nom):
        self._primer_nombre = primer_nom
        return self._primer_nombre

    @property
    def get_segundo_nombre(self):
        return self._segundo_nombre

    @get_segundo_nombre.setter
    def set_segundo_nombre(self, segundo_nom):
        self._segundo_nombre = segundo_nom
        return self._segundo_nombre

    @property
    def get_primer_apellido(self):
        return self._primer_apellido

    @get_primer_apellido.setter
    def set_primer_apellido(self, primer_ape):
        self._primer_apellido = primer_ape
        return self._primer_apellido

    @property
    def get_segundo_apellido(self):
        return self._segundo_apellido

    @get_segundo_apellido.setter
    def set_segundo_apellido(self, segundo_ape):
        self._segundo_apellido = segundo_ape
        return self._segundo_apellido

    @property
    def get_telefono_movil(self):
        return self._telefono_movil

    @get_telefono_movil.setter
    def set_telefono_movil(self, tele_movil):
        self._telefono_movil = tele_movil
        return self._telefono_movil

    @property
    def get_telefono_personal(self):
        return self._telefono_personal

    @get_telefono_personal.setter
    def set_telefono_personal(self, tele_personal):
        self._telefono_personal = tele_personal
        return self._telefono_personal

    def __str__(self):
        return f"""
        N_identificación : {self._num_identificacion}
        1er_Nombre : {self._primer_nombre}
        2do_Nombre : {self._segundo_nombre}
        1er_Apellido : {self._primer_apellido}
        2do_Apellido : {self._segundo_apellido}
        Tele_Movil : {self._telefono_movil}
        Tele_Personal : {self._telefono_personal}
        """
if __name__ == "__main__":
    persona1 = Persona(123, "Diego","Miguel","Sanchez","Buitrago",721345,3203329228)
    print(persona1)
    persona2 = Persona(1234, "Juan","Camilo","Sanchez","Buitrago",721665,3204573101)
    print(persona2)
    persona3 = Persona(12345, "Blanca","Duvy","Buitrago","Escobar",721789,3133628460)
    print(persona3)
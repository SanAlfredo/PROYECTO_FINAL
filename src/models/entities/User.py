from utils.DateFormat import DateFormat

class User():

    

    def __init__(self, id=None, cedula_identidad=None, nombre=None, primer_apellido=None, segundo_apellido=None, fecha_nacimiento=None) -> None:
        self.id = id
        self.cedula_identidad = cedula_identidad
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento

    def to_JSON(self):
        return {
            'id': self.id,
            'cedula_identidad': self.cedula_identidad,
            'nombre': self.nombre,
            'primer_apellido': self.primer_apellido,
            'segundo_apellido': self.segundo_apellido,
            'fecha_nacimiento': DateFormat.convertir_fecha(self.fecha_nacimiento)
        }
    
    #funciones de prueba para otra base de datos y probar metodos get
    # def __init__(self, id_persona=None, nombre=None, apellido1=None, apellido2=None, fecha=None, tipo_sexo=None) -> None:
    #     self.id_persona = id_persona
    #     self.nombre = nombre
    #     self.apellido1 = apellido1
    #     self.apellido2 = apellido2
    #     self.fecha = fecha
    #     self.tipo_sexo = tipo_sexo

    # def to_JSON(self):
    #     return {
    #         'id_persona': self.id_persona,
    #         'nombre': self.nombre,
    #         'apellido1': self.apellido1,
    #         'apellido2': self.apellido2,
    #         'fecha': self.fecha,
    #         'tipo_sexo': self.tipo_sexo
    #     }
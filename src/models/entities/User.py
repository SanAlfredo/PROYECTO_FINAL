class User():

    def __init__(self, id, cedula_identidad=None, nombre=None, primer_apellido=None, segundo_apellido=None, fecha_nacimiento=None) -> None:
        self.id=id
        self.cedula_identidad=cedula_identidad
        self.nombre=nombre
        self.primer_apellido=primer_apellido
        self.segundo_apellido=segundo_apellido
        self.fecha_nacimiento=fecha_nacimiento
    
    def to_JSON(self):
        return {
            'id':self.id,
            'cedula_identidad':self.cedula_identidad,
            'nombre':self.nombre,
            'primer_apellido':self.primer_apellido,
            'segundo_apellido':self.segundo_apellido,
            'fecha_nacimiento':self.fecha_nacimiento
        }

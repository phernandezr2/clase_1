class Empleado :

    def __intf__ (self):
        self.nombre = None
        self.apellido = None
        self.cargo = None
        self.sueldo = None
        
    def __str__ (self):
        return str (
            "nombre: {} \n"
            "apellido {} \n"
            "cargo {}   \n "
            "sueldo {}\n"
        ).format(
            self.nombre,
            self.apellido,
            self.cargo,
            self.sueldo
        )    
     
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre    

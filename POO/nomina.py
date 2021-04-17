from indicadores import indicadores

class Nomina(Indicadores):

    def __init__ (self):
        self.__salarioBasico = 0
        self.__diasLiquidados = 0 
        self.__smlv = self.salarioMinimo()
        self.__auxilioT = 106454

    def setSalarioBasico (self, salarioBasico):
        if str(type(salarioBasico)) == "<class 'int'>" or str(type(salarioBasico))== "<class 'float'>":
            if salarioBasico >= self.salariominimo():
                self.__salarioBasico = salarioBasico
            else :
                print ('el salario basico no puede ser inferior al SWVL legas vigente')
        else :
            print('error')


    def getSalarioBasico (self):
        return self.__salarioBasico    

    def getDiasLiquidados (self):
        return self.__diasLiquidados

    def setDiasLiquidados (self, diasLiquidados):
        self.__diasLiquidados = diasLiquidados       

    def salarioDevengado (self):
        try:
            return (self.__salarioBasico / 30 ) *self.__diasLiquidados 
        except Exception as e:
            print (e)
            print ('error al calcular salario')

    def auxilioTransporte (self) :
        if self.__salarioBasico >  (self.__slmv * 2):
            return 0
        else :
            return sef.__auxilioT /30 * self.__diasLiquidados

    def totalDevengado(self):
        return  self.__salarioDevengado() + sef.__auxiliotransporte()      

    def __str___(self):
        return str("salario basico {} \n"
                    "dias liquidado {} \n "    
                    "salario devengado {} \n "
                    "auxilio de transporte {} \n"
                    "total devengado {} \n" ).format(
                        self.__salarioBasico,
                        self.__diasLiquidados,
                        self.salarioDevengado(),
                        self.auxilioTransporte(),
                        self.totalDevengado()
                    ) 
'''
from empleado import Empleado 

e1 = Emepleado()
e1.nombre = " pedro "
e1.apellido = " hernanedez "
e1.cargo = "Ing Mecanico  "
e1.sueldo = "30 millones "

print (e1)
'''

from nomina import Nomina 

nomina=[]

while True:
    print("1 ingresar nomina")
    print("2 salir")
    
    opcion = input("ingrese la opcion")

    if opcion =="1":
        renglon = []
        n=Nomina()
        salario = float(input("ingrese el sueldo basico"))
        diasL = float(input("ingrese los dias liquidados "))
        n.setSalarioBasico(salario)
        n.getDiasLiquidados(diasL)
        print (n)

        renglon.append({'variable: ': 'salario basico',"resultado ":n.getSalarioBasico()})
        renglon.append({'variable: ': 'dias liquidados',"resultado ":n.getDiasLiquidados()})
        renglon.append({'variable: ': 'salarios devengados',"resultado ":n.salarioDevengado()})
        renglon.append({'variable: ': 'auxilio transporte',"resultado ":n.auxilioTransporte})
        renglon.append({'variable: ': 'total devengado ',"resultado ":n.totalDevengado()})
        nomina.append(renglon)

    elif opcion == "2":
        print ('saliendo')
        break 


f = open ('nominas.txt', 'w')

for i in nomina:
    f.write('******************************')
    for j in i :
        f.write(str(j)+ '\n' )
f.close()        







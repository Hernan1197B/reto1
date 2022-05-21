print("")
print("**Programa para calcular el valor del interes y monto a recibir de acuerdo a su invercion en un CDT**")
print("")

print ("OBSERVACION: ") 
print ("")
print ("Para asegurar una rentabilidad de (3%) libre de riesgo, el tiempo de permanencia debera ser mayor a dos (2) meses")
print ("de lo contrario, si el dinero se retira antes o durante este periodo se aplica una penalidad del 2%.")
print ("")

def CDT(usuario: str, capital: float, tiempo: float,):
     
    
    if(tiempo>2):
        ganancia = (capital * 0.03 * tiempo) / 12 #interes ganado por tiempo mayor a 12 meses
        vtotal = ganancia + capital
        
       
    elif(tiempo<=2):
        ganancia = capital * 0.02 #Perdida generada por tiempo menor o igual a 2 meses 
        vtotal = capital - -ganancia
        
    print("")
    return "Para el usuario: {}, el interes generado es de: ${}, por un tiempo de {} meses, con un capital inicial de ${}, la cantidad de dinero a recibir es: ${}" .format(usuario, ganancia, tiempo, capital, vtotal)

print("")
usuario = str(input("Por favor dijite su usuario: "))
print("")
capital = float(input("Por favor ingrese el capital inicial de invercion en el CDT: "))
print("")
tiempo = float(input("Por favor ingrese el tiempo de permanencia en el CDT: "))

print(CDT(usuario, capital, tiempo))
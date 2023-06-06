import consulta_BBDD
import time

#inicializamos variables de los sensores
tempDI=0
tempDD=0
tempTI=0
tempTD=0
presion=0
rpm=0
giro=0


# cambio de imagenes - por ahora nada
# imagenT="1"
# imagenH="1"
# imagenL="1"


while True:
	#Leo lo recibido de los sensores
	with open("/home/estudiante/Documentos/sofia/PBL/lectura/temperaturaDI","r") as file:   #/home/xilinx/f1mon/lectura/giro
		tempDI = file.read()
	with open("/home/estudiante/Documentos/sofia/PBL/lectura/temperaturaDD","r") as file:
		tempDD = file.read()
	with open("/home/estudiante/Documentos/sofia/PBL/lectura/temperaturaTI","r") as file:
		tempTI = file.read()
	with open("/home/estudiante/Documentos/sofia/PBL/lectura/temperaturaTD","r") as file:
		tempTD = file.read()
	with open("/home/estudiante/Documentos/sofia/PBL/lectura/presion","r") as file:
		presion = file.read()
	with open("/home/estudiante/Documentos/sofia/PBL/lectura/revoluciones","r") as file:
		rpm = file.read()
	with open("/home/estudiante/Documentos/sofia/PBL/lectura/giro","r") as file:
		giro = file.read()



	consulta_BBDD.insert_neumatico(presion, tempDI, rpm, giro, "DELANTE_IZQ")
	consulta_BBDD.insert_neumatico(presion, tempDD, rpm, giro, "DELANTE_DER")
	consulta_BBDD.insert_neumatico(presion, tempTI, rpm, giro, "ATRAS_IZQ")
	consulta_BBDD.insert_neumatico(presion, tempTD, rpm, giro, "ATRAS_DER")
	print("se ha insertado neumaticos")


	time.sleep(10)
	


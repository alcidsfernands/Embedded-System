from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/interfaz")	#RUTA DEL HTML
def raiz():
	#inicializamos variables de los sensores
	# temperatura=0
	# humedad=0
	# humedad_suelo=0
	# luz=0
	# agua=0


	# cambio de imagenes - por ahora nada
	# imagenT="1"
	# imagenH="1"
	# imagenL="1"



	#Leo lo recibido de los sensores
	#with open("/home/xilinx/pruebag4/lectura/temperatura","r") as file:
		#temperatura = file.read()
	#with open("/home/xilinx/pruebag4/lectura/humedad","r") as file:
		#humedad = file.read()
	#with open("/home/xilinx/pruebag4/lectura/humedad_suelo","r") as file:
	#	humedad_suelo = file.read()
	#with open("/home/xilinx/pruebag4/lectura/luz","r") as file:
		#luz = file.read()
#	with open("/home/xilinx/pruebag4/lectura/agua","r") as file:
#		agua = file.read()




	#PROGRAMACION
	# if (int(temperatura) > 15):
	# 	imagenT = "2"
	
	# if (int(humedad) > 70) and (int(humedad) < 150):
	# 	imagenH = "2"
	# if (int(humedad) >= 150):
	# 	imagenH = "3"
	
	# if (int(luz) > 5) and (int(luz) < 10):
	# 	imagenL = "2"
	# if (int(luz) >= 10):
	# 	imagenL = "3"
	#return render_template("interfaz.html", valorT=temperatura, valorH=humedad, valorL=luz, rangoT=imagenT, rangoH=imagenH, rangoL=imagenL)
	return render_template("INTERFAZv0.html")


app.run(host='0.0.0.0', port=8000, debug=True)
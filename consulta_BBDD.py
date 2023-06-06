import mysql.connector
import datetime


#Para insertar en una base de datos
def insert_neumatico(PRESION, TEMP, REVOLUCIONES, ANGULOGIRO, POS):
	try:
		cnx = mysql.connector.connect(user = "root", password = "Muaeci_2022", host = "127.0.0.1", database = "F1MON")
		cursor = cnx.cursor()
		print("Se ha abierto la conexion - NEUMATICO")
		query = """INSERT INTO NEUMATICO (ID_COCHE, PRESION, TEMP, REVOLUCIONES, ANGULOGIRO, POS, TIME) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
		NOW = datetime.datetime.utcnow()
		values = (1, PRESION, TEMP, REVOLUCIONES, ANGULOGIRO, POS, NOW.strftime('%Y-%m-%d %H:%M:%S'))
		cursor.execute(query, values)
		cnx.commit()

	except mysql.connector.Error as error:
		print("No se ha podido insertar en la BBDD - NEUMATICO")

	finally:
		if cnx.is_connected():
			cursor.close()
			cnx.close()
			print("Se ha cerrado la conexion")
		


def insert_chasis(TENSION, AERO):
	try:
		cnx = mysql.connector.connect(user = "root", password = "Muaeci_2022", host = "127.0.0.1", database = "F1MON")
		cursor = cnx.cursor()
		print("Se ha abierto la conexion - CHASIS")
		query = """INSERT INTO CHASIS (ID_COCHE, TENSION, AERO, TIME) VALUES (%s,%s,%s,%s)"""
		NOW = datetime.datetime.utcnow()
		values = (1, TENSION, AERO, NOW.strftime('%Y-%m-%d %H:%M:%S'))
		cursor.execute(query, values)
		cnx.commit()

	except mysql.connector.Error as error:
		print("No se ha podido insertar en la BBDD - CHASIS")

	finally:
		if cnx.is_connected():
			cursor.close()
			cnx.close()
			print("Se ha cerrado la conexion")


def insert_UP(NIVEL, TEMP, TENSION):
	try:
		cnx = mysql.connector.connect(user = "root", password = "Muaeci_2022", host = "127.0.0.1", database = "F1MON")
		cursor = cnx.cursor()
		print("Se ha abierto la conexion - UP")
		query = """INSERT INTO UP (ID_COCHE, NIVEL, TEMP, TENSION, TIME) VALUES (%s,%s,%s,%s,%s)"""
		NOW = datetime.datetime.utcnow()
		values = (1, NIVEL, TEMP, TENSION, NOW.strftime('%Y-%m-%d %H:%M:%S'))
		cursor.execute(query, values)
		cnx.commit()

	except mysql.connector.Error as error:
		print("No se ha podido insertar en la BBDD - UP")

	finally:
		if cnx.is_connected():
			cursor.close()
			cnx.close()
			print("Se ha cerrado la conexion")

def insert_POS(GPS, DISTANCIA, CAMARA):
	try:
		cnx = mysql.connector.connect(user = "root", password = "Muaeci_2022", host = "127.0.0.1", database = "F1MON")
		cursor = cnx.cursor()
		print("Se ha abierto la conexion - POS")
		query = """INSERT INTO POS (ID_COCHE, GPS, DISTANCIA, CAMARA, TIME) VALUES (%s,pointfromtext(%s),%s,%s,%s)"""
		NOW = datetime.datetime.utcnow()
		values = (1, GPS, DISTANCIA, CAMARA, NOW.strftime('%Y-%m-%d %H:%M:%S'))
		cursor.execute(query, values)
		cnx.commit()

	except mysql.connector.Error as error:
		print("No se ha podido insertar en la BBDD - POS", error)

	finally:
		if cnx.is_connected():
			cursor.close()
			cnx.close()
			print("Se ha cerrado la conexion")



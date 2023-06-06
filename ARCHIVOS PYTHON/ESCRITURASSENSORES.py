from pynq import Overlay

ol = Overlay("/home/xilinx/pruebag4/sensor.bit")
ol.download()

IP_BASE_ADDRESS = 0x00A0000000
ADDRESS_RANGE=0x10000


#------------------------------------------------------------------------------------------------------------------------------------------
#ESCRITURA HD_GPIOS

#ol_TH = Overlay("/home/xilinx/pruebag4/XXXXX.bit")
#ol_TH.download()

#IP_BASE_ADDRESS = 0x00A0000000
#ADDRESS_RANGE=0x10000

#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------
#ESCRITURA I2C

# ol_LUZ = 
# ol_AGUA =

#------------------------------------------------------------------------------------------------------------------------------------------ 


from pynq import MMIO
mmio = MMIO(IP_BASE_ADDRESS, ADDRESS_RANGE)

from time import sleep


while True:
	mmio.write(12,1)
	sleep(5) #ESCRIBIMOS DATOS CADA 5 SEG
	with open("/home/xilinx/pruebag4/lectura/temperatura","w") as file:
		file.write(str(mmio.read(0)))
	with open("/home/xilinx/pruebag4/lectura/humedad","w") as file:
		file.write(str(mmio.read(4)))
	with open("/home/xilinx/pruebag4/lectura/luz","w") as file:
		file.write(str(mmio.read(8)))
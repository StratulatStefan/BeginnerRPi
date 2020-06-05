import subprocess
from DHT11 import *
from MQ2 import *

def GetSystemData():
	filepath = "/usr/bin/vcgencmd"
	field = {
		"cpu_temp" : "measure_temp",
		"frecv_arm" : "measure_clock arm",
		"frecv_core" : "measure_clock core",
		"tens_alim_core" : "measure_volts core",
		"throttle" : "get_throttled",
		"ram_cpu" : "get_mem arm",
		"ram_gpu" : "get_mem gpu",
		"tens_ram" : "measure_volts sdram_c",
		"tens_io" : "measure_volts sdram_i",
		"sd_card_clock" : "measure_clock emmc"
	}
	data = {}
	'''
	for key in field:
		process = subprocess.Popen([filepath, field[key]], stdout=subprocess.PIPE)
		output = process.stdout.readline().decode('ascii')
		data[key] = output[:-1]
	'''
	return data


def GetTempHumidityGas():
	temperatura, umiditate = TemperatureAndHumidity()
	gas = Gas()
<<<<<<< HEAD
	return {"temp" : temperatura ,"umiditate" : umiditate, "gaz" : gas}
=======
	return {"temp" : temperatura ,"umiditate" : umiditate, "gaz" : gas}
>>>>>>> 30609e3408c4277b8b70fa24deaba6c110fe43ed

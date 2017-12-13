#! python

# this script will read values from the dust sensor file and plot them using
# matplotlib
import numpy
import matplotlib.pyplot as plt
import itertools
class Sensordata:
	def __init__(self, identifier, data):
		self.identifier = identifier
		self.data=data
writer = open("thanksgivingdust.csv")
#the first line of .csv is always going to be a "sep", so we don't care
titel = writer.readline()
titel = titel.split(';')
writer.readline()
sensors = {};
while(True):
	f = writer.readline()
	if(writer == ""):
		break
	try:
		infos = f.split(';')
		if infos[0] == "":
			raise IndexError
		if infos[0] not in sensors:
			sensors[infos[0]] = {}
		if infos[1] not in sensors[infos[0]]:
			sensors[infos[0]][infos[1]] = []
		sensors[infos[0]][infos[1]].append(infos[2:])
	except IndexError:
		print("reached eof")
		break
print(sensors["0"].keys())
sensordatas = []
for thing in sensors["1"]:
	if thing == "high":
		for stuff in sensors["1"][thing]:
			print(stuff[5])
			print(stuff[0])
			low.setdefault("altitude", []).append(stuff[5])
			low.setdefault("LPO", []).append(stuff[0])
plt.plot([float(x) for x in low["altitude"]],[int(x) for x in low["LPO"]], 'ro')	
plt.show()
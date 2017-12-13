#! python

# this script will read values from the dust sensor file and plot them using
# matplotlib
import numpy
import matplotlib.pyplot as plt
import itertools
class Sensordata:
	def __init__(self, identifier, highdata, lowdata):
		self.identifier = identifier
		self.highdata = highdata
		self.lowdata = lowdata
		self.altitude = [float(x[5]) for x in highdata[:len(lowdata)]]
		self.lowLPO = [int(x[0]) for x in lowdata]
		self.highLPO = [int(x[0]) for x in highdata]
	def maxaltitudelocation(self):
		prevalt = -1
		maxalt = 0
		for i in range(len(self.altitude)):
			if(self.altitude[i] > prevalt):
				prevalt = self.altitude[i]
				maxalt = i
		return maxalt
writer = open("thanksgivingdust.csv")
#the first line of .csv is always going to be a "sep", so we don't care
titel = writer.readline()
titel = titel.split(';')
writer.readline()
sensors = {}
#to do: clean up int() function to only run once
while(True):
	f = writer.readline()
	if(writer == ""):
		break
	try:
		infos = f.split(';')
		if infos[0] == "":
			raise IndexError
		if int(infos[0]) not in sensors:
			sensors[int(infos[0])] = {}
		if infos[1] not in sensors[int(infos[0])]:
			sensors[int(infos[0])][infos[1]] = []
		sensors[int(infos[0])][infos[1]].append(infos[2:])
	except IndexError:
		print("reached eof")
		break
print(sensors[0].keys())
sensordata = []
for i in sensors.keys():
	sensordata.append(Sensordata(i, sensors[i]["high"], sensors[i]["low"]))
	plt.figure("high sensor %d"%(i))
	plt.subplot(211)
	plt.title("sensor %d ascent, large particles"% (i))
	plt.plot(sensordata[i].altitude[:sensordata[i].maxaltitudelocation()], sensordata[i].highLPO[:sensordata[i].maxaltitudelocation()], 'ro')
	plt.ylabel("LPO")
	plt.xlabel("altitude (feet)")
	plt.subplot(212)
	plt.title("sensor %d descent, large particles" % (i))
	plt.plot(sensordata[i].altitude[sensordata[i].maxaltitudelocation():], sensordata[i].highLPO[sensordata[i].maxaltitudelocation():len(sensordata[i].altitude)], 'ro')
	plt.ylabel("LPO")
	plt.xlabel("altitude (feet)")
	plt.tight_layout()
	plt.figure("low sensor %d"%(i))
	plt.subplot(211)
	plt.plot(sensordata[i].altitude[:sensordata[i].maxaltitudelocation()], sensordata[i].lowLPO[:sensordata[i].maxaltitudelocation()], 'ro')
	plt.title("sensor %d ascent, small particles" %(i))
	plt.ylabel("LPO")
	plt.xlabel("altitude (feet)")
	plt.subplot(212)
	plt.plot(sensordata[i].altitude[sensordata[i].maxaltitudelocation():], sensordata[i].lowLPO[sensordata[i].maxaltitudelocation():len(sensordata[i].altitude)], 'ro')
	plt.ylabel("LPO")
	plt.xlabel("altitude (feet)")
	plt.title("sensor %d descent, small particles" %(i))
	plt.tight_layout()
plt.show()

'''
for thing in sensors[1]:
	if thing == "high":
		for stuff in sensors["1"][thing]:
			print(stuff[5])
			print(stuff[0])
			low.setdefault("altitude", []).append(stuff[5])
			low.setdefault("LPO", []).append(stuff[0])
plt.plot([float(x) for x in low["altitude"]],[int(x) for x in low["LPO"]], 'ro')	
plt.show()
'''
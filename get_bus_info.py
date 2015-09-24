import csv
import json
import sys
import urllib2

#def main():
# Define a variable to hold the source URL.
# In this case we use the MTA bus route data.
# key:76ec34a7-40e4-41db-ba87-af22e5241e27

if __name__=='__main__':
	url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" %(sys.argv[1], sys.argv[2].upper())
	urlData = urllib2.urlopen(url)
	data = json.load(urlData)

	BusAc = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
	BusLine = BusAc[0]["MonitoredVehicleJourney"]["PublishedLineName"]
	print "Bus Line : %s" %(BusLine)

	index = 0 

	print 'Latitude, ' 'Longitude, ' 'Stop Name, ' 'Status'

	with open(sys.argv[2], 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(('Latitude', 'Longitude', 'Stop Name', 'Status'))

		for Bus in BusAc:
			Latitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
			Longitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]

			if Bus["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
				Stop = 'N/A'
				Status = 'N/A'
			else:
				Stop = Bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
				Status = Bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]['Extensions']['Distances']["PresentableDistance"]
				index += 1
			row = [Latitude, Longitude, Stop, Status]
			writer.writerow(row)

			print '%s, %s,%s, %s' % (Latitude, Longitude, Stop, Status)


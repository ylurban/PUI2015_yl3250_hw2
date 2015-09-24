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
for Bus in BusAc:
	BusNumber = index
	Latitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
	Longitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
	index += 1
	print "Bus %s is at Latitude %s and Longitude %s" %(BusNumber, Latitude, Longitude)

print "Number of Active Buses: %s" %(index)



	
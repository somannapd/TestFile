import xml.etree.ElementTree as ET
import csv
tree = ET.parse("info.xml")
root = tree.getroot()
resident_data = open('info.csv','w') 
csvwriter = csv.writer(resident_data)
resident_head = []

count = 0
for member in root.findall('resident'):
	resident = []
	address_list=[]
	if count == 0:
		name = member.find('name').tag
		resident_head.append(name)
		number=member.find('number').tag
		resident_head.append(number)
		Address=member[2].tag
		resident_head.append(Address)
		csvwriter.writerow(resident_head)
		count=count+1

	name=member.find('name').text
	resident.append(name)
	number=member.find('number').text
	resident.append(number)
	Address = member[2][0].text
	address_list.append(Address)
	city = member[2][1].text
	address_list.append(city)
	
	resident.append(address_list)
	csvwriter.writerow(resident)
resident_data.close()

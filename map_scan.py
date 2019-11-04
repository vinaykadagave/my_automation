#!/bin/python	
import xml.dom.minidom
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta



def my_scan_report(scan_ref):
	ref_num=str(scan_ref)
	res_url="https://qualysapi.qualys.com/msp/map_report.php?ref="+ref_num
	print( "scan result URL Is :" + res_url)
	headers = {
			'content-type': 'text/json',
			}
	scan_response = requests.get(res_url, headers=headers, auth=('username', 'password'))
	with open('report.xml','w') as fd:
		fd.write(scan_response.text)
	tree = ET.parse('report.xml')
	root = tree.getroot()
	count=0
	for IP in root.findall('IP'):
		ip_list=(IP.attrib['value'])
		#print(ip_list)
		count+=1
	print("total number of IP's found: ")
	print("total number of IP's found: ")
	print(count)


def scan_ref():
	search_date = datetime.today().date() - timedelta(days=10)
	headers = {
		'content-type': 'text/json',
		}
	response = requests.get('https://qualysapi.qualys.com/msp/map_report_list.php', headers=headers, auth=('ydee_vk2', 'KLurD47owR'))

	with open('map.xml','w') as fd:
		fd.write(response.text)

	#tree = ET.parse('map.xml')
	tree = ET.parse('map.xml')
	root = tree.getroot()

	#for child in root.iter('MAP_REPORT'):
	#   print(child.tag, child.attrib)
	
	print "System Date - 10 days : " 
	print search_date
	print "______"
	
	for MAP_REPORT in root.findall('MAP_REPORT'):	
		tag_data=MAP_REPORT.attrib['date']
		scan_date=tag_data[:10]
		scan_date=datetime.strptime(scan_date, '%Y-%m-%d').date()	
	#print(type(scan_date))
	#map_date=datetime.strptime(tag_data,'%d-%m-%y %H:%M:%S').date()
	#print (scan_date)
	
		if scan_date <=search_date:
			print " no mapscan found" 
			break
		else:
			print ('Map scan report details.')
			print (MAP_REPORT.attrib['ref'],MAP_REPORT.attrib['date'])
			break
			
	scan_ref_num=MAP_REPORT.attrib['ref']
	print ("scan_ref number after-" + scan_ref_num)
	my_scan_report(scan_ref_num)

def main():
	scan_ref()

main()
		


import csv
import codecs
from datetime import datetime
from bs4 import BeautifulSoup

#open and parser export
pocket_list=codecs.open("ril_export.html", 'r')
soup = BeautifulSoup(pocket_list, "html.parser")

#create csv and write header
pocket_csv = csv.writer(open("pocket.csv", "w"))
pocket_csv.writerow(["status", "title", "href", "domain","date_added", "time_added", "day_of_week_added", "tags"])

#iterate through each link
links = soup.findAll('a')
for link in links:
	status = link.parent.parent.findPreviousSibling('h1').get_text()
	title = link.contents[0].encode('ascii','ignore')
	href = link['href'].encode('ascii','ignore')
	domain = href.replace("https","").replace("http","").replace("www.","").replace("://","")
	domain = domain.split("/", 1)[0]
	tags = link['tags'].encode('ascii','ignore')
	
	#get epoch time and split
	time_added = float(link['time_added'])
	date_added = datetime.fromtimestamp(time_added).strftime("%x")
	time_added = datetime.fromtimestamp(time_added).strftime("%X")
	day_of_week_added = datetime.fromtimestamp(time_added).strftime("%A")
	
	#write row to file
	row = (status, title, href, domain, date_added, time_added, day_of_week_added, tags)
	pocket_csv.writerow(row)

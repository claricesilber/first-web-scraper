import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html' 
#may have to change url

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

table = soup.findAll('table')[0]
#change table you're working with 

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
        if cell.find('a'):
        	list_of_cells.append("http://www.tdcj.state.tx.us/death_row/" + cell.find('a')['href']) #change this too
    list_of_rows.append(list_of_cells)

outfile = open("./executions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(['date', 'n/a', 'url','last_name','first_name','tdcj_number','dob','race','date_received','county']) #will need to change 
writer.writerows(list_of_rows)
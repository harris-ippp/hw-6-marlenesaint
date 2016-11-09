#start with imports
import requests
import csv
from bs4 import BeautifulSoup

#we need to assign the election_id to this url to download every dataset
url_template = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

#use loop to look in our election_id file created in last question
#split the two variables (year and election id) from each line
#generate the different urls using the split election id
#use resp to get every url
#use another loop to name the files with the year and the extension csv
#write the file for each election

for line in open("ELECTION_ID"):
    parts = line.split() # split line into parts
    idl=parts[1]
    year=parts[0]
    url = url_template.format(idl)
    resp = requests.get(url)
    for i in year:
        file_name = year +".csv"
        with open(file_name, "w") as out:
            out.write(resp.text)

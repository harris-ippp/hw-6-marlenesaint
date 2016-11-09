#start with imports
import requests
from bs4 import BeautifulSoup

#this is the link that we need to use soup in
link = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"

#regular commands to get the source
req = requests.get(link)
html = req.content
soup = BeautifulSoup(html, "html.parser")

#we have to create a file "ELECTION_ID
# look in our soup source for tr and election_item, where we identified that the id appears
#locate the id, split with - and take the third element (the id)
# locate the year by searching for td and first, take the first elements
# write the year and the id_number in ELECTION_ID 
with open ("ELECTION_ID", "w") as out:
    for result in soup.find_all("tr", "election_item"):
        id_number = result["id"].split("-")[2]
        year = result.find("td", "first").contents[0]
        out.write("{} {}\n".format(year, id_number))

from bs4 import BeautifulSoup
import urllib.request
import csv

# Define the url being scraped
urlpage =  'https://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

# Make the connection to the webpage and parse the html using BeautifulSoup, storing the object in the variable ‘soup’
page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')

# soup variable at this stage should return the full parsed html of the webpage we have requested
print(soup)

# find results within table
table = soup.find('table', attrs={'class': 'tableSorter'})
results = table.find_all('tr')
print('Number of results', len(results))

# create and write headers to a list 
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])
print(rows)

# loop over results
for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data 
    if len(data) == 0: 
        continue
    # write columns to variables
    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    yearend = data[3].getText()
    salesrise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comments = data[7].getText()







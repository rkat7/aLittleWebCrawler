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
    
# Cleaning the data
''' If we print out the variable company, the text not only contains the name of the company but also a description. If we then print out sales, it contains unwanted characters such as footnote symbols that would be useful to remove.'''
    # extract description from the name
    companyname = data[1].find('span', attrs={'class':'company-name'}).getText()    
    description = company.replace(companyname, '')
    
    # remove unwanted characters
    sales = sales.strip('*').strip('†').replace(',','')
    
# Now scrape the url from each table and save it as a variable

    # go to link and extract company website
    url = data[1].find('a').get('href')
    page = urllib.request.urlopen(url)
    # parse the html 
    soup = BeautifulSoup(page, 'html.parser')
    # find the last result in the table and get the link
    try:
        tableRow = soup.find('table').find_all('tr')[-1]
        webpage = tableRow.find('a').get('href')
    except:
        webpage = None
        
        
 # Add each result to the list row
     # write each result to rows
    rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])
print(rows)


# Writing to an output file
# Create csv and write rows to output file
with open('techtrack100.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
    
    
    
-----------------------------------------------------------------------------------------------------------------------------------------






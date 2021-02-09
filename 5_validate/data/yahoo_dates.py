##########################################################
# Extract Date from Press Release Pages from Yahoo Finance
##########################################################

# libraries used
import os
import re
import bs4 as bs
import csv


# Input file
articleList = []
with open('article_list.txt', 'r') as f:
	for i in f:
		articleList.append(i)
		
print(len(articleList))

# empty lists
idList = []
titleList = []
dateList = []

# loop through articles to extract title and date
for art in articleList:
    art = art.rstrip()
    print(art)
    id = re.search('yahoo_scrape/(.+?)\.html', art).group(1)
    id = id.split("/")[1]
    print(id)

    try:
        source = open(art, 'r', encoding= 'utf-8')
        soup = bs.BeautifulSoup(source, "lxml")

        # find title
        title = soup.find('h1', {'data-test-locator': "headline"})
        title = title.text
        print(title)
        titleList.append(title)

        # find date
        datetime = soup.find('time').attrs['datetime']
        #date = datetime.split('T')[0]
        print(datetime)
        dateList.append(datetime)

        # save id
        idList.append(id)
       
    except:
        print('Did not open')



#####save data to a csv file
with open('yahoo_dates.csv', 'w', encoding='UTF-8', newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(("ID", "Tile", "Date"))
    writer.writerows(zip(idList, titleList, dateList))

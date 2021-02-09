###############################################################
# Extract Data and Save Press Release Pages from Yahoo Finance
###############################################################

# libraries used
import os
import re
import bs4 as bs
import csv
import requests
import time

coList = ["AAPL.html", "AMZN.html", "ARTW.html", "EVGN.html", "FB.html", "GOOG.html", "MSFT.html"]

print(len(coList))

# empty lists
tickerList = []
idList = []
titleList = []
siteList = []
sourceList = []
dateList = []
filepathList = []


id = 0
path_beg = "blank"

for co in coList:
    co = co.rstrip()
    print(co)
    name = str(co)[:-5]
    print(name)

    # create directories for each ticker
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = str(dir_path) + "/" + str(name)
    print(dir_path)

    try:
        os.mkdir(dir_path)
    except OSError:
        print ("Creation of the directory %s failed" % dir_path)
    else:
        print ("Successfully created the directory %s " % dir_path)

    # collect data
    try:
        source = open(co, 'r', encoding= 'utf-8')
        soup = bs.BeautifulSoup(source, "lxml")
        #text = soup.find('div', {'class': "eiReviewDetails__EIReviewDetailsPageStyles__reviewDetailsPage singleReview mb-sm mb-md-std"})

        # find the html table with the press releases
        press = soup.find('div',{'id':"summaryPressStream-0-Stream"})
        articles = press.findAll('li',{'class':"js-stream-content Pos(r)"})
        print(len(articles))

        for i in articles:
            try:
              
                # title
                title = i.find('h3', {'class': 'Mb(5px)'})
                title = title.text
                print(title)
                titleList.append(title)

                # website
                website = i.find('a', href=True)
                website = website['href']
                website = 'https://finance.yahoo.com' + str(website)
                print(website)
                siteList.append(website)

                # save website
                path_prev = path_beg
                path_beg = dir_path + "/"

                if path_prev == path_beg:
                    id = id + 1
                else:
                    id = 1
                path = path_beg + str(name) + str(id) + ".html"
                print(path)
                filepathList.append(path)
                id_name = str(name) + str(id)
                idList.append(id_name)
                time.sleep(3)
                page = requests.get(website)
                with open(path, "wb") as f:
                    f.write(page.content)
                
                # source
                source_all = i.find('div', {'class': 'C(#959595) Fz(11px) D(ib) Mb(6px)'})
                source = source_all.find_next('span')
                source = source.text
                print(source)
                sourceList.append(source)

                # date
                date = source_all.find_next('span').find_next('span')
                date = date.text
                print(date)
                dateList.append(date)

                # company
                tickerList.append(name)

            except:
                print("ad")

       
    except:
        print('Did not open')




#####save data to a csv file
with open('yahoo_main.csv', 'w', encoding='UTF-8', newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(("ID", "Ticker", "Tile", "Site", "Source", "Date", "File Path"))
    writer.writerows(zip(idList, tickerList, titleList, siteList, sourceList, dateList, filepathList))

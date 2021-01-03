from bs4 import BeautifulSoup
import requests
import string

#Prompt user to enter NYSE stock symbol and convert it to full URL
#The program will continually ask the user for symbols after displaying the data
while(True):
    infoDict = {}
    peRatio = ''
    strippedList = []
    symbol = input("Enter an NYSE symbol (enter 1 to quit): ")
    if(symbol == '1'):
        break

    url = 'https://finance.yahoo.com/quote/{0}/'.format(symbol)
    url2 = 'https://www.multpl.com/s-p-500-pe-ratio'
#Get the source codes using requests
    source = requests.get(url).text
    source2 = requests.get(url2).text
#Parse the source codes using BeautifulSoup and lxml parser
    soup = BeautifulSoup(source, 'lxml')
    soup2 = BeautifulSoup(source2, 'lxml')
#Find stock name to be printed later
    name = soup.find('h1', {'data-reactid' : '7'})
#Select all table data from the parsed code (where the stock info is actually contained)
    info = soup.select('table td')
#Find and select average PE ratio for the S&P500
    averagePE = soup2.find('div', {'id' : 'current'})
    averagePE = averagePE.text.split('\n')
    averagePE = averagePE[3]
#Add stock info to a dictionary for easier calling of values.
    for i in range(len(info)):
        if (i%2 == 0):
            info[i] = info[i].text.replace(' ', '')
            infoDict[info[i]] = None
        else:
            infoDict[info[i-1]] = info[i].text
#Access our table data to find the P/E Ratio for the selected stock
#Also added error handling here for potential invalid stock symbol input
    try:
        peRatio = info[21].text
#Quick logic to decide whether P/E Ratio is good or bad (compares it to S&P500 average).

        peRatio = peRatio.replace(",","")
        if (float(peRatio) >= (float(averagePE) + 1.5)):
            peRatio = peRatio + ' - Overvalued'
        elif (float(peRatio) <= (float(averagePE) - 1.5)):
            peRatio = peRatio + ' - Cheap'
        else:
            peRatio = peRatio + ' - Average'
#Finally, display the information.
#I use dictionaries to make it a little more human-readable
        print()
        print(name.text)
        print("Previous Close: " + infoDict['PreviousClose'])
        print("Bid Value: " + infoDict['Bid'])
        print("Ask Value: " + infoDict['Ask'])
        print("Average Volume: " + infoDict['Avg.Volume'])
        print("Market Cap: " + infoDict['MarketCap'])
        print("\nP/E Ratio: " + peRatio + "\nAverage PE Ratio is: " + averagePE)
    except Exception:
        print('You must enter a valid symbol!' + '\n')
    print('\n')

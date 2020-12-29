from bs4 import BeautifulSoup
import requests

#Prompt user to enter NYSE stock symbol and convert it to full URL
#The program will continually ask the user for symbols after displaying the data
while(True):
    peRatio = ''
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
#Access our table data to find the P/E Ratio for the selected stock
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
#Finally, display the information and include some error handling for invalid stock symbols
#I may need to find a more intuitive way to do this, for now this gets the job done:
        print()
        print(name.text)
        print("Previous Close: " + info[1].text)
        print("Bid Value: " + info[5].text)
        print("Ask Value: " + info[7].text)
        print("Average Volume: " + info[13].text)
        print("Market Cap: " + info[17].text)
        print("\nP/E Ratio: " + peRatio)
    except Exception:
        print('You must enter a valid symbol!' + '\n')
    print('\n')

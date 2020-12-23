from bs4 import BeautifulSoup
import requests

#Prompt user to enter NYSE stock symbol and convert it to full URL
#The program will continually ask the user for symbols after displaying the data
while(True):
    symbol = input("Enter an NYSE symbol (enter 1 to quit): ")
    if(symbol == '1'):
        break

    url = 'https://finance.yahoo.com/quote/{0}/'.format(symbol)
    #Get the source code using requests
    source = requests.get(url).text
    #Parse the source code using BeautifulSoup and lxml parser
    soup = BeautifulSoup(source, 'lxml')
    #Find stock name to be printed later
    name = soup.find('h1', {'data-reactid' : '7'})
    #Select all table entries from the parsed code (where the stock info is actually contained)
    info = soup.select('table td')
    #Finally, display the information and include some error handling for invalid stock symbols
    #I may need to find a more intuitive way to do this, for now this gets the job done:
    print()
    try:
        print(name.text)
        print("Previous Close: " + info[1].text)
        print("Bid Value: " + info[5].text)
        print("Ask Value: " + info[7].text)
        print("Average Volume: " + info[13].text)
        print("Market Cap: " + info[17].text)
    except Exception as e:
        print('You must enter a valid symbol!')
    print('\n')

from bs4 import BeautifulSoup
import requests

#Prompt user to enter NYSE stock symbol and convert it to full URL
#I hope to add error checking in the future to ensure a valid symbol
symbol = input("Enter a valid NYSE symbol: ")
url = 'https://finance.yahoo.com/quote/{0}/'.format(symbol)
#Get the source code using requests
source = requests.get(url).text
#Parse the source code using BeautifulSoup and lxml parser
soup = BeautifulSoup(source, 'lxml')
#Select stock name to be printed later
name = soup.find('h1', {'data-reactid' : '7'})
#Select all table entries from the parsed code (this is where the info is actually contained)
info = soup.select('table td')
#Display the Information
#I may need to find a more intuitive way to do this, for now this works:
print()
print(name.text)
print("Previous Close: " + info[1].text)
print("Bid Value: " + info[5].text)
print("Ask Value: " + info[7].text)
print("Average Volume: " + info[13].text)
print("Market Cap: " + info[17].text)

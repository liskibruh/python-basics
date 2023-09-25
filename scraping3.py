import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=iphone+11&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

#youtube_link = soup.find_all('div',class_='style-scope ytd-rich-grid-row')
youtube_link = soup.find_all('div',{'class':'_4rR01T'})

count = 0
for each_link in youtube_link:
	print(each_link)
	count+=1

print(count)
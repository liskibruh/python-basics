import requests
from bs4 import BeautifulSoup

url = "https://www.daraz.pk/catalog/?q=iphone+11&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e349370eJrDN"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

#youtube_link = soup.find_all('div',class_='style-scope ytd-rich-grid-row')
youtube_link = soup.find_all('div',{'class':'title--wFj93'})

count = 0
for each_link in youtube_link:
	print(each_link)
	count+=1

print(count)
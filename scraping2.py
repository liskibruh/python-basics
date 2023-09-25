import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/@PW-Foundation/videos"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

#youtube_link = soup.find_all('div',class_='style-scope ytd-rich-grid-row')
youtube_link = soup.find_all('a')

count = 0
for each_link in youtube_link:
	print(each_link)
	count+=1

print(count)
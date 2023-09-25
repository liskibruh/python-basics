import requests
from bs4 import BeautifulSoup

url = "https://www.electronic-festivals.com/event/i-am-hardstyle-germany"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

youtube_link = soup.find('iframe')['src']
print(youtube_link)
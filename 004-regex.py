import requests
import re

url = 'https://www.youtube.com/@PW-Foundation/videos'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
'Accept-Language': 'en-US,en;q=0.9'
}
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

response = requests.get(url, headers=headers)
response_text = response.text

#thumbnails
pattern1 = re.compile(r"https://i.ytimg.com/vi/[A-Za-z0-9_]{11}/[A-Za-z0-9_]{9}.jpg\?sqp=-[A-Za-z0-9_]{45}")

#links
pattern2 = re.compile(r"watch\?v=[A-Za-z0-9_-]{11}")

#view count
pattern3 = re.compile(r"[0-9]+(\.[0-9]+)?[a-zA-Z]*K views")

#time posted
pattern4 = re.compile(r"\d+ (hours|days|weeks|years) ago")


count = 0

matches1 = pattern1.finditer(response_text)
matches2 = pattern2.finditer(response_text)
matches3 = pattern3.finditer(response_text)
for match1,match2,match3 in zip(matches1,matches2,matches3):
	print(match1[0])
	print(match2[0])
	print(match3[0])
	count+=1
	
print(count)
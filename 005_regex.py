import logging
import requests
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(BASE_DIR, "logs.log") , level=logging.INFO)

url = 'https://www.youtube.com/@PW-Foundation/videos'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
'Accept-Language': 'en-US,en;q=0.9'
}

try:
	#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
	logging.info("Requesting HTML...")
	response = requests.get(url, headers=headers)
	response_text = response.text

	#thumbnails
	logging.info("Finding thumbnails...")
	vid_thumbnails = re.findall(r"https://i.ytimg.com/vi/[A-Za-z0-9_-]{11}/[A-Za-z0-9_]{9}.jpg\?sqp=-[A-Za-z0-9_]{45}", response_text)

	#links
	logging.info("Finding links...")
	vid_links = re.findall(r"watch\?v=[A-Za-z0-9_-]{11}", response_text)

	#view count
	logging.info("Finding view counts...")
	pattern3 = re.compile(r"[0-9]+(\.[0-9]+)?[a-zA-Z]*K views")

	#time posted
	logging.info("Finding videos age...")
	pattern4 = re.compile(r"\d+ (minutes|hours|hour|days|day|weeks|week|years|year) ago")

	matches1 = pattern3.finditer(response_text)
	matches2 = pattern4.finditer(response_text)

	vid_viewcounts=[]
	vid_ages=[]
	count = 0
	for match1,match2 in zip(matches1,matches2):
		vid_ages.append(match2[0])
		vid_viewcounts.append(match1[0])

	logging.info("Storing thumbnails...")
	thumbnails = vid_thumbnails[0:20:2]
	logging.info("Storing links...")
	links = vid_links[0:10:1]
	logging.info("Storing viewcounts...")
	viewcounts=vid_viewcounts[0:20:2]
	logging.info("Storing videos age...")
	ages=vid_ages[0:20:2]

	data_dict = {'thumbnails': thumbnails, 'links': links, 'viewcounts': viewcounts, 'ages': ages}

	#print(data_dict['links'])
	for thumbnail,link,viewcount,age in zip(thumbnails,links,viewcounts,ages):
	 	print(thumbnail)
	 	print(link)
	 	print(viewcount)
	 	print(age)
	 	print()

	logging.shutdown()

except Exception as e:
	print(e)
	logging.error(e)

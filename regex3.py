import re


# pattern2 = re.compile(r"https://i.ytimg.com/vi/[A-Za-z0-9_]{11}/[A-Za-z0-9_]{9}.jpg\?sqp=-[A-Za-z0-9_]{45}")
# pattern3 = re.compile(r"watch\?v=[A-Za-z0-9_-]{11}")
#pattern6 = re.compile(r"[0-9]+(\.[0-9]+)?[a-zA-Z]*K views")
# pattern7 = re.compile(r"\d+ (hours|days|weeks|years) ago")


count = 0
with open('page_source.txt','r',encoding="utf-8") as file:
	content = file.read()

	#matches = pattern6.finditer(content)

	vid_thumbnails = re.findall(r"https://i.ytimg.com/vi/[A-Za-z0-9_]{11}/[A-Za-z0-9_]{9}.jpg\?sqp=-[A-Za-z0-9_]{45}", content)
	thumbnails = vid_thumbnails[:10]
	vid_links = re.findall(r"watch\?v=[A-Za-z0-9_-]{11}", content)
	links = vid_links[0:20:2]
	

	for link in links:
		print(link)
		count+=1
	print(count)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def lauchpage():
	driver.get("https://www.youtube.com/@PW-Foundation/videos")

	try:
		vid_details = WebDriverWait(driver,10).until(
			EC.presence_of_element_located((By.ID, "contents"))
			)
	except:
		driver.quit()
	return vid_details.text
#######################################################################

vid_info = lauchpage()

data_dict = {}
line_num = 1
all_lines=[]

for line in vid_info.split('\n'):
	print(line)
	if ':' in line:
		pass
	else:
		all_lines.append(line)

for line in all_lines:
    if line_num % 3 == 1:
        record_dict = {}

    if line_num % 3 == 1:
        record_dict['title'] = line

    elif line_num % 3 == 2:
        record_dict['views'] = line

    elif line_num % 3 == 0:
        record_dict['posting_time'] = line
        data_dict[len(data_dict)] = record_dict

    line_num+=1

df = pd.DataFrame.from_dict(data_dict, orient='index')
df.to_csv('pwskills_youtube_vid_details.csv')
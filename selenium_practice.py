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
	#print(vid_details.text)
	#print(driver.page_source)
	#while True:
		#pass
	return vid_details.text

vid_info = lauchpage()

print(type(vid_info))

# initialize an empty dictionary to hold the data
data_dict = {}

# initialize a counter to keep track of the current line number
line_num = 1

for line in vid_info.split('\n'):

	# if this is the first line of a new record, initialize a dictionary to hold the data for that record
    if line_num % 4 == 1:
        record_dict = {}

    # add the time data to the current record dictionary
    if line_num % 4 == 1:
        record_dict['time'] = line

    # add the title data to the current record dictionary
    elif line_num % 4 == 2:
        record_dict['title'] = line

    # add the views data to the current record dictionary
    elif line_num % 4 == 3:
        record_dict['views'] = line

    # add the posting time data to the current record dictionary, and add the completed record dictionary to the overall data dictionary
    elif line_num % 4 == 0:
        record_dict['posting_time'] = line
        data_dict[len(data_dict)] = record_dict

    # increment the line number counter
    print(f'Line No. {line_num}: {line}')
    line_num += 1

	
	#i+=1

#print(data_dict)
# create a pandas DataFrame from the data_dict
#df = pd.DataFrame.from_dict(data_dict, orient='index')

#df.to_csv('pwskills_youtube_vid_details.csv')
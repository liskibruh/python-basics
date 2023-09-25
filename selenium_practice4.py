from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/@PW-Foundation/videos")

try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "contents"))
        )
    each_vid_main = main.find_elements_by_tag_name("ytd-rich-item-renderer")

    for each_vid in each_vid_main:
        thumbnail = each_vid.find_elements_by_class("yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded")
        print(thumbnail)

except:
    driver.quit()
#######################################################################
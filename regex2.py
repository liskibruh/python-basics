import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

text_to_search = """https://i.ytimg.com/vi/nX5ONgCdLcc/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBaa_KLfKyYbUYRsb5xf0YCp1YrlQ
https://i.ytimg.com/vi/AM2Dt7cNebw/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBJHWHabeJ94dcUDlDDNfvQxnUfJg 
https://i.ytimg.com/vi/hC86u4g6QPk/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD5AeHXmdOF3J-FoFIAYtmfh28ciQ
https://i.ytimg.com/vi/7O5MY8Y1JCE/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBH2cIH3mp1fEKJja5KVXiwRP3p4w
https://i.ytimg.com/vi/pXjLbNAa_ag/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCen1qfPg4ypFCiezVWQrqIpEEbug
https://i.ytimg.com/vi/ZdyGE7nwItI/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBhZJ3imOSJhmg15nJBezmqvVQUAg
"""

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
# driver.get("https://www.youtube.com/@PW-Foundation/videos")

# content = driver.page_source

# content_new = str(content)
# print((content_new))
pattern = re.compile(r"https://i.ytimg.com/vi/(\w|\d){11}/(\w|\d){9}.jpg\?sqp=-(\w|\d){45}==&rs=(\w|\d|-){34}")
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

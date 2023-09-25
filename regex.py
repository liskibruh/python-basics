import re

text_to_search = """
Data Science Masters course is highly curated and 
uniquely designed according to the latest industry 
standards. This program instills students the skills 
essential to knowledge discovery efforts to identify 
standard, novel, and truly differentiated solutions 
and decision-making, including skills in managing, 
querying, analyzing, visualizing, and extracting 
meaning from extremely large data sets. This trending 
program provides students with the statistical, 
mathematical and computational skills needed to meet 
the large-scale data science challenges of today's 
professional world. You will learn all the stack 
required to work in data science industry including 
cloud infrastructure and real-time industry projects. 
This course will be taught in Hindi language. coreyms.com
"""

text_to_search2 = """
12345667889
313-423-5435
325.235.6534
800.235.6534
900.235.6534
123*342*5423
"""

text_to_search3 = """https://i.ytimg.com/vi/nX5ONgCdLcc/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBaa_KLfKyYbUYRsb5xf0YCp1YrlQ
https://i.ytimg.com/vi/AM2Dt7cNebw/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBJHWHabeJ94dcUDlDDNfvQxnUfJg 
https://i.ytimg.com/vi/hC86u4g6QPk/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD5AeHXmdOF3J-FoFIAYtmfh28ciQ
https://i.ytimg.com/vi/7O5MY8Y1JCE/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBH2cIH3mp1fEKJja5KVXiwRP3p4w
https://i.ytimg.com/vi/pXjLbNAa_ag/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCen1qfPg4ypFCiezVWQrqIpEEbug
https://i.ytimg.com/vi/ZdyGE7nwItI/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBhZJ3imOSJhmg15nJBezmqvVQUAg
"""

text_to_search4 = """
cat
pat
mat
bat
"""

text_to_search5="""
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

pattern = re.compile(r"https://i.ytimg.com/vi/(\w|\d){11}/(\w|\d){9}.jpg\?sqp=-(\w|\d){45}==&rs=(\w|\d|-){34}")
#pattern = re.compile(r'[^b]at')
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

#pattern = re.compile(r'[1-5]')
matches = pattern.finditer(text_to_search3)

for match in matches:
	print(match)


print(len("https://i.ytimg.com/vi/nX5ONgCdLcc/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBaa_KLfKyYbUYRsb5xf0YCp1YrlQ"))
print(279-140)
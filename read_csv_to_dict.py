import csv

csv_filename = 'pwskills_youtube_vid_details - Copy.csv'

details=[]
with open(csv_filename,'r') as data:
   for line in csv.reader(data):
        mydict = {"Index": line[0], "Title": line[1], "Views": line[2], "Time_since_posted": line[3]}
        details.append(mydict)

print(details)
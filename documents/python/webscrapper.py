import requests
from bs4 import BeautifulSoup as bs
for i in range(1,100):
	comic_num = i
	xkcd_url = "https://xkcd.com/"+str(comic_num)
	comic = requests.get(xkcd_url)
	parser=bs(comic.content,features="html.parser")
	url = parser.find("div",{"id":"comic"})
	image_url = url.img["src"]
	image_url = "https:"+ image_url
	image_data = requests.get(image_url)
	extension = image_url.split(".")
	extension = extension[len(extension)-1]
	with open(r"C:\Users\Chirag Nagpal\Pictures\Comics\comic_"+str(comic_num)+"."+extension,"wb") as comic_file: 
		comic_file.write(image_data.content)


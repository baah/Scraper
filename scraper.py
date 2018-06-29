from bs4 import BeautifulSoup
import requests

url = "https://store.steampowered.com/search/?category1=998,996&specials=1"

r = requests.get(url)
# Gets the html text of the website
rText = r.text

soup = BeautifulSoup(rText, "html.parser")

samples = soup.find_all("span", class_="title")
count = 0;

for sample in samples:
	print(sample.text)
	count = count + 1
	if count == 10:
		break


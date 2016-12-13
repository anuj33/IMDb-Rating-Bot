import requests
from bs4 import BeautifulSoup

title = raw_input("Enter Movie name to search: ") 

s="+".join(title.split())


f_url = 'http://www.imdb.com/find?q='
url=f_url+s+'&s=all'

var = requests.get(url)


soup = BeautifulSoup(var.content)

x = soup.find("td", {"class": "result_text"})
m = x.find("a")['href']


new_url = 'http://www.imdb.com' + m 

content = requests.get(new_url)
soup = BeautifulSoup(content.content)


x = soup.find("div", {"class": "title_wrapper"})

c = x.findChildren()[0]
print "Movie Name: %s" % c.text

c = soup.find("div", {"class":"ratingValue"})
print "IMDb: %s" % c.text 

c = soup.find_all("div", {"class":"credit_summary_item"})



for tag in c:
	if tag.find("span")['itemprop'] == 'director':
		print tag.text,

	if tag.find("span")['itemprop'] == 'creator':
		print tag.text,

	if tag.find("span")['itemprop'] == 'actors':
		print tag.text 
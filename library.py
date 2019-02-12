import urllib
from bs4 import BeautifulSoup
quote_page = 'https://www.dur.ac.uk/library/'
page = urllib.request.urlopen(quote_page)
data=page.read()
sibling_soup = BeautifulSoup(data, 'html.parser')
tag=int(sibling_soup.svg.text)
print(tag)
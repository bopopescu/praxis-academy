from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.detik.com/search/searchall?query=sepak+bola&siteid=2"
driver = webdriver.Firefox()
driver.get(url)
content = driver.page_source
driver.quit()

soup = BeautifulSoup(content , 'html.parser')
title = soup.findAll('h2', attrs={'class':'title'})
sp = soup.findAll('span', attrs={'class':'date'})
count = 0 
for x in range(0, len(title)):
    count += 1
    print("{0}. {1}\n -{2}".format(count, title[x].text.strip(), sp[x].text.strip()))
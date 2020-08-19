from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml
# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains 

print("=====================Starting ===========")

base_url = "https://honolulu.craigslist.org/search/oah/sss?query=cars&sort=rel"
page = requests.get(base_url)
print(page.status_code)
if page.status_code == requests.codes.ok:
	bs = BeautifulSoup(page.text, 'lxml')
	print(bs.head, bs.title)

containing_div = bs.find('div', class_='content')
list_of_listings = containing_div.find('ul', class_='rows')
first_posting = list_of_listings.find('li', class_='result-row')
all_postings = list_of_listings.find_all('li', class_='result-row')
listings = bs.find('div', class_='content').find('ul',class_='rows').find_all('li')
#Dictionary to hold the data
data = {
	'Title': [],
	'Price': [],
	}
print("First title= ", all_postings[0].find('a',class_='result-title hdrlnk').text)
print("First price= ", all_postings[0].find('span', class_='result-price').text)

for posting in all_postings:
	title = posting.find('a', class_='result-title hdrlnk').text
	if title:
		data['Title'].append(title)
	else:
		data['Title'].append('N/A')
	price = posting.find('span', class_='result-price').text
	
	if price:
		data['Price'].append(price)
	else:
		data['Price'].append('N/A')
		
df = pd.DataFrame(data, columns=['Title','Price'])
df.index = df.index + 1
print(df)
df.to_csv('hannuslist_postings_file.csv', sep=',', index=False, encoding='utf-8')
print("First page Completed")
print("===================== Starting selenium ===========")
# import webdriver 
from selenium import webdriver 
  
# create webdriver object 
driver = webdriver.Firefox() 
  
# get honolulu.craigslist.org 
driver.get("https://honolulu.craigslist.org/search/oah/sss?query=cars&sort=rel") 
  
driver.implicitly_wait(2)  
element_button = driver.find_element_by_xpath("/html/body/section/form/div[3]/div[3]/span[2]/a[3]")
element_button.click()

get_title = driver.title
print(get_title)
print(driver.current_url)
base_url2 = driver.current_url
page2 = requests.get(base_url2)
if page2.status_code == requests.codes.ok:
	bs2 = BeautifulSoup(page2.text, 'lxml')
containing_div = bs2.find('div', class_='content')
list_of_listings = containing_div.find('ul', class_='rows')
all_postings = list_of_listings.find_all('li',class_='result-row')
data2 = {
	'Title': [],
	'Price': [],
	}
print("page2 first car=   ", all_postings[0].find('a',class_='result-title hdrlnk').text)
print("page2 first price= ", all_postings[0].find('span', class_='result-price').text)	
for posting in all_postings:
	title = posting.find('a', class_='result-title hdrlnk').text
	if title:
		data2['Title'].append(title)
	else: 
		data2['Title'].append('N/A')
	price = posting.find('span', class_='result-price').text	
	if price:
		data2['Price'].append(price)
	else:
		data2['Price'].append('N/A')
			
		
df2 = pd.DataFrame(data2, columns=['Title','Price'])
df2.index = df2.index + 1
print(df2)
df2.to_csv('hannuslist_postings_file2.csv', sep=',', index=False, encoding='utf-8')

	
	


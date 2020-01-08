from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#driver = webdriver.Chrome()



def scrape():
	driver.get("http://www.desitellybox.me/category/colors/bigg-boss-13/")
	headlines = driver.find_elements_by_xpath("//*[contains(text(), 'Episode Watch Online')]")[0].click()
	time.sleep(5)
	headlines = driver.find_elements_by_xpath("//a[contains(text(), 'Bigg Boss') and contains(text(), '13')]")
	links = []
	for headline in headlines:
		link = (headline.get_attribute("href"))
		if (link.lower().find("vk") > 0 ):
			links.append(link)
			print (link)

	if(len(links) == 0):
		return 'Latest Episode not available yet'
	link = links[-2]
	eyeD = link[link.find("=")+1: len(link)]
	print (eyeD)
	# paragraphs = driver.find_elements_by_tag_name('p')
	# for p in paragraphs:
	# 	print (p.find_element_by_xpath('.//b').element.get_attribute("text"))

	return ('<iframe src="http://vkprime.com/embed-%s.html" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(eyeD))

def scrapeSecond():
	driver.get("https://www.desitellybox.me/category/and-tv/bhabhiji-ghar-par-hain/")
	headlines = driver.find_elements_by_xpath("//*[contains(text(), 'Episode Watch Online')]")[0].click()
	time.sleep(5)
	headlines = driver.find_elements_by_xpath("//a[contains(text(), 'Bhabhiji Ghar Pe Hai') and contains(text(), 'Hai')]")
	links = []
	for headline in headlines:
		link = (headline.get_attribute("href"))
		if (link.lower().find("vk") > 0 ):
			links.append(link)
			print (link)

	if(len(links) == 0):
		return 'Latest Episode not available yet'
	link = links[0]
	eyeD = link[link.find("=")+1: len(link)]
	linkTwo = links[1]
	eyeDTwo = linkTwo[linkTwo.find("=")+1: len(linkTwo)]
	print (eyeD)
	print (eyeDTwo)
	return (['<iframe src="http://vkprime.com/embed-%s.html" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(eyeD), '<iframe src="http://vkprime.com/embed-%s.html" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(eyeDTwo)])
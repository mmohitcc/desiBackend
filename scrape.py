from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import json
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
#driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#driver = webdriver.Chrome()



def scrape(link):
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	# driver.execute_script("window.open('"+link+"', '_blank')")
	driver.get(link)
	# time.sleep(5)
	headlines = driver.find_elements_by_xpath("//*[contains(text(), 'VKprime')]")[0]
	button = headlines.find_element_by_xpath("..")
	pary = button.find_element_by_xpath("following-sibling::p")
	allvkPrimeLinks = pary.find_elements_by_tag_name("a")
	allLinks = []
	del headlines
	del button
	del pary
	for l in allvkPrimeLinks:
		allLinks.append(l.get_attribute("href"))
	sources = []
	for l in allLinks:
		# print (l)
		# going to the video page
		driver.get(l)
		# frame = driver.find_element_by_xpath("//iframe[contains(@src,'vkprime'])]")
		# grabbing the iframes on the page
		ifras = driver.find_elements_by_tag_name("iframe")
		# print("found frames \n")
		for ifra in ifras:
			# print("checking frames")
			# looking for iframes with src containing vk
			if(ifra.get_attribute("src").find("vk") > 0):
				sources.append(ifra.get_attribute("src"))
				


	# for source in sources:
	# 	# print(source)
	
	frames = []
	for source in sources:
		frames.append('<iframe src="%s" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(source))
	driver.quit()
	return (frames)

def scrapeDailyMotion(link):
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	# driver.execute_script("window.open('"+link+"', '_blank')")
	driver.get(link)
	# time.sleep(5)
	allvkPrimeLinks = []
	btns = driver.find_elements_by_class_name("btn_green")
	for b in btns:
		a = b.find_elements_by_xpath("//*[contains(text(), 'Dailymotion')]")
		if(len(a) > 0):
			# print("should have the one with daily motion")
			button = a[0].find_element_by_xpath("..")
			# print (button.get_attribute('innerHTML'))
			pary = button.find_element_by_xpath("following-sibling::p")
			allvkPrimeLinks = pary.find_elements_by_tag_name("a")
	# headlines = btns.find_elements_by_xpath("//*[contains(text(), 'Dailymotion')]")[0]
	
	
	
	allLinks = []
	# del headlines
	# del button
	# del pary
	for l in allvkPrimeLinks:
		allLinks.append(l.get_attribute("href"))
		print(allLinks.append(l.get_attribute("href")))
	sources = []
	count = 0
	driver.quit()
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	for l in allLinks:
		# if(count % 2 == 0):
		driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
		# print (l)
		# going to the video page
		# print("printing l")
		# print(l)
		driver.get(l)
		# frame = driver.find_element_by_xpath("//iframe[contains(@src,'vkprime'])]")
		# grabbing the iframes on the page
		ifras = driver.find_elements_by_tag_name("iframe")
		# print("found frames \n")
		for ifra in ifras:
			# print("checking frames")
			# looking for iframes with src containing vk
			# print(ifra.get_attribute("src"))
			if(ifra.get_attribute("src").find("plyr") > 0):
				sources.append(ifra.get_attribute("src"))

		# if(count % 2 == 0):
		driver.quit()
		count+=1
				


	# for source in sources:
	# 	# print(source)
	
	frames = []
	for source in sources:
		frames.append('<iframe src="%s" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(source))
	driver.quit()
	list(set(a))
	return (list(set(frames)))


def scrapeSecond():
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	driver.get("https://www.desitellybox.me/category/and-tv/bhabhiji-ghar-par-hain/")
	headlines = driver.find_elements_by_xpath("//*[contains(text(), 'Episode Watch Online')]")[0].click()
	time.sleep(5)
	headlines = driver.find_elements_by_xpath("//a[contains(text(), 'Bhabhiji Ghar Pe Hai') and contains(text(), 'Hai')]")
	links = []
	for headline in headlines:
		link = (headline.get_attribute("href"))
		if (link.lower().find("vk") > 0 ):
			links.append(link)
			# print (link)

	if(len(links) == 0):
		return 'Latest Episode not available yet'
	link = links[0]
	eyeD = link[link.find("=")+1: len(link)]
	linkTwo = links[1]
	eyeDTwo = linkTwo[linkTwo.find("=")+1: len(linkTwo)]
	# print (eyeD)
	# print (eyeDTwo)
	driver.quit()
	return (['<iframe src="http://vkprime.com/embed-%s.html" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(eyeD), '<iframe src="http://vkprime.com/embed-%s.html" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(eyeDTwo)])

def scrapeThird():
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	driver.get("https://www.desitellybox.me/category/star-plus/kullfi-kumarr-bajewala/")
	headlines = driver.find_elements_by_xpath("//*[contains(text(), '2020 Watch Online')]")[0].click()
	time.sleep(5)
	headlines = driver.find_elements_by_xpath("//a[contains(text(), 'Kullfi Kumarr') and contains(text(), 'Bajewala')]")
	links = []
	for headline in headlines:
		link = (headline.get_attribute("href"))
		if (link.lower().find("vk") > 0 ):
			links.append(link)
			# print (link)

	if(len(links) == 0):
		return 'Latest Episode not available yet'
	link = links[0]
	eyeD = link[link.find("=")+1: len(link)]
	linkTwo = links[1]
	eyeDTwo = linkTwo[linkTwo.find("=")+1: len(linkTwo)]
	# print (eyeD)
	# print (eyeDTwo)
	driver.quit()
	return (['<iframe src="http://vkprime.com/embed-%s.html" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(eyeD), '<iframe src="http://vkprime.com/embed-%s.html" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(eyeDTwo)])

def scrapeFourth():
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	driver.get("https://www.desitellybox.me/category/sony-tv/kapil-sharma-show/")
	headlines = driver.find_elements_by_xpath("//*[contains(text(), 'Episode Watch Online')]")[0].click()
	time.sleep(5)
	headlines = driver.find_elements_by_xpath("//a[contains(text(), 'The Kapil Sharma') and contains(text(), 'Show')]")
	links = []
	for headline in headlines:
		link = (headline.get_attribute("href"))
		if (link.lower().find("vk") > 0 ):
			links.append(link)
			# print (link)

	if(len(links) == 0):
		return 'Latest Episode not available yet'
	link = links[-1]
	eyeD = link[link.find("=")+1: len(link)]
	driver.quit()
	return (['<iframe src="http://vkprime.com/embed-%s.html" frameborder="0" allowfullscreen="" marginwidth="0" marginheight="0" scrolling="NO" width="520" height="400"></iframe>'%(eyeD)])

def getListOfShows():
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	showLinks = [
	#"http://www.yodesitv.info/star-plus/",
	#"http://www.yodesitv.info/colors/",
	#"http://www.yodesitv.info/zee-tv/",
	#"http://www.yodesitv.info/sony-tv/",
	#"http://www.yodesitv.info/tv-and-tv/",
	#"http://www.yodesitv.info/mtv-india/",
	#"http://www.yodesitv.info/sab-tv/",
	#"http://www.yodesitv.info/star-bharat/",
	#"http://www.yodesitv.info/star-jalsha/",
	#"http://www.yodesitv.info/star-pravah/",
	#"http://www.yodesitv.info/star-vijay/",
	"http://www.yodesitv.info/bindass-tv/"
	]

	allShows = {"allShows": []}

	for show in showLinks:
		# allShows.append(show)
		driver.get(show)
		showCards = driver.find_elements_by_class_name("one_fourth  ")
		#driver.find_element_by_xpath("//*[contains(text(), 'Archived')]").click()
		for card in showCards:
			show = {"name": "",
				"link": "",
				"imageLink": ""
				}

			name = (card.find_element_by_tag_name("p").find_element_by_tag_name("a").text)
			show["name"] = name
			show["link"] = (card.find_element_by_tag_name("p").find_element_by_tag_name("a").get_attribute("href"))
			show["imageLink"] = (card.find_element_by_tag_name("a").find_element_by_tag_name("img").get_attribute("src"))
			if((len(name) != 0)):
				allShows["allShows"].append(show)
		# print(len(showCards))
	driver.quit()
	return allShows

def getDates(link):
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	driver.get(link)
	headlines = driver.find_elements_by_class_name("latestPost-content")
	eppisodes = {"eppisodes": []}
	for headline in headlines:
		title = headline.find_element_by_tag_name("a").get_attribute("title")
		link = headline.find_element_by_tag_name("a").get_attribute("href")
		eppisode = {"title": title, "link": link}
		eppisodes["eppisodes"].append(eppisode)
		# print(title)
	driver.quit()
	return eppisodes







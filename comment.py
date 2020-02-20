from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


def print_same_line(text):
	sys.stdout.write('\r')
	sys.stdout.flush()
	sys.stdout.write(text)
	sys.stdout.flush()

while True:
	website = "https://www.instagram.com/"
	username = "mybotforyou"
	password = "kam125486"
	message = "YOUR MESSAGE"



	class InstagramBot:

		def __init__(self, username, password):
			self.username = username
			self.password = password
			self.browser = webdriver.Firefox()
			self.browser.set_window_size(1100, 900)

		def closeBrowser(self):
			self.browser.close()

		def login(self):
			browser = self.browser
			start_time = time.monotonic()
			browser.get(website)
			time.sleep(1)

			#Login button
			login_button = browser.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
			login_button.click()
			time.sleep(1)

			#Username input
			user_name_elem = browser.find_element_by_css_selector('div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
			user_name_elem.clear()
			user_name_elem.send_keys(self.username)

			#Password input
			passworword_elem = browser.find_element_by_css_selector('div.-MzZI:nth-child(3) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
			passworword_elem.clear()
			passworword_elem.send_keys(self.password)
			passworword_elem.send_keys(Keys.RETURN)
			time.sleep(3)

			#Copy url after https://instagram.com/ into quotations marks 
			browser.get(website + "p/B8ZbouiBDFr/")
			time.sleep(1)
			
			#Comment
			for x in range(2):
				try:
					comment_box_elem = browser.find_element_by_css_selector(".Ypffh")
					comment_box_elem.clear()
					comment_box_elem.send_keys(message)
					comment_box_elem.send_keys(Keys.ENTER)
					time.sleep(2)
				except:
					pass
			browser.close()

			print("Exit time: 			",(f'{time.monotonic()-start_time}'))

	andreyIG = InstagramBot(username, password)
	andreyIG.login()
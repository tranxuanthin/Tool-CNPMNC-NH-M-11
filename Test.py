from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
def ham_surf_face():
	options = Options() 
	
	profile = 	["10","11","12","13"]
	# ,"11","12","13","14","15","16","18", 
	# 			"19","20","21","22","23","24","1","3","5","6"]
	for i in profile: 
		path = 'Profile ' + i 
		print(i) 
		options.add_argument(r"--user-data-dir=C:\\Users\\Acer\\AppData\\Local\\Google\\Chrome\\User Data") 
		options.add_argument(r'--profile-directory='+path) 
		driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=options)
		driver.get('https://www.facebook.com/') 
		time.sleep(3) 
		driver.get('https://www.facebook.com/CNProteinThin/') 
		time.sleep(4)
		driver.execute_script('document.querySelector(".bp9cbjyn.j83agx80.taijpn5t.c4xchbtz.by2jbhx6.a0jftqn4").click()')
		
		time.sleep(5)
		if(path == 'Profile 10'):
			driver.get('https://bookshoponlineit.000webhostapp.com/nhom11.html') 
			time.sleep(5)
		 	
		driver.close()
ham_surf_face()	
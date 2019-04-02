# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


#webdriver and time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
from time import strftime


#mail
import smtplib



#set variables
time = (datetime.datetime.now().strftime('%H'))

email_user = ('')
email_pass = ('')
email_send = ('')


def email():
	#fetch weather from website
	driver = webdriver.PhantomJS()
	driver.get("http://worldweather.wmo.int/en/city.html?cityId=138")

#decriptors_weather
	min_temp = driver.find_element_by_xpath("/html/body/div/div[6]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/span[1]").text
	max_temp = driver.find_element_by_xpath("/html/body/div/div[6]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/span[3]").text
	desc_temp = driver.find_element_by_xpath("/html/body/div/div[6]/div[5]/div[2]/div[2]/div[1]/div[1]/div[4]").text
	min_temp1 = ("The minimum is " + min_temp[0] + min_temp[1])
	max_temp1 = (", the Maximum is " + max_temp[0] + max_temp[1])
	desc_temp1 = (" and the weather description is " +desc_temp)
	weather = min_temp1 + max_temp1 + desc_temp1

#email stuff
	message = weather
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(email_user, email_pass)
	server.sendmail(email_user, email_send, message)
	server.quit()

while 1 == 1:
	time = strftime("%H")
	if time >= 7 and time <= 24:
		email()
		break

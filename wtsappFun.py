from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

driver=webdriver.Chrome() #to open chrome browser
driver.get("https://web.whatsapp.com") #to go to whatsapp webpage

time.sleep(90) #time for QR code scanning

text="The text that is to be sent" #any text

#to send same message multiple times to different contact, just have to run for a list of contacts
##for my_contact in ["contact 1","contact 2",...,"contact n"]:

#Or for a single contact
my_contact="my contact"

#to find the search bar and then to search the contact name
search = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(my_contact+Keys.ENTER)

#to find the chatbox of the selected contact
chatbox_xpath='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'

#run the loop to the number of times you want to forward the message
for i in range(5000):
    text_box=driver.find_element(By.XPATH,chatbox_xpath)
    text_box.send_keys(text+Keys.ENTER)

#to confirm all messages are sent
text_box=driver.find_element(By.XPATH,chatbox_xpath)
text_box.send_keys("Last text"+Keys.ENTER)

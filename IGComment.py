from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
#taking inputs
user=input('Enter your username: ')
password=input('Enter your password: ')
acc=input("Enter the account's username: ")
n=input('Enter the no, of posts you want to go through: ')
#open instagram
PATH='C:\\Program Files (x86)\chromedriver_win32\\chromedriver'
driver=webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/')
sleep(1)s
#enters login details and logs you into instagram
driver.find_element_by_xpath("//input[@name='username']").send_keys(user)
sleep(0.2)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
sleep(0.2)
driver.find_element_by_xpath("//button[@type='submit']").click() #or driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
sleep(3)
driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
sleep(0.6)
driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
#opens the account
driver.get('https://www.instagram.com/'+acc+'/?hl=en')
sleep(1.5)
# finds the first picture  
pic = driver.find_element_by_class_name("_9AhH0")    
pic.click()   # clicks on the first picture
sleep(1)
comments={1:'WOW',2:'Amazing',3:'Great'}
for i in range(4):
    sleep(2)
    n=randint(1,3)
    try:
        comment=driver.find_element_by_css_selector("[aria-label='Comment']")
        comment.click()
        sleep(3)
        Add_c=driver.find_element_by_css_selector("[aria-label='Add a comment…']")
        Add_c.send_keys(comments[n])
        sleep(1)
        Add_c.send_keys(Keys.RETURN)
        sleep(2)
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()   
        sleep(2)
    except:
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()   
        sleep(2)

from selenium import webdriver
from selenium.webdriver.common.by import By

def base(url):
    driver=webdriver.Chrome(executable_path='D:\\Python\\Framework\\chromedriver_win32\\chromedriver.exe')
    driver.get(url=url)
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    print(type(driver.current_url))
    driver.find_element(By.ID,'name').send_keys("AKshay Shelke")
    #driver.find_element(By.NAME,'enter-name').send_keys('Akshay')
    #This is for Git 
    driver.find_element(By.ID,'alertbtn').click()
    driver.save_screenshot("D:\\Python\\Framework\\chromedriver_win32\\ss.png")
    print("Execution Completed")


def screen_shot(url):
    driver=webdriver.Chrome(executable_path='D:\\Python\\Framework\\chromedriver_win32\\chromedriver.exe')
    driver.get(url=url)
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    print(type(driver.current_url))
    driver.save_screenshot("D:\\Python\\Framework\\chromedriver_win32\\ss.png")
    
    
from selenium import webdriver
browser = webdriver.Chrome()
use=input("帳號:")
psw=input("密碼")

browser.get('https://www.eyny.com/member.php?mod=logging&action=login')

a=browser.find_element_by_name('username')
a.send_keys(use)

a=browser.find_element_by_name('password')

a.send_keys(psw)

a.submit()

#!/LouisDing/bin/python3.7
from selenium import webdriver
import urllib.request as req
import bs4
import time

driverPath = 'chromedriver.exe'  # 留意路徑內容，此案放在專案資料夾內
url = 'http://www08.eyny.com/'
request = req.Request(url, headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")
loginTag = root.select('#toptb > div > div.y > a:nth-child(5)')[0]['href']
loginpageUrl = url + loginTag
usernameStr=input('請輸入帳號: ')
passwordStr=input('請輸入密碼: ')

browser = webdriver.Chrome()
browser.get(loginpageUrl)
username=browser.find_element_by_name('username').send_keys(usernameStr)
password=browser.find_elements_by_name('password')[0].send_keys(passwordStr)
loginsubmit=browser.find_elements_by_name('loginsubmit')[0].click()
time.sleep(5)


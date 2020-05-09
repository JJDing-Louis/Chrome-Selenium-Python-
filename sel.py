from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://ppt.cc/f9GtSx')

a=browser.find_element_by_xpath('/html/body/div/form/center/b/font/input[1]')
a.click()

a=browser.find_element_by_name('p')
a.send_keys('0507')

a.submit()

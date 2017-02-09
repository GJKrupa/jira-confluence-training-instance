from selenium import webdriver

browser = webdriver.phantomjs.webdriver.WebDriver()
browser.get('http://localhost:8080/')

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

driver = webdriver.Chrome(options=options)
service = Service(executable_path='chromedriver.exe', log_path='NUL')

# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# total_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# search = driver.find_element(By.NAME, value='search')
# search.send_keys('Python', Keys.ENTER)

# driver.get('https://secure-retreat-92358.herokuapp.com')

# first_name = driver.find_element(By.CLASS_NAME, 'top')
# first_name.send_keys('Grace')

# last_name = driver.find_element(By.CLASS_NAME, 'middle')
# last_name.send_keys('Bong')

# email = driver.find_element(By.CLASS_NAME, 'bottom')
# email.send_keys('gracebong.park@gmail.com')

# submit_button = driver.find_element(By.CSS_SELECTOR, 'button')
# submit_button.click()

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')
store_items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
items_ids = [ item.get_attribute('id') for item in store_items ]

five_seconds = time.time() + 5
five_minutes = time.time() + (60 * 5)

while True:
    cookie.click()
    current_time = time.time()

    if current_time > five_seconds:
        
        upgrade_prices = []
        all_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        
        for price in all_prices:
            if price.text != '':
                cost = price.text.split('-')[1]
                upgrade_prices.append(cost)
        
        upgrades_dict = {}
        for i in range(len(upgrade_prices)):
            if ',' in upgrade_prices[i]:
                upgrade_prices[i] = upgrade_prices[i].replace(',', '')
            upgrades_dict[items_ids[i]] = upgrade_prices[i]
        
        cookie_count = driver.find_element(By.ID, value='money').text
        if ',' in cookie_count:
            cookie_count = cookie_count.replace(',', '')
        money = int(cookie_count)
        
        can_upgrade_dict = {}
        
        for key, value in upgrades_dict.items():
            if money > int(value):
                can_upgrade_dict[key] = value
      
        highest_upgrade = max(can_upgrade_dict)
        highest_upgrade_element = driver.find_element(By.ID, value=highest_upgrade)
        highest_upgrade_element.click()

        five_seconds = current_time + 5
    
    if current_time > five_minutes:
        cookie_per_second = driver.find_element(By.ID, value='cps')
        print(f'Cookies per second: {cookie_per_second}')
        
driver.quit()
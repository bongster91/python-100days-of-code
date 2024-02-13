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


driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3745278638&f_AL=true&keywords=software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')

sign_in_button = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

email_input = driver.find_element(By.ID, value='username')
password_input = driver.find_element(By.ID, value='password')

email_input.send_keys('')
password_input.send_keys('')

sign_in_button = driver.find_element(By.CSS_SELECTOR, value='.login__form_action_container button')
sign_in_button.click()

time.sleep(5)

save_button = driver.find_element(By.CLASS_NAME, value='jobs-save-button')
save_button.click()
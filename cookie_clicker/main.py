from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

driver = webdriver.Chrome(options=options)
service = Service(executable_path='chromedriver.exe', log_path='NUL')

# driver.get('https://www.amazon.com/PrimePets-Tennis-Squeaky-Interactive-Medium/dp/B0C81H84JX/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=dAJkM&content-id=amzn1.sym.225b4624-972d-4629-9040-f1bf9923dd95%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=225b4624-972d-4629-9040-f1bf9923dd95&pf_rd_r=8W4KNZGMDTZVTDT22Q28&pd_rd_wg=96fej&pd_rd_r=bc50e89e-dc60-4749-8430-ca1d0b78ada8&pd_rd_i=B0C81H84JX&th=1')

# captcha = driver.find_element(By.LINK_TEXT, 'Try different image')
# captcha.click()

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get('https://www.python.org/')

dates = driver.find_elements(By.CLASS_NAME, value='event-widget time')
date_labels = driver.find_elements(By.CLASS_NAME, value='event-widget ul a')

new_dates_dict = {}

for i in range(0, len(dates)):
    current_date = dates[i].text
    current_label = date_labels[i].text
    inner_dict = {
        'time': current_date,
        'name': current_label
    }
    new_dates_dict[i] = inner_dict
    
print(new_dates_dict)
    
driver.quit()
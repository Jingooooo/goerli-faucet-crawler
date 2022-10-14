import time, os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

address = "0x621a5AdA4f37074Eb10D06fe070FF9cac096B564"

service = ChromeService(executable_path=ChromeDriverManager().install())
options = ChromeOptions()
# options.add_argument("headless")
# options.add_argument("user-data-dir=/Users/user/Library/Application Support/Google/Chrome/Profile 2")
driver = webdriver.Chrome(options=options, service=service)

driver.get('https://goerlifaucet.com/')

login_btn = driver.find_element(By.CLASS_NAME, 'btn-sm')

login_btn_text = login_btn.get_attribute('innerHTML').splitlines()[0]
print(login_btn_text)

if login_btn_text == 'Alchemy Login':
    print("login")
    ActionChains(driver).move_to_element(login_btn).click().pause(4).perform()

    if driver.current_url != 'https://goerlifaucet.com/':
        print("google login")
        connect_google_btn = driver.find_element(By.CLASS_NAME, 'css-1aizh0x')

        ActionChains(driver).move_to_element(connect_google_btn).click().pause(4).perform()

        time.sleep(5)

        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element(By.NAME, "identifier").send_keys(os.getenv("EMAIL") + Keys.ENTER)
            time.sleep(3)
            driver.find_element(By.NAME, "password").send_keys(os.getenv("PASSWORD") + Keys.ENTER)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(10)


address_input = driver.find_element(By.CLASS_NAME, "alchemy-faucet-panel-input-text").send_keys(address)
time.sleep(3)

driver.quit()
# send_btn = driver.find_element(By.CLASS_NAME, "alchemy-faucet-button")
# ActionChains(driver).move_to_element(address_input).send_keys(address).pause(3).perform()

# driver.switch_to.window(driver.window_handles[1])
#
# driver.find_element(By.ID, "identifierId").send_keys("jingooo2@hexlant.com" + Keys.ENTER)
# time.sleep(4)
# driver.find_element(By.NAME, "password").send_keys("0805redso0801" + Keys.ENTER)
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(10)


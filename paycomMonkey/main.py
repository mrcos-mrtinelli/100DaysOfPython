import credentials
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

DRIVER_PATH = "/Users/marcos/chromedriver"

TIME_SHEET_XPATH = "/html/body/div[6]/div[2]/div[1]/div[1]/div/div/div[4]/div/a"


def convert_dates(d):
    return datetime.strptime(d, '%b %d, %Y').strftime('%m/%d/%Y')


driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Login to paycom
driver.get(url="https://www.paycomonline.net/v4/ee/web.php/app/login")
time.sleep(2)
username = driver.find_element_by_id("txtlogin")
username.send_keys(credentials.USERNAME)

password = driver.find_element_by_id("txtpass")
password.send_keys(credentials.PASSWORD)

userpin = driver.find_element_by_id("userpinid")
userpin.send_keys(credentials.USERPIN)
userpin.send_keys(Keys.ENTER)

# Request text message
time.sleep(2)
send_a_text = driver.find_element_by_id("factor_option0")
driver.execute_script("arguments[0].click();", send_a_text)

next_button = driver.find_element_by_name("next")
next_button.click()

time.sleep(1)
pin_input = driver.find_element_by_name("pin")
pin_input.send_keys("")

# Wait for auth
while True:
    auth_confirm = input("Hit 'y' when confirmation code entered: ")
    if auth_confirm == "y":
        break

# Go to time sheet
time.sleep(2)
time_sheet = driver.find_element_by_xpath(TIME_SHEET_XPATH)
time_sheet.click()

# Get date
time.sleep(3)
current_pay_period = driver.find_element_by_name("timecard-payperiod-header")
from_to = current_pay_period.text.split('to')
start_day = convert_dates(from_to[0].strip())
end_day = convert_dates(from_to[1].strip())

# Add punch
add_punch = driver.find_element_by_name("timecard-add-punch")
add_punch.click()

time.sleep(2)
punch_start_day = driver.find_element_by_name("punch_start_day")
punch_start_day.clear()
punch_start_day.send_keys(start_day)

punch_end_day = driver.find_element_by_name("punch_end_day")
punch_end_day.clear()
punch_end_day.send_keys(end_day)

punch_exclude_weekend = driver.find_element_by_xpath("//*[contains(text(), 'Exclude Weekends')]")
driver.execute_script("arguments[0].click();", punch_exclude_weekend)





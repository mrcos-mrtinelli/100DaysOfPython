from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/marcos/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://www.python.org")
events_elements = driver.find_elements_by_css_selector(".event-widget ul.menu li")
events_dict = {}

for idx, el in enumerate(events_elements):
    time = el.find_element_by_tag_name("time").text
    name = el.find_element_by_tag_name("a").text
    events_dict[idx] = {
        "time": time,
        "name": name
    }

print(events_dict)

# driver.get("http://secure-retreat-92358.herokuapp.com/")
# fname = driver.find_element_by_name("fName")
# lname = driver.find_element_by_name("lName")
# email = driver.find_element_by_name("email")
# sign_up = driver.find_element_by_class_name("btn-primary")
#
# fname.send_keys("5w3469 rty8oefhsd")
# lname.send_keys("74t8903rweuodfisl")
# email.send_keys("edfosui@gerysh.com")
# sign_up.click()


# driver.close()

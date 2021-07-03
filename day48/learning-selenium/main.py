from selenium import webdriver

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

driver.close()

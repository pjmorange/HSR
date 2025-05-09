from selenium import webdriver
from selenium.webdriver.common.by import By

# for holding the resultant list
element_list = []

for page in range(1, 3, 1):
    driver = webdriver.Chrome()
    page_url = "https://game8.co/games/Honkai-Star-Rail/archives/486305?page=" + str(page)
    driver.get(page_url)
    
    driver.maximize_window()

    searchIcon = driver.find_element(By.CLASS_NAME, 'a-table a-table top center')

    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

print(element_list)

#closing the driver
driver.close()
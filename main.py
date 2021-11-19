from web import driver
from time import sleep
driver.get("https://popcat.click/")
x= 0

while x <100:
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="app"]/div').click()
    x+=1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome('/Users/harryovnik/Desktop/project/chromedriver',options=chrome_options)

driver.get("https://socialblade.com/youtube/top/country/kw")

delay = 3 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'sp_message_iframe_403865')))



    driver.switch_to.frame("sp_message_iframe_403865")

    driver.find_element_by_xpath('//*[@title="Accept"]').click()

    driver.switch_to.default_content()

    c=[]
    x=driver.find_elements_by_xpath("html/body/div/div/div/div/sup/i")
    for i in x:
        parent = i.find_element_by_xpath("./../..")
        c.append(parent)
    print(len(c))

    final=[]
    for i in c:
        # print(i.get_attribute('innerHTML'))
        # print(i.find_element_by_xpath("./a").text)
        q=i.find_element_by_xpath("./sup/i").get_attribute("title")
        print(q)
        if q=="Category: education":
            final.append(i.find_element_by_xpath("./a").text)

    print(final)
except TimeoutException:
    print("Done")




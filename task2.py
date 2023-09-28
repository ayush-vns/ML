import time
import pandas as pd
from selenium import webdriver


def getUrls(asins, countries):
 url = "https://www.amazon.{0}/dp/{1}"
 n = len(asins)
 urls = []
 for i in range(n):
    country = countries[i]
    asin = asins[i]
    urls.append(url.format(country, asin))
    return urls


def downloadUrl(url):
    # driver = webdriver.Chrome(
    #     'D:/chrome/chromedriver.exe')  # Optional argument, if not specified will search path.
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome()

    driver.get(
        url)

    time.sleep(15)  # Let the user actually see something!

    src = driver.page_source
    driver.quit()
    return src


url="https://www.amazon.de/dp/1015"
data=downloadUrl(url)
print(data)
name, money = readexcel()
urls = getUrls(asins, countries)
print(urls)
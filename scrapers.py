from abc import ABC, abstractmethod
import time
from bs4 import BeautifulSoup as soup
from calculations import get_price_per_100g

class Scraper(ABC):
    @abstractmethod
    def scrapeData(self, driver, link):
        pass

class CostcoScraper(Scraper):
    def scrapeData(self, driver, link):
        driver.get(link)
        try:
            driver.find_element_by_class_name('modal-buttons').click()
        except:
            pass
        driver.refresh()
        time.sleep(18)
        page_html = driver.page_source

        page_soup = soup(page_html, "html.parser")
        try:
            name = page_soup.find("h1", itemprop="name").text
            price = page_soup.find("div", id="pull-right-price").text
            price = price.strip()
            price = float(price[:-1])
        except:
            name = "Product Error"
            price = -1

        per_100g = get_price_per_100g(name, price)
        if (per_100g != -1):
            unit_price = f"{per_100g} /100 g"
        else:
            unit_price = None
        # print(unit_price)

        return (name, price, unit_price)

class AmazonScraper(Scraper):
    def scrapeData(self, driver, link):
        driver.get(link)
        time.sleep(2)

        name = driver.find_element_by_id("productTitle").text

        try:
            price = driver.find_element_by_xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]').text[1:]
            unit_price = driver.find_element_by_xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[2]').text[3:-1]
            # print(f"Price {price} | Unit Price {unit_price} | Unit: {unit}")
        except:
            price = -1
            unit_price = None

        return (name, price, unit_price)
#!"C:\Users\Kang\.conda\envs\web_scraping\python.exe"

from selenium import webdriver
from dotenv import load_dotenv
import os

import sys

from scrapers import AmazonScraper, CostcoScraper
from InvalidLinkError import InvalidLinkError
from sendEmail import sendEmail
from FileWriter import CsvWriter

if(__name__ == "__main__"):

    load_dotenv()

    driver = webdriver.Chrome(os.environ['DRIVER_PATH'])

    records = []

    costcoScraper = CostcoScraper()
    amazonScraper = AmazonScraper()

    with open(sys.argv[1], "r") as file:
        for line in file.readlines():
            line = line.strip()
            if ("www.costco.ca" in line):
                record = costcoScraper.scrapeData(driver, line)
            elif ("www.amazon.ca" in line):
                record = amazonScraper.scrapeData(driver, line)
            else:
                raise InvalidLinkError(f"Invalid Link: {line}")
            records.append(record);

    driver.quit()

    csvWriter = CsvWriter()
    csvWriter.write(records, os.environ['OUTPUT_FILE_NAME']+".csv")

    sendEmail(os.environ['EMAIL_FROM'], os.environ['EMAIL_TO'], os.environ['OUTPUT_FILE_NAME']+".csv", os.environ['EMAIL_SUBJECT'], os.environ["EMAIL_PWD"])

    # def get_split_amt(name, start, end):
    #     split = re.split(r'[xX×]', name[start:end].strip().replace(",", "."))
    #     if (len(split) == 2):
    #         return float(split[0].strip()) * float(split[1].strip())
    #     else:
    #         try:
    #             return float(split[0].strip())
    #         except:
    #             return -1

    # def get_price_per_100g(name: str, price: float) -> float:
    #     # print(name, price)
    #     if (price != -1) or ("count" not in name) or ("pack" not in name):
    #         # start = re.search(r"\d", name).start()
    #         start = name.rfind(",") + 2
    #         kg = name[start:].lower().find(" kg")
    #         g = name[start:].lower().find(" g")
    #         if (kg != -1):
    #             end = kg + start
    #             amount = get_split_amt(name, start, end)
    #             if (amount == -1):
    #                 return -1
    #             unit_price = round(price / (amount * 1000) * 100, 2)
    #         elif (g != -1):
    #             end = g + start
    #             amount = get_split_amt(name, start, end)
    #             if (amount == -1):
    #                 return -1
    #             unit_price = round(price /  amount * 100, 2)
    #         else:
    #             unit_price = -1
    #         # print(start, end, unit_price)
    #         return unit_price
    #     return -1

    # def getCostcoData(link):
    #     driver.get(link)
    #     try:
    #         driver.find_element_by_class_name('modal-buttons').click()
    #     except:
    #         pass
    #     driver.refresh()
    #     time.sleep(18)
    #     page_html = driver.page_source

    #     page_soup = soup(page_html, "html.parser")
    #     try:
    #         name = page_soup.find("h1", itemprop="name").text
    #         price = page_soup.find("div", id="pull-right-price").text
    #         price = price.strip()
    #         price = float(price[:-1])
    #     except:
    #         name = "Product Error"
    #         price = -1

    #     per_100g = get_price_per_100g(name, price)
    #     if (per_100g != -1):
    #         unit_price = f"{per_100g} /100 g"
    #     else:
    #         unit_price = None
    #     # print(unit_price)

    #     return (name, price, unit_price)

    # def getAmazonData(link):
    #     driver.get(link)
    #     time.sleep(2)

    #     name = driver.find_element_by_id("productTitle").text

    #     try:
    #         price = driver.find_element_by_xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]').text[1:]
    #         unit_price = driver.find_element_by_xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[2]').text[3:-1]
    #         # print(f"Price {price} | Unit Price {unit_price} | Unit: {unit}")
    #     except:
    #         price = -1
    #         unit_price = None

    #     return (name, price, unit_price)


    # # Costco
    # costco_records = []

    # costco_links = [
    #         "https://www.costco.ca/kirkland-signature-organic-virgin-coconut-oil%2c-2.3-kg.product.100416822.html",
    #         "https://www.costco.ca/compass-sweetened-shredded-coconut%2c-2-kg.product.100413542.html",
    #         "https://www.costco.ca/kraft-smooth-peanut-butter%2c-2-kg.product.100417656.html",
    #         "https://www.costco.ca/kirkland-signature-100%25-pure-liquid-honey%2c-3-kg.product.100417641.html",
    #         "https://www.costco.ca/sunmaid-organic-raisins%2c-1814-g.product.100538492.html",
    #         "https://www.costco.ca/yupik-sultana-raisins%2c-2-kg.product.100498339.html",
    #         "https://www.costco.ca/happy-village-organic-smyrna-figs%2c-1.13-kg.product.100538457.html",
    #         "https://www.costco.ca/ocean-spray-craisins-whole-%2526-juicy-dried-cranberries%2c-1.8-kg.product.100417267.html",
    #         "https://www.costco.ca/kirkland-signature-shelled-walnuts%2c-1.36-kg.product.100416584.html",
    #         "https://www.costco.ca/kirkland-signature-whole-almonds,-1.36-kg.product.100177082.html",
    #         "https://www.costco.ca/master%e2%80%99s-hand-enriched-all-purpose-flour%2c-10-kg.product.100417270.html",
    #         "https://www.costco.ca/norquin-canadian-tri-colour-quinoa%2c-2.3-kg.product.100563087.html",
    #         "https://www.costco.ca/norquin-golden-whole-grain-quinoa%2c-2.3-kg.product.100574530.html",
    #         "https://www.costco.ca/quaker-quick-oats,-2-×-2.58-kg.product.100570610.html",
    #         "https://www.costco.ca/kirkland-signature-organic-soy-beverage%2c-946-ml%2c-6-count.product.100417879.html",
    #         "https://www.costco.ca/springtime-complete-laundry-detergent%2c-165-wash-loads.product.100552995.html",
    #         "https://www.costco.ca/lysol-advanced-disinfecting-wet-wipes%2c-6-pack.product.100461222.html",
    #         "https://www.costco.ca/kirkland-signature-b100-complex-tablets%2c-300-count.product.100300719.html",
    #         "https://www.costco.ca/kirkland-signature-vitamin-d3%2c-1000-iu%2c-2-packs.product.100322373.html",
    #         "https://www.costco.ca/webber-naturals-vitamin-e-400-iu-softgels%2c-300-count.product.100235730.html",
    #         "https://www.costco.ca/swiss-dark-chocolate%2c-1%2c3-kg-(2.8-lb).product.100417063.html",
    #         "https://www.costco.ca/.product.100417065.html",
    #         "https://www.costco.ca/redpath-golden-yellow-sugar%2c-2-kg.product.100413549.html",
    #         "https://www.costco.ca/post-honey-bunches-of-oats-with-almonds%2c-1.4-kg.product.100417852.html",
    #         "https://www.costco.ca/kellogg%e2%80%99s-corn-flakes%2c-1.22-kg.product.100417877.html",
    #         "https://www.costco.ca/kellogg%e2%80%99s-mini-wheats-original-jumbo-pack%2c-1.6-kg.product.100417872.html",
    #         "https://www.costco.ca/lindt-lindor-assorted-chocolates-cornet%2c-900-g.product.100462299.html",
    #         "https://www.costco.ca/eagle-brand-sweetened-condensed-milk-original-300-ml,-3-pack.product.100417285.html",
    #         "https://www.costco.ca/isopropyl-alcohol-99%25-bottles%2c-4-pack.product.100422775.html",
    #         "https://www.costco.ca/lysol-advanced-toilet-bowl-cleaner%2c-4-x-946-ml%2c-2-pack.product.100356764.html"]

    # for item in costco_links:
    #     costco_records.append(getCostcoData(item))

    # # Amazon
    # amazon_records = []

    # amazon_links = [
    #         "https://www.amazon.ca/Yupik-Thompson-Raisins-1Kg/dp/B00NAU307M/ref=sr_1_4?dchild=1&keywords=Thompson+raisin&qid=1604411077&sr=8-4",
    #         "https://www.amazon.ca/Vaseline-Problem-Therapy-Petroleum-Jelly/dp/B003M5UN02/ref=sr_1_2?crid=34CWVM1LK9UFN&dchild=1&keywords=problem+skin+therapy&qid=1604411322&sprefix=problem+skin%2Caps%2C263&sr=8-2",
    #         "https://www.amazon.ca/Bobs-Red-Mill-Flaxseed-Meal/dp/B07BG49J3D/ref=sr_1_1?crid=24OOAEBYH8BRF&dchild=1&keywords=bobs+red+mill+flaxseed+meal&qid=1604411466&sprefix=flaxseed%2Bbobs+red+meal%2Caps%2C295&sr=8-1"]

    # for item in amazon_links:
    #     amazon_records.append(getAmazonData(item))

    # driver.quit()

    # # Costo csv
    # for thing in costco_records:
    #     print(f"Name: {thing[0]} || Price: {thing[1]}")

    # time = datetime.datetime.now()
    # with open("dailyPriceData.csv", "w", newline='', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["Date:", time])
    #     writer.writerow("\n")

    #     writer.writerow(["Costco"])
    #     writer.writerow(['Name', 'Price', 'Unit Price'])
    #     writer.writerows(costco_records)

    #     writer.writerow("\n")

    #     writer.writerow(["Amazon"])
    #     writer.writerow(['Name', 'Price', 'Unit Price'])
    #     writer.writerows(amazon_records)




    # msg = EmailMessage()
    # msg["From"] = "chunkanglu@gmail.com"
    # msg["Subject"] = "Daily Costco Price Update"
    # msg["To"] = "stephaniewng@hotmail.com"
    # msg.set_content("Attached is the price data.")
    # msg.add_attachment(open("dailyPriceData.csv", "r").read(), filename="dailyPriceData.csv")

    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.ehlo()
    # server.starttls()
    # server.ehlo()
    # server.login("chunkanglu@gmail.com", "89B8d686daf748508c7c")

    # server.send_message(msg)
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
    
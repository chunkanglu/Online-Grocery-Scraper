import datetime
import csv
import os
from abc import ABC, abstractmethod

class Writer(ABC):
    @abstractmethod
    def write(self, records, filename):
        pass

class CsvWriter(Writer):
    def write(self, records, filename):
        time = datetime.datetime.now()
        with open(filename, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Date:", time])
            writer.writerow("\n")

            writer.writerow(['Name', 'Price', 'Unit Price'])
            writer.writerows(records)
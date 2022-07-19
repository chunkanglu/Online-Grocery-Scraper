import re

def get_split_amt(name, start, end):
    split = re.split(r'[xX×]', name[start:end].strip().replace(",", "."))
    if (len(split) == 2):
        return float(split[0].strip()) * float(split[1].strip())
    else:
        try:
            return float(split[0].strip())
        except:
            return -1

def get_price_per_100g(name: str, price: float) -> float:
    # print(name, price)
    if (price != -1) or ("count" not in name) or ("pack" not in name):
        # start = re.search(r"\d", name).start()
        start = name.rfind(",") + 2
        kg = name[start:].lower().find(" kg")
        g = name[start:].lower().find(" g")
        if (kg != -1):
            end = kg + start
            amount = get_split_amt(name, start, end)
            if (amount == -1):
                return -1
            unit_price = round(price / (amount * 1000) * 100, 2)
        elif (g != -1):
            end = g + start
            amount = get_split_amt(name, start, end)
            if (amount == -1):
                return -1
            unit_price = round(price /  amount * 100, 2)
        else:
            unit_price = -1
        # print(start, end, unit_price)
        return unit_price
    return -1
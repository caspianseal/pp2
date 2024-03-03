import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

price_pattern = r'\d+\.\d+\sx\s(\d+,\d+)'

prices = re.findall(price_pattern, text)

for index, price in enumerate(prices, start=1):
    print(f"{index}. Price: {price}")

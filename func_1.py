import csv


f = open("all_stocks_5yr.csv", "r", encoding="utf-8")
reader = csv.DictReader(f, delimiter=',', quotechar='|')

top10 = sorted(reader,key=lambda x: float(x["high"] or 0), reverse=True)[:10]

for row in top10:
    print(f"{row['date']}|{row['open']}|{row['high']}|{row['low']}|{row['close']}|{row['volume']}|{row['Name']}")
import csv


def select_sorted(sort_columns=["high"], limit=30, group_by_name=False, order='desc', filename='dump.csv'):
    s_c = "".join(sort_columns)
    f = open("all_stocks_5yr.csv", "r", encoding="utf-8")
    reader = csv.DictReader(f, delimiter=',', quotechar='|')
    top10 = sorted(reader, key=lambda x: float(x[s_c] or 0), reverse=True)[:int(limit)]

    for row in top10:
        print(f"{row['date']}|{row['open']}|{row['high']}|{row['low']}|{row['close']}|{row['volume']}|{row['Name']}")

        """Запись в файл"""
    f = open("dump.csv", "w", encoding="utf-8", newline="")
    writer = csv.DictWriter(f, fieldnames=list(top10[0].keys()), delimiter=",", quoting=csv.QUOTE_NONE)
    writer.writeheader()
    for i in top10:
        writer.writerow(i)


select_sorted(sort_columns=["high"], limit=15, group_by_name=False, order='desc', filename='dump.csv')

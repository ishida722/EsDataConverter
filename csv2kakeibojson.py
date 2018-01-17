import csv
import datetime
import sys

args = sys.argv

if len(args) < 2 : sys.exit()

CSV_FILE = args[1]
OUTPUT_FILE = args[1] + '.json'
INDEX_JSON = '{"index":{"_index":"accounts"}}\n'
DATA_JSON = '{{"date": {date}, "name": {name}, "amount": {amount}, "expence": {expence}}}\n'
CANMA = '"'

with open(CSV_FILE, newline='') as f:
    csvList = list(csv.reader(f))
    csvList = csvList[1:]

def PrepareDate(dateStr):
    INPUT_DATE_FORMAT_1  = '%Y/%m/%d %H:%M:%S'
    INPUT_DATE_FORMAT_2  = '%Y/%m/%d'
    OUTPUT_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

    try:
        date = datetime.datetime.strptime(dateStr, INPUT_DATE_FORMAT_1)
    except:
        date = datetime.datetime.strptime(dateStr, INPUT_DATE_FORMAT_2)

    retDate = date.strftime(OUTPUT_DATE_FORMAT)

    return retDate

with open(OUTPUT_FILE, mode='w') as f:
    for row in csvList:
        f.write(INDEX_JSON)
        date = CANMA+PrepareDate(row[0])+CANMA
        name = CANMA+row[3]+CANMA
        amount = row[1]
        expence = CANMA+row[2]+CANMA
        f.write(DATA_JSON.format(date=date, name=name, amount=amount, expence=expence))
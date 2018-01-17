import csv
import datetime

INDEX_JSON = '{"index":{"_index":"accounts"}}'
DEFAULT_JSON_FORMAT = '{{"date": {date}, "name": {name}, "amount": {amount}, "expence": {expence}}}'
CANMA = '"'

class Converter:
    inputDateFomat = False
    INPUT_DATE_FORMAT_SIRIAL = '%Y%m%d'

    def LoadCsvFile(self, csvFile):
        with open(csvFile, newline='') as f:
            self.csvList = list(csv.reader(f))
            self.csvList = self.csvList[1:]

    def LoadCsvStrings(self, csvStrings):
        pass

    def Convert(self):
        self.convertedJson = []
        for row in self.csvList:
            self.convertedJson.append(INDEX_JSON)
            date = CANMA+self.PrepareDateFromStr(row[0])+CANMA
            name = CANMA+row[3]+CANMA
            amount = row[1]
            expence = CANMA+row[2]+CANMA
            self.convertedJson.append(DEFAULT_JSON_FORMAT.format(date=date, name=name, amount=amount, expence=expence))

    @classmethod
    def SetInputDateFormatToSirial(self):
        self.inputDateFomat = self.INPUT_DATE_FORMAT_SIRIAL

    @classmethod
    def SetInputDateFormatToDefault(self):
        self.inputDateFomat = False

    @classmethod
    def PrepareDateFromStr(self, dateStr):
        DEFAULT_INPUT_DATE_FORMAT_1  = '%Y/%m/%d %H:%M:%S'
        DEFAULT_INPUT_DATE_FORMAT_2  = '%Y/%m/%d'
        OUTPUT_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

        if self.inputDateFomat:
            date = datetime.datetime.strptime(dateStr, self.inputDateFomat)
        else:
            try:
                date = datetime.datetime.strptime(dateStr, DEFAULT_INPUT_DATE_FORMAT_1)
            except:
                date = datetime.datetime.strptime(dateStr, DEFAULT_INPUT_DATE_FORMAT_2)

        retDate = date.strftime(OUTPUT_DATE_FORMAT)

        return retDate

    # with open(OUTPUT_FILE, mode='w') as f:
    #     for row in csvList:
    #         f.write(INDEX_JSON)
    #         date = CANMA+PrepareDate(row[0])+CANMA
    #         name = CANMA+row[3]+CANMA
    #         amount = row[1]
    #         expence = CANMA+row[2]+CANMA
    #         f.write(DEFAULT_JSON_FORMAT.format(date=date, name=name, amount=amount, expence=expence))

if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) <= 1:
        print('Input CSV file name')
        sys.exit()

    CSV_FILE = args[1]
    OUTPUT_FILE = args[1] + '.json'

    converter = Converter()
    converter.LoadCsvFile(CSV_FILE)
    converter.Convert()

    print(converter.convertedJson)

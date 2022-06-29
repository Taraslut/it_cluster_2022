import json
import xmltodict

import xlrd


class BaseReader:

    def __init__(self, f_name):
        self.file_name = f_name
        self.data = None

    def read(self):
        raise NotImplemented

    def get_param(self, name):
        return self.data.get(name)


class JsonReader(BaseReader):

    def read(self):
        self.data = json.load(self.file_name)


class XMLReader(BaseReader):

    def read(self):
        file_data = open(self.file_name, "rt").read()
        self.data = xmltodict.parse(file_data)


class ExcelReader(BaseReader):

    def read(self):
        file = xlrd.open_workbook(self.file_name)
        sheert = file.sheet_by_index(0)
        index = 0
        self.data = {}
        while True:
            key = sheert.cell_value(index, 0)
            val = sheert.cell_value(index, 1)
            if key is None or key == "":
                break
            self.data[key] = val


class Reader:

    def __init__(self, f_name: str):
        self.f_name = f_name
        self.reader = None
        self.process()

    def process(self):
        if self.f_name.endswith("json"):
            self.reader = JsonReader(self.f_name)
        elif self.f_name.endswith("xml"):
            self.reader = XMLReader(self.f_name)
        elif self.f_name.endswith("xls") or self.f_name.endswith("xlsx"):
            self.reader = ExcelReader(self.f_name)
        else:
            print("File format is unknown!!!")


def main():
    f_name = "my.json"

    data = Reader(f_name)
    print(data.reader.data)


if __name__ == '__main__':
    main()

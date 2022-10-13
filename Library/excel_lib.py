import xlrd
from Library.config import Config


class ReadExcel:
    """Includes methods for reading locators and data from excel sheet"""

    def read_testdata(self, sheetname):
        wb = xlrd.open_workbook(Config.TESTDATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()  # generator object
        header = next(rows)
        data = []

        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data


    def read_locators(self, sheetname):
        wb = xlrd.open_workbook(Config.LOCATORS_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)

        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)

        return d
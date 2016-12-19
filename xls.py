# -*- coding: utf-8 -*-
import xlrd

def readSnomedData(filename,colIndex,startRow = 0):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    #print(table.nrows)
    #print(table.name)
    count = 0
    for row in range(startRow,table.nrows):
        content = table.cell(row,colIndex).value
        print(content)


if __name__ == '__main__':
    #readSnomedData('snomed.xlsx',1)
    readSnomedData('疾病分类与代码.xlsx',2,2)
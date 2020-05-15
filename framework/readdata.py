import xlrd

class ReadData():
    def __init__(self,filename):
        self.filename =filename

    
    def readrow(self,sheetname):
        data = xlrd.open_workbook(self)
        table = data.sheet_by_name(sheetname)
        nrows = table.nrows  # 行数
        #ncols = table.ncols  # 列数
        line=[]
        #line2=[]
        for row in range(1, nrows):
            line.append(str(table.row_values(row, 1)))
            #line2.append(str(table.row_values(row, 1)[-1]))
        return line

        #print(line)
        #print(line2)


#ReadData.readtable('F:\THDwebframe\data\longin.xlsx','login')
    def readcol(self,sheetname):
        data = xlrd.open_workbook(self)
        table = data.sheet_by_name(sheetname)
        #nrows = table.nrows  # 行数
        ncols = table.ncols  # 列数
        line=[]
        #line2=[]
        for col in range(1, ncols):
            #line1.append(str(table.row_values(row, 1)[0]))
            line.append(table.col_values(col, 1))

        return line

'''a='F:\THDwebframe\data\longin.xlsx'
b=ReadData.readrow(a,'login')
print(b)'''
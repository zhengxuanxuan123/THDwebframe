from framework.readdata import ReadData
data = ReadData.readcol('F:\THDwebframe\data\longin.xlsx', 'login')
usn = data[0]
psw = data[1]
#psw = data.line2
print(usn[0])
print(psw[0])
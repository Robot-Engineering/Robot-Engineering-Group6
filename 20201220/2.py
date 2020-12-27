import xlrd
import xlwt
from xlutils.copy import copy

def read_sheet():
    workbook=xlrd.open_workbook(r'D:\python\testdat\student.xlsx)
    sheet=excel.sheet_by_index(0)
    rows=sheet.row_values(0)
    index=rows.index('photo')

    for i in range(1,rows)
        if i!='photo'
            picture.append()
        print(picture)
        if not photo_data[0]:
             color = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')
                sheet2.write(i, 1, sheet1.cell_value(i,2), color)
                sheet.save('D:\python\testdat\student.xlsx')
        elif '.jpg' in photo_data[0][0]:
                sheet2.write(i, 2, 'D:\python\testdat' + str(int(element)))
                sheet.save('D:\python\testdat\student.xlsx')
wb.save(r'D:\testdat\student.xlsx)

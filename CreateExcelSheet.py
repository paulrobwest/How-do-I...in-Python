# Create an Excel worksheet

import xlsxwriter

workbook = xlsxwriter.Workbook('testpy.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Task')
worksheet.write('B1', 'Date')
worksheet.write('C1', 'Complete?')

workbook.close()

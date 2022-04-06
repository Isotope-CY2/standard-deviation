# 开发时间：2022/4/6 22:43
import  xlrd
from decimal import  Decimal
import math
import cmath
#导入数学模块，高数模块，小数模块（虽然没用上），Excel读取模块

workbook = xlrd.open_workbook('Fluid.xls')

print('文件导入成功','\n')

sheet1 = workbook.sheet_by_index(4)
nrows1 = sheet1.nrows
ncols1 = sheet1.ncols

#获取第一张sheet内数据

print('sheet导入成功，该表格有{0}行，{1}列'.format(nrows1,ncols1),'\n')

#确认数据正确

for i in range(2,nrows1):
    sum = 0
    sqsum = 0
    for j in range(1,ncols1 - 1):
        sum += sheet1.cell_value(i, j)
    avg = sum / 10
    for j in range(1,ncols1 - 1):
        sqsum += (sheet1.cell_value(i, j) - avg) ** 2
    #    print('第{0}行数据的方差为{1:0.3f}'.format(i - 1, sqsum)) 计算方差，可不用
    print('第{0}行数据的标准差为{1:0.3f}'.format(i - 1, abs(cmath.sqrt(sqsum))))

# 标准差运算模块

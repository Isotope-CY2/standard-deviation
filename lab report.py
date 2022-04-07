# 开发时间：2022/4/6 22:43
import xlrd
import cmath

# 导入数学模块，高数模块，小数模块（虽然没用上），Excel读取模块

workbook = xlrd.open_workbook('Fluid.xls')

print('文件导入成功', '\n')

n = int(input('请输入你需要查找的页码'))

print('')

datas = 10

if n == 1 or n == 2 or n == 5:
    new_row = 1
else:
    new_row = 2
if n == 6:
    datas = 3

n = n - 1

sheet1 = workbook.sheet_by_index(n)
nrows1 = sheet1.nrows
ncols1 = sheet1.ncols

# 获取第一张sheet内数据

print('sheet{2}导入成功，该表格有{0}行，{1}列'.format(nrows1, ncols1, n + 1), '\n')

# 确认数据正确

for i in range(2, nrows1):
    sum = 0
    sqsum = 0
    A = []
    for j in range(new_row, ncols1 - 1):
        sum += sheet1.cell_value(i, j)
        A.append(sheet1.cell_value(i, j))
    avg = sum / datas
    for j in range(new_row, ncols1 - 1):
        sqsum += (sheet1.cell_value(i, j) - avg) ** 2
    #    print('第{0}行数据的方差为{1:0.3f}'.format(i - 1, sqsum)) 计算方差，可不用
    error = max(max(A) - avg, avg - min(A))
    print('第{0}行数据的标准差为{1:0.3f}'.format(i - 1, abs(cmath.sqrt(sqsum))),end='  ')
    print('数值为{0:0.3f}+-{1:0.3f}'.format(avg, error))

# 标准差运算模块

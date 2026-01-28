"""
读取excel文件
    xls文件
        使用xlrd模块的open_workbook
"""


import xlrd
import xlwt
def read_excel():
    """读取xls文件"""

    wd = xlrd.open_workbook('1769140037667安卓订单数据.xls')# 通过open——workbook打开文件
    sheet_names = wd.sheet_names()# 通过sheet——names获取所有表单名字
    # print(sheet_names)

    sheet = wd.sheet_by_name('安卓订单数据')# 通过sheet_by_name获取指定表单
    # print(sheet.name, sheet.nrows, sheet.ncols)# 获取表单名字，行数，列数

    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            """
            通过row、col
            """
            value = sheet.cell(row, col).value
            if col > 0:
                """对非首行数据进行格式化处理"""
                value = int(value)
            print(value, end='\t')
        print()


import pandas as pd
def read_excel_pandas():
    """使用pandas模块读取excel文件"""

    df = pd.read_excel('1769140037667安卓订单数据.xls', sheet_name='安卓订单数据')
    print(df)
    df2 = pd.read_excel('1769140037667安卓订单数据.xlsx', sheet_name='安卓订单数据', index_col=0)
    print(df2)

import random
def write_excel():
    """写入excel文件"""

    wb = xlwt.Workbook()# 创建一个工作簿
    sheet_name = '成绩单'# 创建一个表单
    sheet = wb.add_sheet(sheet_name)# 指定工作表单

    titles = ['姓名','语文', '数学', '物理', '化学', '生物']# 表单标题
    nams = ['王昭君', '貂蝉', '西施', '小乔', '大乔']


    header_style = xlwt.XFStyle()

    # 字体（Font）
    header_style.font.name = 'Times New Roman'
    header_style.font.height = 20 * 11    # 字体大小（Font）
    header_style.font.colour_index = 4# 设置字体颜色   0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色

    # 斜体
    header_style.font.italic = True

    # 加粗
    header_style.font.bold = True  # 设置字体加粗

    # 对齐方式（Alignment）
    header_style.alignment.vert = xlwt.Alignment.VERT_CENTER  # 设置垂直居中
    header_style.alignment.horz = xlwt.Alignment.HORZ_CENTER  # 设置水平居中

    # 边框（Border）
    header_style.borders.left = xlwt.Borders.THIN
    header_style.borders.right = xlwt.Borders.THIN
    header_style.borders.top = xlwt.Borders.THIN
    header_style.borders.bottom = xlwt.Borders.THIN

    # 背景（Background）
    # header_style.pattern.pattern = xlwt.Pattern.SOLID_PATTERN# 设置背景 启用填充 NO_PATTERN（关闭填充）
    # header_style.pattern.pattern_back_colour = xlwt.Style.colour_map['yellow']# 设置背景 纯黄
    # header_style.pattern.pattern_back_colour = 5


    for index,title in enumerate(titles):
        """
            enumerate:将一个可迭代对象组合成带索引的枚举对象
            enumerate（iterable，start=0）
                iterable：可迭代对象（如，列表、元组、字符串等）
                start：索引起始值，默认0
                return：返回一个枚举对象，enumerate object，含（index，value）形式的元组    
        """
        sheet.write(0, index, title, header_style)

    for index,name in enumerate(nams):
        """
            write(row, col, value, style=None)
                row：行号
                col：列号
                value：写入的值
                style：样式
        """
        sheet.write(index+1, 0, name)

        # 为每个学生生成5门课程的不同分数
        for subject_index in range(1, len(titles)):  # 从第1列开始（跳过姓名列）
            score = random.randint(60, 100)
            sheet.write(index+1, subject_index, score)

    wb.save('成绩单.xls')

from xlutils.copy import copy
def get_col_letter(col_idx):
    """获取列字母"""
    result = ''

    while col_idx >= 0:
        result = chr(ord('A') + col_idx % 26) + result
        col_idx = col_idx // 26 - 1
    return  result

def computation():
    """公式计算"""

    # 打开 文件
    wb_for_read = xlrd.open_workbook('成绩单.xls')

    #获取工作表
    # sheet = wb_for_write.sheet_by_name('成绩单')# 指定表名
    original_sheet = wb_for_read.sheet_by_index(0)

    # 获取表内 行列
    nrows , ncols = original_sheet.nrows,original_sheet.ncols

    wb_for_write = copy(wb_for_read)# 需要复制一份进行写入操作
    sheet = wb_for_write.get_sheet(0)# 获取表对象

    # 新增列
    titles = ['总分', '平均分', '排名','最高分', '最低分']
    for index,title in enumerate(titles):
        """
        write(row, col, value, style=None)
            row：行号
            col：列号
            value：写入的值
            style：样式
        """
        sheet.write(0, ncols+index, title)

    for row in range(1, nrows):# 从第二行开始
        """
            为每个学生计算成绩
        """
        # 总分计算
        scores = [original_sheet.cell(row,col).value for col in range(1, ncols)]
        total = sum(scores)
        sheet.write(row, ncols, total)

        # 平均分计算
        avg = total/len(scores)
        sheet.write(row, ncols+1, avg)

        # 排名计算 按总分排序
        total_col = get_col_letter(ncols)  # ncols=6 则返回 'G'
        excel_row = row + 1 # 行从2开始
        formula_str = f'RANK({total_col}{excel_row},{total_col}2:{total_col}6,0)'# 获取总分排名
        formula = xlwt.Formula(formula_str)# 创建公式对象
        sheet.write(row, ncols + 2, formula)  # I列：排名

        # 最高分、最低分计算
        score_col_first = get_col_letter(1)  # 假设第一门课程成绩列
        score_col_last = get_col_letter(ncols-1)
        max_formula = xlwt.Formula(f'MAX({score_col_first}{row+1}:{score_col_last}{row+1})')
        sheet.write(row, ncols + 3, max_formula)
        min_formula = xlwt.Formula(f'MIN({score_col_first}{row+1}:{score_col_last}{row+1})')
        sheet.write(row, ncols + 4, min_formula)

    wb_for_write.save('成绩单2.xls')


def main():
    # read_excel()
    # read_excel_pandas()
    # write_excel()
    computation()

    pass

if __name__ == '__main__':
    main()
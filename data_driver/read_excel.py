#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 13:27
# @Author  : being℡
# @File    : read_excel.py
# @Software: python3.9.5 win10
import openpyxl


# 读取Excel内容，实现文件驱动自动化执行
def read_excel():
    excel = openpyxl.load_workbook('./data/testdata.xlsx')
    sheet = excel['Sheet1']
    list_tuple = []
    # 逐行读取Excel的数据
    for value in sheet.values:
        if type(value[0]) is int:
            # print(value)
            # 将元组tuple装进list里
            list_tuple.append(value)
    return list_tuple


if __name__ == '__main__':
    print(read_excel())
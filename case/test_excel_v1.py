#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 13:39
# @Author  : being℡
# @File    : test_excel_v1.py
# @Software: python3.9.5 win10
import pytest

from pytest_excel_allure.data_driver.read_excel import read_excel


@pytest.mark.parametrize('data',read_excel())
def test01(data):
    print(data)



if __name__ == '__main__':
    pytest.main(['-s'])

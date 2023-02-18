#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 15:10
# @Author  : being℡
# @File    : main_run.py
# @Software: python3.9.5 win10
import os
import pytest

if __name__ == '__main__':
    # -s 参数，不加的时候，日志会自动捕捉到allure报告中去
    # pytest.main(['-v','--alluredir','allure-results','--clean-alluredir','./case/test_excel_v2.py'])
    # # 生成allure报告
    # os.system('allure generate ./allure-results -o ./allure-report/html --clean')

    # pytest.main(['-s', '-q','./','--clean-alluredir','--alluredir=allure-results'])
    # os.system('cp environment.properties ./allure-results/environment.properties')
    # os.system("allure generate -c -o allure-report")
    # "--alluredir"这个是创建allure报告的路径。
    # -o是执行，--clean是清除之前生成的报告。
     pytest.main(["./case/test_excel_v2.py",
                 "-v", "--alluredir", "../allure-report/temp_jsonreport"])
     os.system("allure generate ../allure-report/temp_jsonreport -o ./allure-report/html --clean")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 15:47
# @Author  : being℡
# @File    : api_key.py
# @Software: python3.9.5 win10
"""
这个是接口关键字驱动类，用于提供自动化接口测试的关键字方法
"""
import json

import jsonpath
import requests


class ApiKey:
    # 基于jsonpath获取数据的关键字方法：用于获取所需要的内容
    # json输出，格式转换
    # loads,将json格式的报文转换成字典
    # dumps,将字典格式的报文转换成json
    def get_text(self,data,key):
        """
        :return:
        """
        dict_data = json.loads(data)
        value_list= jsonpath.jsonpath(dict_data,key)
        return value_list[0]

    # post 请求封装
    def post(self,url, data=None, json=None, **kwargs):
        res_post = requests.post(url=url, data=data, json=json, **kwargs)
        return res_post

    # get 请求封装
    def get(self,url, params=None, **kwargs):
        res_get = requests.get(url=url,params=params,**kwargs)
        return res_get

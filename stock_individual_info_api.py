# -*- coding: utf-8 -*-
"""
AKTools API调用 - 个股信息查询相关接口
基于AKShare股票数据接口完整文档编写
"""

import requests
import pandas as pd


def stock_individual_info_em(symbol):
    """
    获取个股信息查询-东方财富
    
    接口名称: stock_individual_info_em
    目标地址: http://quote.eastmoney.com/concept/sh603777.html?from=classic
    描述: 东方财富-个股-股票信息
    限量: 单次返回指定个股的详细信息
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="603777"; 股票代码 |
    
    输出参数:
    - 返回个股详细信息
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_individual_info_em"
    params = {
        "symbol": symbol
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_individual_basic_info_xq(symbol):
    """
    获取个股信息查询-雪球
    
    接口名称: stock_individual_basic_info_xq
    目标地址: https://xueqiu.com/snowman/S/SH601127/detail#/GSJJ
    描述: 雪球财经-个股-公司概况-公司简介
    限量: 单次返回指定个股的基本信息
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="SH601127"; 股票代码 |
    
    输出参数:
    - 返回个股基本信息
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_individual_basic_info_xq"
    params = {
        "symbol": symbol
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


# 示例调用
if __name__ == "__main__":
    print("=== 个股信息查询数据接口测试 ===")
    
    # 获取个股信息查询-东方财富
    print("\n1. 个股信息查询-东方财富(000001):")
    individual_info_df = stock_individual_info_em(symbol="000001")
    print(individual_info_df.head())
    
    # 获取个股信息查询-雪球
    print("\n2. 个股信息查询-雪球(SH601127):")
    basic_info_df = stock_individual_basic_info_xq(symbol="SH601127")
    print(basic_info_df.head())

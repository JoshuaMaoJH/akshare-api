# -*- coding: utf-8 -*-
"""
AKTools API调用 - 股票市场总貌相关接口
基于AKShare股票数据接口完整文档编写
"""

import requests
import pandas as pd


def stock_sse_summary():
    """
    获取上海证券交易所总貌数据
    
    接口名称: stock_sse_summary
    目标地址: http://www.sse.com.cn/market/stockdata/statistic/
    描述: 上海证券交易所-股票数据总貌
    限量: 单次返回上海证券交易所股票数据总貌
    
    输入参数:
    - 无参数
    
    输出参数:
    - 返回实时行情数据表格
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_sse_summary"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_szse_summary():
    """
    获取深圳证券交易所总貌数据
    
    接口名称: stock_szse_summary
    目标地址: http://www.szse.cn/market/overview/index.html
    描述: 深圳证券交易所-市场总貌-证券类别统计
    限量: 单次返回深圳证券交易所市场总貌数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 返回证券类别统计数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_szse_summary"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_szse_area_summary():
    """
    获取深圳证券交易所地区交易排序数据
    
    接口名称: stock_szse_area_summary
    目标地址: http://www.szse.cn/market/overview/index.html
    描述: 深圳证券交易所-市场总貌-地区交易排序
    限量: 单次返回深圳证券交易所地区交易排序数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 返回地区交易排序数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_szse_area_summary"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_szse_sector_summary(symbol="当年"):
    """
    获取深圳证券交易所股票行业成交数据
    
    接口名称: stock_szse_sector_summary
    目标地址: http://docs.static.szse.cn/www/market/periodical/month/W020220511355248518608.html
    描述: 深圳证券交易所-统计资料-股票行业成交数据
    限量: 单次返回深圳证券交易所股票行业成交数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="当月"; choice of {"当月", "当年"} |
    
    输出参数:
    - 返回股票行业成交数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_szse_sector_summary"
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


def stock_sse_deal_daily():
    """
    获取上海证券交易所每日概况数据
    
    接口名称: stock_sse_deal_daily
    目标地址: http://www.sse.com.cn/market/stockdata/overview/day/
    描述: 上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况
    限量: 单次返回上海证券交易所每日概况数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 返回每日概况数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_sse_deal_daily"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


# 示例调用
if __name__ == "__main__":
    print("=== 股票市场总貌数据接口测试 ===")
    
    # 获取上海证券交易所总貌数据
    print("\n1. 上海证券交易所总貌数据:")
    sse_summary_df = stock_sse_summary()
    print(sse_summary_df.head())
    
    # 获取深圳证券交易所总貌数据
    print("\n2. 深圳证券交易所总貌数据:")
    szse_summary_df = stock_szse_summary()
    print(szse_summary_df.head())
    
    # 获取深圳证券交易所地区交易排序数据
    print("\n3. 深圳证券交易所地区交易排序数据:")
    szse_area_df = stock_szse_area_summary()
    print(szse_area_df.head())
    
    # 获取深圳证券交易所股票行业成交数据
    print("\n4. 深圳证券交易所股票行业成交数据(当年):")
    szse_sector_df = stock_szse_sector_summary(symbol="当年")
    print(szse_sector_df.head())
    
    # 获取上海证券交易所每日概况数据
    print("\n5. 上海证券交易所每日概况数据:")
    sse_daily_df = stock_sse_deal_daily()
    print(sse_daily_df.head())

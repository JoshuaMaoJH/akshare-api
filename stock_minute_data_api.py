# -*- coding: utf-8 -*-
"""
AKTools API调用 - 分时数据相关接口
基于AKShare股票数据接口完整文档编写
"""

import requests
import pandas as pd


def stock_zh_a_minute(symbol, period="1", adjust=""):
    """
    获取分时数据-新浪
    
    接口名称: stock_zh_a_minute
    目标地址: http://finance.sina.com.cn/realstock/company/sh600519/nc.shtml
    描述: 新浪财经-沪深京A股股票或者指数的分时数据，目前可以获取1, 5, 15, 30, 60分钟的数据频率, 可以指定是否复权
    限量: 单次返回指定沪深京A股上市公司指定日期间的分时数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="sh600519"; 股票代码 |
    | period | str | period="1"; choice of {"1", "5", "15", "30", "60"} |
    | adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |
    
    输出参数:
    - 返回分时数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_a_minute"
    params = {
        "symbol": symbol,
        "period": period,
        "adjust": adjust
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_zh_a_hist_min_em(symbol, period="1", start_date="", end_date="", adjust=""):
    """
    获取分时数据-东方财富
    
    接口名称: stock_zh_a_hist_min_em
    目标地址: https://quote.eastmoney.com/concept/sh603777.html
    描述: 东方财富网-行情首页-沪深京A股-每日分时行情; 该接口只能获取近期的分时数据，注意时间周期的设置
    限量: 单次返回指定沪深京A股上市公司指定日期间的分时数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="603777"; 股票代码 |
    | period | str | period="1"; choice of {"1", "5", "15", "30", "60"} |
    | start_date | str | start_date="2021-09-01 09:30:00"; 开始查询的日期 |
    | end_date | str | end_date="2021-09-01 15:00:00"; 结束查询的日期 |
    | adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |
    
    输出参数:
    - 返回分时数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_a_hist_min_em"
    params = {
        "symbol": symbol,
        "period": period,
        "start_date": start_date,
        "end_date": end_date,
        "adjust": adjust
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_intraday_em(symbol):
    """
    获取日内分时数据-东方财富
    
    接口名称: stock_intraday_em
    目标地址: https://quote.eastmoney.com/f1.html?newcode=0.000001
    描述: 东方财富-分时数据
    限量: 单次返回指定股票的日内分时数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="000001"; 股票代码 |
    
    输出参数:
    - 返回日内分时数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_intraday_em"
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


def stock_intraday_sina(symbol):
    """
    获取日内分时数据-新浪
    
    接口名称: stock_intraday_sina
    目标地址: https://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill.php?symbol=sz000001
    描述: 新浪财经-日内分时数据
    限量: 单次返回指定股票的日内分时数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="sz000001"; 股票代码 |
    
    输出参数:
    - 返回日内分时数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_intraday_sina"
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


def stock_zh_a_hist_pre_min_em(symbol):
    """
    获取盘前数据-东方财富
    
    接口名称: stock_zh_a_hist_pre_min_em
    目标地址: https://quote.eastmoney.com/concept/sh603777.html
    描述: 东方财富-股票行情-盘前数据
    限量: 单次返回指定股票的盘前数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="603777"; 股票代码 |
    
    输出参数:
    - 返回盘前数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_a_hist_pre_min_em"
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
    print("=== 分时数据接口测试 ===")
    
    # 获取分时数据-新浪
    print("\n1. 分时数据-新浪(sh600519, 1分钟):")
    minute_df = stock_zh_a_minute(symbol="sh600519", period="1")
    print(minute_df.head())
    
    # 获取分时数据-东方财富
    print("\n2. 分时数据-东方财富(603777, 1分钟):")
    hist_min_df = stock_zh_a_hist_min_em(
        symbol="603777", 
        period="1", 
        start_date="2021-09-01 09:30:00", 
        end_date="2021-09-01 15:00:00"
    )
    print(hist_min_df.head())
    
    # 获取日内分时数据-东方财富
    print("\n3. 日内分时数据-东方财富(000001):")
    intraday_em_df = stock_intraday_em(symbol="000001")
    print(intraday_em_df.head())
    
    # 获取日内分时数据-新浪
    print("\n4. 日内分时数据-新浪(sz000001):")
    intraday_sina_df = stock_intraday_sina(symbol="sz000001")
    print(intraday_sina_df.head())
    
    # 获取盘前数据-东方财富
    print("\n5. 盘前数据-东方财富(603777):")
    pre_min_df = stock_zh_a_hist_pre_min_em(symbol="603777")
    print(pre_min_df.head())

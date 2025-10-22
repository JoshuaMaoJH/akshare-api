# -*- coding: utf-8 -*-
"""
AKTools API调用 - 历史行情数据相关接口
基于AKShare股票数据接口完整文档编写
"""

import requests
import pandas as pd


def stock_zh_a_hist(symbol, period="daily", start_date="", end_date="", adjust="", timeout=None):
    """
    获取历史行情数据-东方财富
    
    接口名称: stock_zh_a_hist
    目标地址: https://quote.eastmoney.com/concept/sh603777.html?from=classic(示例)
    描述: 东方财富-沪深京A股日频率数据; 历史数据按日频率更新, 当日收盘价请在收盘后获取
    限量: 单次返回指定沪深京A股上市公司、指定周期和指定日期间的历史行情日频率数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol='603777'; 股票代码可以在ak.stock_zh_a_spot_em()中获取 |
    | period | str | period='daily'; choice of {'daily', 'weekly', 'monthly'} |
    | start_date | str | start_date='20210301'; 开始查询的日期 |
    | end_date | str | end_date='20210616'; 结束查询的日期 |
    | adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |
    | timeout | float | timeout=None; 默认不设置超时参数 |
    
    输出参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | 日期 | object | 交易日 |
    | 股票代码 | object | 不带市场标识的股票代码 |
    | 开盘 | float64 | 开盘价 |
    | 收盘 | float64 | 收盘价 |
    | 最高 | float64 | 最高价 |
    | 最低 | float64 | 最低价 |
    | 成交量 | float64 | 成交量 |
    | 成交额 | float64 | 成交额 |
    | 振幅 | float64 | 振幅 |
    | 涨跌幅 | float64 | 涨跌幅 |
    | 涨跌额 | float64 | 涨跌额 |
    | 换手率 | float64 | 换手率 |
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_a_hist"
    params = {
        "symbol": symbol,
        "period": period,
        "start_date": start_date,
        "end_date": end_date,
        "adjust": adjust
    }
    if timeout is not None:
        params["timeout"] = timeout
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_zh_a_daily(symbol, start_date, end_date, adjust=""):
    """
    获取历史行情数据-新浪
    
    接口名称: stock_zh_a_daily
    目标地址: https://finance.sina.com.cn/realstock/company/sh600006/nc.shtml(示例)
    描述: 新浪财经-沪深京A股的数据, 历史数据按日频率更新; 注意其中的sh689009为CDR, 请通过ak.stock_zh_a_cdr_daily接口获取
    限量: 单次返回指定沪深京A股上市公司指定日期间的历史行情日频率数据, 多次获取容易封禁IP
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol='sh600000'; 股票代码可以在ak.stock_zh_a_spot()中获取 |
    | start_date | str | start_date='20201103'; 开始查询的日期 |
    | end_date | str | end_date='20201116'; 结束查询的日期 |
    | adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子 |
    
    输出参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | date | object | 交易日 |
    | open | float64 | 开盘价 |
    | high | float64 | 最高价 |
    | low | float64 | 最低价 |
    | close | float64 | 收盘价 |
    | volume | float64 | 成交量; 注意单位: 股 |
    | amount | float64 | 成交额; 注意单位: 元 |
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_a_daily"
    params = {
        "symbol": symbol,
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


def stock_zh_a_hist_tx(symbol, start_date, end_date, adjust=""):
    """
    获取历史行情数据-腾讯
    
    接口名称: stock_zh_a_hist_tx
    目标地址: https://gu.qq.com/sh000919/zs
    描述: 腾讯证券-日频-股票历史数据; 历史数据按日频率更新, 当日收盘价请在收盘后获取
    限量: 单次返回指定沪深京A股上市公司指定日期间的历史行情日频率数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="sh000919"; 股票代码 |
    | start_date | str | start_date="20201103"; 开始查询的日期 |
    | end_date | str | end_date="20201116"; 结束查询的日期 |
    | adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |
    
    输出参数:
    - 返回历史行情数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_a_hist_tx"
    params = {
        "symbol": symbol,
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


# 示例调用
if __name__ == "__main__":
    print("=== 历史行情数据接口测试 ===")
    
    # 获取历史行情数据-东方财富(不复权)
    print("\n1. 历史行情数据-东方财富(000001, 不复权):")
    hist_df = stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616")
    print(hist_df.head())
    
    # 获取历史行情数据-东方财富(前复权)
    print("\n2. 历史行情数据-东方财富(000001, 前复权):")
    hist_qfq_df = stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616", adjust="qfq")
    print(hist_qfq_df.head())
    
    # 获取历史行情数据-东方财富(后复权)
    print("\n3. 历史行情数据-东方财富(000001, 后复权):")
    hist_hfq_df = stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616", adjust="hfq")
    print(hist_hfq_df.head())
    
    # 获取历史行情数据-新浪
    print("\n4. 历史行情数据-新浪(sh600000):")
    daily_df = stock_zh_a_daily(symbol="sh600000", start_date="20201103", end_date="20201116")
    print(daily_df.head())
    
    # 获取历史行情数据-腾讯
    print("\n5. 历史行情数据-腾讯(sh000919):")
    hist_tx_df = stock_zh_a_hist_tx(symbol="sh000919", start_date="20201103", end_date="20201116")
    print(hist_tx_df.head())

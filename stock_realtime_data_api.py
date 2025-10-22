# -*- coding: utf-8 -*-
"""
AKTools API调用 - 实时行情数据相关接口
基于AKShare股票数据接口完整文档编写
"""

import requests
import pandas as pd


def stock_zh_a_spot_em():
    """
    获取沪深京A股实时行情-东方财富
    
    接口名称: stock_zh_a_spot_em
    目标地址: https://quote.eastmoney.com/center/gridlist.html#hs_a_board
    描述: 东方财富网-沪深京A股-实时行情数据
    限量: 单次返回所有沪深京A股上市公司的实时行情数据
    
    输入参数:
    - 无参数
    
    输出参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | 序号 | int64 | - |
    | 代码 | object | - |
    | 名称 | object | - |
    | 最新价 | float64 | - |
    | 涨跌幅 | float64 | 注意单位: % |
    | 涨跌额 | float64 | - |
    | 成交量 | float64 | 注意单位: 手 |
    | 成交额 | float64 | 注意单位: 元 |
    | 振幅 | float64 | 注意单位: % |
    | 最高 | float64 | - |
    | 最低 | float64 | - |
    | 今开 | float64 | - |
    | 昨收 | float64 | - |
    | 量比 | float64 | - |
    | 换手率 | float64 | 注意单位: % |
    | 市盈率-动态 | float64 | - |
    | 市净率 | float64 | - |
    | 总市值 | float64 | 注意单位: 元 |
    | 流通市值 | float64 | 注意单位: 元 |
    | 涨速 | float64 | - |
    | 5分钟涨跌 | float64 | 注意单位: % |
    | 60日涨跌幅 | float64 | 注意单位: % |
    | 年初至今涨跌幅 | float64 | 注意单位: % |
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_a_spot_em"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_sh_a_spot_em():
    """
    获取沪A股实时行情-东方财富
    
    接口名称: stock_sh_a_spot_em
    目标地址: http://quote.eastmoney.com/center/gridlist.html#sh_a_board
    描述: 东方财富网-沪A股-实时行情数据
    限量: 单次返回所有沪A股上市公司的实时行情数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 与沪深京A股实时行情相同的字段结构
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_sh_a_spot_em"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_sz_a_spot_em():
    """
    获取深A股实时行情-东方财富
    
    接口名称: stock_sz_a_spot_em
    目标地址: http://quote.eastmoney.com/center/gridlist.html#sz_a_board
    描述: 东方财富网-深A股-实时行情数据
    限量: 单次返回所有深A股上市公司的实时行情数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 与沪深京A股实时行情相同的字段结构
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_sz_a_spot_em"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_bj_a_spot_em():
    """
    获取京A股实时行情-东方财富
    
    接口名称: stock_bj_a_spot_em
    目标地址: http://quote.eastmoney.com/center/gridlist.html#bj_a_board
    描述: 东方财富网-京A股-实时行情数据
    限量: 单次返回所有京A股上市公司的实时行情数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 与沪深京A股实时行情相同的字段结构
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_bj_a_spot_em"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_new_a_spot_em():
    """
    获取新股实时行情-东方财富
    
    接口名称: stock_new_a_spot_em
    目标地址: http://quote.eastmoney.com/center/gridlist.html#newshares
    描述: 东方财富网-新股-实时行情数据
    限量: 单次返回所有新股的实时行情数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 与沪深京A股实时行情相同的字段结构
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_new_a_spot_em"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_cy_a_spot_em():
    """
    获取创业板实时行情-东方财富
    
    接口名称: stock_cy_a_spot_em
    目标地址: https://quote.eastmoney.com/center/gridlist.html#gem_board
    描述: 东方财富网-创业板-实时行情
    限量: 单次返回所有创业板股票的实时行情数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 与沪深京A股实时行情相同的字段结构
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_cy_a_spot_em"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_kc_a_spot_em():
    """
    获取科创板实时行情-东方财富
    
    接口名称: stock_kc_a_spot_em
    目标地址: http://quote.eastmoney.com/center/gridlist.html#kcb_board
    描述: 东方财富网-科创板-实时行情
    限量: 单次返回所有科创板股票的实时行情数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 与沪深京A股实时行情相同的字段结构
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_kc_a_spot_em"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_zh_ab_comparison_em():
    """
    获取AB股比价-东方财富
    
    接口名称: stock_zh_ab_comparison_em
    目标地址: https://quote.eastmoney.com/center/gridlist.html#ab_comparison
    描述: 东方财富网-行情中心-沪深京个股-AB股比价-全部AB股比价
    限量: 单次返回所有AB股比价数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 返回AB股比价数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_ab_comparison_em"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_zh_a_spot():
    """
    获取沪深京A股实时行情-新浪
    
    接口名称: stock_zh_a_spot
    目标地址: https://vip.stock.finance.sina.com.cn/mkt/#hs_a
    描述: 新浪财经-沪深京A股数据, 重复运行本函数会被新浪暂时封IP, 建议增加时间间隔
    限量: 单次返回所有沪深京A股上市公司的实时行情数据
    
    输入参数:
    - 无参数
    
    输出参数:
    - 返回实时行情数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_a_spot"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


def stock_individual_spot_xq(symbol):
    """
    获取个股实时行情-雪球
    
    接口名称: stock_individual_spot_xq
    目标地址: https://xueqiu.com/S/SH513520
    描述: 雪球-行情中心-个股
    限量: 单次返回指定个股的实时行情数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="SH600000"; 证券代码，可以是A股个股代码，A股场内基金代码，A股指数，美股代码, 美股指数 |
    
    输出参数:
    - 返回个股实时行情数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_individual_spot_xq"
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
    print("=== 实时行情数据接口测试 ===")
    
    # 获取沪深京A股实时行情-东方财富
    print("\n1. 沪深京A股实时行情-东方财富:")
    zh_a_spot_em_df = stock_zh_a_spot_em()
    print(zh_a_spot_em_df.head())
    
    # 获取沪A股实时行情-东方财富
    print("\n2. 沪A股实时行情-东方财富:")
    sh_a_spot_em_df = stock_sh_a_spot_em()
    print(sh_a_spot_em_df.head())
    
    # 获取深A股实时行情-东方财富
    print("\n3. 深A股实时行情-东方财富:")
    sz_a_spot_em_df = stock_sz_a_spot_em()
    print(sz_a_spot_em_df.head())
    
    # 获取京A股实时行情-东方财富
    print("\n4. 京A股实时行情-东方财富:")
    bj_a_spot_em_df = stock_bj_a_spot_em()
    print(bj_a_spot_em_df.head())
    
    # 获取新股实时行情-东方财富
    print("\n5. 新股实时行情-东方财富:")
    new_a_spot_em_df = stock_new_a_spot_em()
    print(new_a_spot_em_df.head())
    
    # 获取创业板实时行情-东方财富
    print("\n6. 创业板实时行情-东方财富:")
    cy_a_spot_em_df = stock_cy_a_spot_em()
    print(cy_a_spot_em_df.head())
    
    # 获取科创板实时行情-东方财富
    print("\n7. 科创板实时行情-东方财富:")
    kc_a_spot_em_df = stock_kc_a_spot_em()
    print(kc_a_spot_em_df.head())
    
    # 获取AB股比价-东方财富
    print("\n8. AB股比价-东方财富:")
    ab_comparison_df = stock_zh_ab_comparison_em()
    print(ab_comparison_df.head())
    
    # 获取沪深京A股实时行情-新浪
    print("\n9. 沪深京A股实时行情-新浪:")
    zh_a_spot_df = stock_zh_a_spot()
    print(zh_a_spot_df.head())
    
    # 获取个股实时行情-雪球
    print("\n10. 个股实时行情-雪球(SH600000):")
    individual_spot_df = stock_individual_spot_xq(symbol="SH600000")
    print(individual_spot_df.head())

# -*- coding: utf-8 -*-
"""
AKTools API调用 - A股数据接口完整汇总
基于AKShare股票数据接口完整文档编写
包含所有A股相关的数据接口调用方法
"""

import requests
import pandas as pd


# =============================================================================
# 1. 股票市场总貌相关接口
# =============================================================================

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


# =============================================================================
# 2. 个股信息查询相关接口
# =============================================================================

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


# =============================================================================
# 3. 行情报价相关接口
# =============================================================================

def stock_bid_ask_em(symbol):
    """
    获取行情报价-东方财富
    
    接口名称: stock_bid_ask_em
    目标地址: https://quote.eastmoney.com/sz000001.html
    描述: 东方财富-行情报价
    限量: 单次返回指定股票的行情报价数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="000001"; 股票代码 |
    
    输出参数:
    - 返回行情报价数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_bid_ask_em"
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


# =============================================================================
# 4. 实时行情数据相关接口
# =============================================================================

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


# =============================================================================
# 5. 历史行情数据相关接口
# =============================================================================

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


# =============================================================================
# 6. 分时数据相关接口
# =============================================================================

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


# =============================================================================
# 7. 历史分笔数据相关接口
# =============================================================================

def stock_zh_a_tick_tx(symbol, trade_date):
    """
    获取历史分笔数据-腾讯
    
    接口名称: stock_zh_a_tick_tx
    目标地址: http://gu.qq.com/sz300494/gp/detail(示例)
    描述: 每个交易日16:00提供当日数据; 如遇到数据缺失, 请使用ak.stock_zh_a_tick_163()接口(注意数据会有一定差异)
    限量: 单次返回指定股票的历史分笔数据
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | symbol | str | symbol="sz300494"; 股票代码 |
    | trade_date | str | trade_date="20210316"; 交易日期 |
    
    输出参数:
    - 返回历史分笔数据
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/stock_zh_a_tick_tx"
    params = {
        "symbol": symbol,
        "trade_date": trade_date
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()


# =============================================================================
# 示例调用和测试
# =============================================================================

if __name__ == "__main__":
    print("=== AKTools API调用 - A股数据接口完整测试 ===")
    
    # 1. 股票市场总貌数据接口测试
    print("\n=== 1. 股票市场总貌数据接口测试 ===")
    
    # 获取上海证券交易所总貌数据
    print("\n1.1 上海证券交易所总貌数据:")
    sse_summary_df = stock_sse_summary()
    print(sse_summary_df.head())
    
    # 获取深圳证券交易所总貌数据
    print("\n1.2 深圳证券交易所总貌数据:")
    szse_summary_df = stock_szse_summary()
    print(szse_summary_df.head())
    
    # 获取深圳证券交易所地区交易排序数据
    print("\n1.3 深圳证券交易所地区交易排序数据:")
    szse_area_df = stock_szse_area_summary()
    print(szse_area_df.head())
    
    # 获取深圳证券交易所股票行业成交数据
    print("\n1.4 深圳证券交易所股票行业成交数据(当年):")
    szse_sector_df = stock_szse_sector_summary(symbol="当年")
    print(szse_sector_df.head())
    
    # 获取上海证券交易所每日概况数据
    print("\n1.5 上海证券交易所每日概况数据:")
    sse_daily_df = stock_sse_deal_daily()
    print(sse_daily_df.head())
    
    # 2. 个股信息查询数据接口测试
    print("\n=== 2. 个股信息查询数据接口测试 ===")
    
    # 获取个股信息查询-东方财富
    print("\n2.1 个股信息查询-东方财富(000001):")
    individual_info_df = stock_individual_info_em(symbol="000001")
    print(individual_info_df.head())
    
    # 获取个股信息查询-雪球
    print("\n2.2 个股信息查询-雪球(SH601127):")
    basic_info_df = stock_individual_basic_info_xq(symbol="SH601127")
    print(basic_info_df.head())
    
    # 3. 行情报价数据接口测试
    print("\n=== 3. 行情报价数据接口测试 ===")
    
    # 获取行情报价-东方财富
    print("\n3.1 行情报价-东方财富(000001):")
    bid_ask_df = stock_bid_ask_em(symbol="000001")
    print(bid_ask_df.head())
    
    # 4. 实时行情数据接口测试
    print("\n=== 4. 实时行情数据接口测试 ===")
    
    # 获取沪深京A股实时行情-东方财富
    print("\n4.1 沪深京A股实时行情-东方财富:")
    zh_a_spot_em_df = stock_zh_a_spot_em()
    print(zh_a_spot_em_df.head())
    
    # 获取沪A股实时行情-东方财富
    print("\n4.2 沪A股实时行情-东方财富:")
    sh_a_spot_em_df = stock_sh_a_spot_em()
    print(sh_a_spot_em_df.head())
    
    # 获取深A股实时行情-东方财富
    print("\n4.3 深A股实时行情-东方财富:")
    sz_a_spot_em_df = stock_sz_a_spot_em()
    print(sz_a_spot_em_df.head())
    
    # 获取京A股实时行情-东方财富
    print("\n4.4 京A股实时行情-东方财富:")
    bj_a_spot_em_df = stock_bj_a_spot_em()
    print(bj_a_spot_em_df.head())
    
    # 获取新股实时行情-东方财富
    print("\n4.5 新股实时行情-东方财富:")
    new_a_spot_em_df = stock_new_a_spot_em()
    print(new_a_spot_em_df.head())
    
    # 获取创业板实时行情-东方财富
    print("\n4.6 创业板实时行情-东方财富:")
    cy_a_spot_em_df = stock_cy_a_spot_em()
    print(cy_a_spot_em_df.head())
    
    # 获取科创板实时行情-东方财富
    print("\n4.7 科创板实时行情-东方财富:")
    kc_a_spot_em_df = stock_kc_a_spot_em()
    print(kc_a_spot_em_df.head())
    
    # 获取AB股比价-东方财富
    print("\n4.8 AB股比价-东方财富:")
    ab_comparison_df = stock_zh_ab_comparison_em()
    print(ab_comparison_df.head())
    
    # 获取沪深京A股实时行情-新浪
    print("\n4.9 沪深京A股实时行情-新浪:")
    zh_a_spot_df = stock_zh_a_spot()
    print(zh_a_spot_df.head())
    
    # 获取个股实时行情-雪球
    print("\n4.10 个股实时行情-雪球(SH600000):")
    individual_spot_df = stock_individual_spot_xq(symbol="SH600000")
    print(individual_spot_df.head())
    
    # 5. 历史行情数据接口测试
    print("\n=== 5. 历史行情数据接口测试 ===")
    
    # 获取历史行情数据-东方财富(不复权)
    print("\n5.1 历史行情数据-东方财富(000001, 不复权):")
    hist_df = stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616")
    print(hist_df.head())
    
    # 获取历史行情数据-东方财富(前复权)
    print("\n5.2 历史行情数据-东方财富(000001, 前复权):")
    hist_qfq_df = stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616", adjust="qfq")
    print(hist_qfq_df.head())
    
    # 获取历史行情数据-东方财富(后复权)
    print("\n5.3 历史行情数据-东方财富(000001, 后复权):")
    hist_hfq_df = stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616", adjust="hfq")
    print(hist_hfq_df.head())
    
    # 获取历史行情数据-新浪
    print("\n5.4 历史行情数据-新浪(sh600000):")
    daily_df = stock_zh_a_daily(symbol="sh600000", start_date="20201103", end_date="20201116")
    print(daily_df.head())
    
    # 获取历史行情数据-腾讯
    print("\n5.5 历史行情数据-腾讯(sh000919):")
    hist_tx_df = stock_zh_a_hist_tx(symbol="sh000919", start_date="20201103", end_date="20201116")
    print(hist_tx_df.head())
    
    # 6. 分时数据接口测试
    print("\n=== 6. 分时数据接口测试 ===")
    
    # 获取分时数据-新浪
    print("\n6.1 分时数据-新浪(sh600519, 1分钟):")
    minute_df = stock_zh_a_minute(symbol="sh600519", period="1")
    print(minute_df.head())
    
    # 获取分时数据-东方财富
    print("\n6.2 分时数据-东方财富(603777, 1分钟):")
    hist_min_df = stock_zh_a_hist_min_em(
        symbol="603777", 
        period="1", 
        start_date="2021-09-01 09:30:00", 
        end_date="2021-09-01 15:00:00"
    )
    print(hist_min_df.head())
    
    # 获取日内分时数据-东方财富
    print("\n6.3 日内分时数据-东方财富(000001):")
    intraday_em_df = stock_intraday_em(symbol="000001")
    print(intraday_em_df.head())
    
    # 获取日内分时数据-新浪
    print("\n6.4 日内分时数据-新浪(sz000001):")
    intraday_sina_df = stock_intraday_sina(symbol="sz000001")
    print(intraday_sina_df.head())
    
    # 获取盘前数据-东方财富
    print("\n6.5 盘前数据-东方财富(603777):")
    pre_min_df = stock_zh_a_hist_pre_min_em(symbol="603777")
    print(pre_min_df.head())
    
    # 7. 历史分笔数据接口测试
    print("\n=== 7. 历史分笔数据接口测试 ===")
    
    # 获取历史分笔数据-腾讯
    print("\n7.1 历史分笔数据-腾讯(sz300494, 20210316):")
    tick_tx_df = stock_zh_a_tick_tx(symbol="sz300494", trade_date="20210316")
    print(tick_tx_df.head())
    
    print("\n=== 所有A股数据接口测试完成 ===")

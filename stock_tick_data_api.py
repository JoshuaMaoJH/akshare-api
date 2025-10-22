# -*- coding: utf-8 -*-
"""
AKTools API调用 - 历史分笔数据相关接口
基于AKShare股票数据接口完整文档编写
"""

import requests
import pandas as pd


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


# 示例调用
if __name__ == "__main__":
    print("=== 历史分笔数据接口测试 ===")
    
    # 获取历史分笔数据-腾讯
    print("\n1. 历史分笔数据-腾讯(sz300494, 20210316):")
    tick_tx_df = stock_zh_a_tick_tx(symbol="sz300494", trade_date="20210316")
    print(tick_tx_df.head())

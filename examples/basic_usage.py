# -*- coding: utf-8 -*-
"""
AKTools API调用 - 基础使用示例
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stock_a_share_api_complete import *


def basic_usage_example():
    """基础使用示例"""
    print("=== AKTools API 基础使用示例 ===")
    
    # 1. 获取市场总貌数据
    print("\n1. 获取市场总貌数据:")
    sse_summary = stock_sse_summary()
    print(f"上海证券交易所总貌数据: {len(sse_summary)} 条记录")
    
    # 2. 获取实时行情数据
    print("\n2. 获取实时行情数据:")
    spot_data = stock_zh_a_spot_em()
    print(f"沪深京A股实时行情: {len(spot_data)} 只股票")
    
    # 3. 获取历史行情数据
    print("\n3. 获取历史行情数据:")
    hist_data = stock_zh_a_hist(symbol="000001", period="daily", 
                               start_date="20230101", end_date="20230131")
    print(f"平安银行历史数据: {len(hist_data)} 条记录")
    
    # 4. 获取分时数据
    print("\n4. 获取分时数据:")
    minute_data = stock_zh_a_minute(symbol="sh600519", period="1")
    print(f"贵州茅台1分钟分时数据: {len(minute_data)} 条记录")


if __name__ == "__main__":
    basic_usage_example()

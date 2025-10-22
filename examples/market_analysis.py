# -*- coding: utf-8 -*-
"""
AKTools API调用 - 市场分析示例
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stock_a_share_api_complete import *


def market_analysis_example():
    """市场分析示例"""
    print("=== 股票市场分析示例 ===")
    
    # 1. 获取实时行情数据
    print("\n1. 获取实时行情数据...")
    spot_data = stock_zh_a_spot_em()
    
    if spot_data.empty:
        print("未能获取到实时行情数据")
        return
    
    # 2. 市场概况分析
    print("\n2. 市场概况分析:")
    print(f"   总股票数: {len(spot_data)}")
    print(f"   上涨股票: {len(spot_data[spot_data['涨跌幅'] > 0])}")
    print(f"   下跌股票: {len(spot_data[spot_data['涨跌幅'] < 0])}")
    print(f"   平盘股票: {len(spot_data[spot_data['涨跌幅'] == 0])}")
    print(f"   平均涨跌幅: {spot_data['涨跌幅'].mean():.2f}%")
    print(f"   最大涨幅: {spot_data['涨跌幅'].max():.2f}%")
    print(f"   最大跌幅: {spot_data['涨跌幅'].min():.2f}%")
    
    # 3. 成交量分析
    print("\n3. 成交量分析:")
    print(f"   总成交量: {spot_data['成交量'].sum():,.0f} 手")
    print(f"   平均成交量: {spot_data['成交量'].mean():,.0f} 手")
    print(f"   成交量中位数: {spot_data['成交量'].median():,.0f} 手")
    
    # 4. 涨跌幅分布
    print("\n4. 涨跌幅分布:")
    gain_ranges = [
        (10, float('inf'), "涨停"),
        (5, 10, "大涨(5%-10%)"),
        (0, 5, "上涨(0%-5%)"),
        (-5, 0, "下跌(-5%-0%)"),
        (-10, -5, "大跌(-10%--5%)"),
        (float('-inf'), -10, "跌停")
    ]
    
    for min_val, max_val, label in gain_ranges:
        if max_val == float('inf'):
            count = len(spot_data[spot_data['涨跌幅'] >= min_val])
        elif min_val == float('-inf'):
            count = len(spot_data[spot_data['涨跌幅'] < max_val])
        else:
            count = len(spot_data[(spot_data['涨跌幅'] >= min_val) & (spot_data['涨跌幅'] < max_val)])
        print(f"   {label}: {count} 只")
    
    # 5. 热门股票排行
    print("\n5. 成交量前10的股票:")
    top_volume = spot_data.nlargest(10, '成交量')[['代码', '名称', '最新价', '涨跌幅', '成交量']]
    print(top_volume.to_string(index=False))
    
    # 6. 涨幅前10的股票
    print("\n6. 涨幅前10的股票:")
    top_gain = spot_data.nlargest(10, '涨跌幅')[['代码', '名称', '最新价', '涨跌幅', '成交量']]
    print(top_gain.to_string(index=False))
    
    # 7. 跌幅前10的股票
    print("\n7. 跌幅前10的股票:")
    top_loss = spot_data.nsmallest(10, '涨跌幅')[['代码', '名称', '最新价', '涨跌幅', '成交量']]
    print(top_loss.to_string(index=False))


def sector_analysis_example():
    """板块分析示例"""
    print("\n=== 板块分析示例 ===")
    
    # 1. 获取各板块实时行情
    print("\n1. 获取各板块实时行情...")
    
    # 创业板
    cy_data = stock_cy_a_spot_em()
    if not cy_data.empty:
        print(f"创业板: {len(cy_data)} 只股票, 平均涨跌幅: {cy_data['涨跌幅'].mean():.2f}%")
    
    # 科创板
    kc_data = stock_kc_a_spot_em()
    if not kc_data.empty:
        print(f"科创板: {len(kc_data)} 只股票, 平均涨跌幅: {kc_data['涨跌幅'].mean():.2f}%")
    
    # 京A股
    bj_data = stock_bj_a_spot_em()
    if not bj_data.empty:
        print(f"京A股: {len(bj_data)} 只股票, 平均涨跌幅: {bj_data['涨跌幅'].mean():.2f}%")


if __name__ == "__main__":
    market_analysis_example()
    sector_analysis_example()

# -*- coding: utf-8 -*-
"""
AKTools API调用 - 数据可视化示例
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stock_a_share_api_complete import *
import matplotlib.pyplot as plt
import pandas as pd


def data_visualization_example():
    """数据可视化示例"""
    print("=== 数据可视化示例 ===")
    
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 1. 获取实时行情数据
    print("\n1. 获取实时行情数据...")
    spot_data = stock_zh_a_spot_em()
    
    if spot_data.empty:
        print("未能获取到实时行情数据")
        return
    
    # 2. 涨跌幅分布直方图
    print("\n2. 绘制涨跌幅分布直方图...")
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.hist(spot_data['涨跌幅'], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('股票涨跌幅分布')
    plt.xlabel('涨跌幅 (%)')
    plt.ylabel('股票数量')
    plt.grid(True, alpha=0.3)
    
    # 3. 成交量分布直方图
    print("\n3. 绘制成交量分布直方图...")
    plt.subplot(2, 2, 2)
    plt.hist(spot_data['成交量'], bins=50, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.title('股票成交量分布')
    plt.xlabel('成交量 (手)')
    plt.ylabel('股票数量')
    plt.yscale('log')  # 使用对数坐标
    plt.grid(True, alpha=0.3)
    
    # 4. 涨跌幅与成交量散点图
    print("\n4. 绘制涨跌幅与成交量散点图...")
    plt.subplot(2, 2, 3)
    plt.scatter(spot_data['涨跌幅'], spot_data['成交量'], alpha=0.5, s=10)
    plt.title('涨跌幅与成交量关系')
    plt.xlabel('涨跌幅 (%)')
    plt.ylabel('成交量 (手)')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    
    # 5. 市值分布
    print("\n5. 绘制市值分布...")
    plt.subplot(2, 2, 4)
    plt.hist(spot_data['总市值'], bins=50, alpha=0.7, color='orange', edgecolor='black')
    plt.title('股票总市值分布')
    plt.xlabel('总市值 (元)')
    plt.ylabel('股票数量')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('market_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 6. 获取历史数据并绘制K线图
    print("\n6. 获取历史数据并绘制K线图...")
    hist_data = stock_zh_a_hist(symbol="000001", period="daily", 
                               start_date="20230101", end_date="20231231")
    
    if not hist_data.empty:
        plt.figure(figsize=(15, 8))
        
        # 绘制价格走势
        plt.subplot(2, 1, 1)
        plt.plot(hist_data['日期'], hist_data['收盘'], label='收盘价', linewidth=2)
        plt.plot(hist_data['日期'], hist_data['开盘'], label='开盘价', alpha=0.7)
        plt.plot(hist_data['日期'], hist_data['最高'], label='最高价', alpha=0.7)
        plt.plot(hist_data['日期'], hist_data['最低'], label='最低价', alpha=0.7)
        plt.title('平安银行(000001) 2023年价格走势')
        plt.xlabel('日期')
        plt.ylabel('价格 (元)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        
        # 绘制成交量
        plt.subplot(2, 1, 2)
        plt.bar(hist_data['日期'], hist_data['成交量'], alpha=0.7, color='lightblue')
        plt.title('平安银行(000001) 2023年成交量')
        plt.xlabel('日期')
        plt.ylabel('成交量')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.savefig('stock_history.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    # 7. 板块对比分析
    print("\n7. 板块对比分析...")
    sectors = {}
    
    # 获取各板块数据
    cy_data = stock_cy_a_spot_em()
    if not cy_data.empty:
        sectors['创业板'] = cy_data['涨跌幅'].mean()
    
    kc_data = stock_kc_a_spot_em()
    if not kc_data.empty:
        sectors['科创板'] = kc_data['涨跌幅'].mean()
    
    bj_data = stock_bj_a_spot_em()
    if not bj_data.empty:
        sectors['京A股'] = bj_data['涨跌幅'].mean()
    
    if sectors:
        plt.figure(figsize=(10, 6))
        sectors_df = pd.DataFrame(list(sectors.items()), columns=['板块', '平均涨跌幅'])
        bars = plt.bar(sectors_df['板块'], sectors_df['平均涨跌幅'], 
                      color=['red' if x < 0 else 'green' for x in sectors_df['平均涨跌幅']])
        plt.title('各板块平均涨跌幅对比')
        plt.xlabel('板块')
        plt.ylabel('平均涨跌幅 (%)')
        plt.grid(True, alpha=0.3)
        
        # 在柱状图上添加数值标签
        for bar, value in zip(bars, sectors_df['平均涨跌幅']):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (0.1 if value > 0 else -0.3), 
                    f'{value:.2f}%', ha='center', va='bottom' if value > 0 else 'top')
        
        plt.tight_layout()
        plt.savefig('sector_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()


if __name__ == "__main__":
    try:
        data_visualization_example()
    except ImportError as e:
        print(f"缺少必要的可视化库: {e}")
        print("请安装: pip install matplotlib")
    except Exception as e:
        print(f"可视化过程中出现错误: {e}")

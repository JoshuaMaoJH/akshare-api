# AKShare-API

基于AKTools公开API的AKShare股票数据接口Python调用库，提供完整的A股数据获取功能。

## 项目简介

本项目基于AKShare股票数据接口完整文档，通过AKTools的公开API，封装了所有A股相关的数据接口调用方法。用户可以通过简洁的Python方法调用，获取包括股票市场总貌、个股信息、行情报价、实时行情、历史行情、分时数据、历史分笔数据等在内的完整A股数据。

## 功能特点

- **接口完整**：涵盖AKShare文档中所有A股相关的数据接口（共27个接口）
- **调用简便**：通过封装的Python方法，一行代码即可获取数据
- **参数灵活**：支持多种参数配置，满足不同分析需求
- **错误处理**：内置异常处理机制，确保程序稳定运行
- **数据格式**：统一返回pandas.DataFrame格式，便于数据分析
- **文档详细**：每个接口都包含完整的参数说明和使用示例

## 支持的接口类型

### 1. 股票市场总貌 (5个接口)
- `stock_sse_summary()` - 上海证券交易所总貌数据
- `stock_szse_summary()` - 深圳证券交易所总貌数据
- `stock_szse_area_summary()` - 深圳证券交易所地区交易排序
- `stock_szse_sector_summary()` - 深圳证券交易所股票行业成交数据
- `stock_sse_deal_daily()` - 上海证券交易所每日概况数据

### 2. 个股信息查询 (2个接口)
- `stock_individual_info_em()` - 个股信息查询-东方财富
- `stock_individual_basic_info_xq()` - 个股信息查询-雪球

### 3. 行情报价 (1个接口)
- `stock_bid_ask_em()` - 行情报价-东方财富

### 4. 实时行情数据 (10个接口)
- `stock_zh_a_spot_em()` - 沪深京A股实时行情-东方财富
- `stock_sh_a_spot_em()` - 沪A股实时行情-东方财富
- `stock_sz_a_spot_em()` - 深A股实时行情-东方财富
- `stock_bj_a_spot_em()` - 京A股实时行情-东方财富
- `stock_new_a_spot_em()` - 新股实时行情-东方财富
- `stock_cy_a_spot_em()` - 创业板实时行情-东方财富
- `stock_kc_a_spot_em()` - 科创板实时行情-东方财富
- `stock_zh_ab_comparison_em()` - AB股比价-东方财富
- `stock_zh_a_spot()` - 沪深京A股实时行情-新浪
- `stock_individual_spot_xq()` - 个股实时行情-雪球

### 5. 历史行情数据 (3个接口)
- `stock_zh_a_hist()` - 历史行情数据-东方财富
- `stock_zh_a_daily()` - 历史行情数据-新浪
- `stock_zh_a_hist_tx()` - 历史行情数据-腾讯

### 6. 分时数据 (5个接口)
- `stock_zh_a_minute()` - 分时数据-新浪
- `stock_zh_a_hist_min_em()` - 分时数据-东方财富
- `stock_intraday_em()` - 日内分时数据-东方财富
- `stock_intraday_sina()` - 日内分时数据-新浪
- `stock_zh_a_hist_pre_min_em()` - 盘前数据-东方财富

### 7. 历史分笔数据 (1个接口)
- `stock_zh_a_tick_tx()` - 历史分笔数据-腾讯

## 安装指南

### 环境要求

- Python 3.7 及以上版本
- AKTools服务已启动（默认端口8080）

### 安装步骤

1. 克隆本仓库到本地：

   ```bash
   git clone https://github.com/yourusername/akshare-api.git
   cd akshare-api
   ```

2. 安装依赖库：

   ```bash
   pip install requests pandas
   ```

3. 启动AKTools服务：

   ```bash
   # 请参考AKTools官方文档启动服务
   # 默认服务地址：http://127.0.0.1:8080
   ```

## 使用说明

### 快速开始

```python
# 导入完整接口库
from stock_a_share_api_complete import *

# 获取上海证券交易所总貌数据
sse_data = stock_sse_summary()
print(sse_data.head())

# 获取所有A股实时行情
spot_data = stock_zh_a_spot_em()
print(f"共获取到 {len(spot_data)} 只股票数据")

# 获取历史行情数据（前复权）
hist_data = stock_zh_a_hist(symbol="000001", period="daily", 
                           start_date="20210301", end_date="20210616", adjust="qfq")
print(hist_data.head())
```

### 详细使用示例

#### 1. 获取市场总貌数据

```python
# 获取上海证券交易所总貌
sse_summary = stock_sse_summary()

# 获取深圳证券交易所总貌
szse_summary = stock_szse_summary()

# 获取深圳证券交易所地区交易排序
szse_area = stock_szse_area_summary()

# 获取深圳证券交易所股票行业成交数据
szse_sector = stock_szse_sector_summary(symbol="当年")
```

#### 2. 获取实时行情数据

```python
# 获取所有A股实时行情
all_stocks = stock_zh_a_spot_em()

# 获取特定板块实时行情
cy_stocks = stock_cy_a_spot_em()  # 创业板
kc_stocks = stock_kc_a_spot_em()  # 科创板
bj_stocks = stock_bj_a_spot_em()  # 京A股

# 获取个股实时行情
individual_stock = stock_individual_spot_xq(symbol="SH600000")
```

#### 3. 获取历史行情数据

```python
# 获取不复权历史数据
hist_data = stock_zh_a_hist(symbol="000001", period="daily", 
                           start_date="20210301", end_date="20210616")

# 获取前复权历史数据
hist_qfq = stock_zh_a_hist(symbol="000001", period="daily", 
                          start_date="20210301", end_date="20210616", adjust="qfq")

# 获取后复权历史数据
hist_hfq = stock_zh_a_hist(symbol="000001", period="daily", 
                          start_date="20210301", end_date="20210616", adjust="hfq")

# 获取周线数据
weekly_data = stock_zh_a_hist(symbol="000001", period="weekly", 
                             start_date="20210301", end_date="20210616")
```

#### 4. 获取分时数据

```python
# 获取1分钟分时数据
minute_1 = stock_zh_a_minute(symbol="sh600519", period="1")

# 获取5分钟分时数据
minute_5 = stock_zh_a_minute(symbol="sh600519", period="5")

# 获取日内分时数据
intraday_data = stock_intraday_em(symbol="000001")

# 获取盘前数据
pre_data = stock_zh_a_hist_pre_min_em(symbol="603777")
```

#### 5. 数据分析和保存

```python
# 获取实时行情数据
spot_data = stock_zh_a_spot_em()

# 数据分析
print(f"总股票数: {len(spot_data)}")
print(f"上涨股票: {len(spot_data[spot_data['涨跌幅'] > 0])}")
print(f"下跌股票: {len(spot_data[spot_data['涨跌幅'] < 0])}")
print(f"平均涨跌幅: {spot_data['涨跌幅'].mean():.2f}%")

# 筛选涨幅大于5%的股票
high_gain_stocks = spot_data[spot_data['涨跌幅'] > 5]
print(f"涨幅大于5%的股票有 {len(high_gain_stocks)} 只")

# 按成交量排序
volume_sorted = spot_data.sort_values('成交量', ascending=False)
print("成交量前10的股票：")
print(volume_sorted.head(10))

# 保存数据
spot_data.to_csv('stock_data.csv', index=False, encoding='utf-8-sig')
spot_data.to_excel('stock_data.xlsx', index=False)
```

### 批量数据获取

```python
import time

def batch_get_stock_data(symbols, start_date, end_date):
    """批量获取多只股票的历史数据"""
    results = {}
    for symbol in symbols:
        try:
            df = stock_zh_a_hist(symbol=symbol, start_date=start_date, end_date=end_date)
            results[symbol] = df
            print(f"成功获取 {symbol} 的数据")
            time.sleep(0.5)  # 避免请求过于频繁
        except Exception as e:
            print(f"获取 {symbol} 数据失败: {e}")
    return results

# 使用示例
symbols = ["000001", "000002", "600000", "600036"]
data_dict = batch_get_stock_data(symbols, "20230101", "20231231")
```

## 文件结构

```
akshare-api/
├── README.md                           # 项目说明文档
├── requirements.txt                    # 依赖库列表
├── stock_a_share_api_complete.py      # 完整接口汇总文件
├── stock_market_summary_api.py         # 股票市场总貌相关接口
├── stock_individual_info_api.py        # 个股信息查询相关接口
├── stock_quotes_api.py                 # 行情报价相关接口
├── stock_realtime_data_api.py          # 实时行情数据相关接口
├── stock_historical_data_api.py        # 历史行情数据相关接口
├── stock_minute_data_api.py            # 分时数据相关接口
├── stock_tick_data_api.py              # 历史分笔数据相关接口
├── AKShare股票数据接口完整文档.md       # AKShare接口文档
└── examples/                           # 使用示例目录
    ├── basic_usage.py                  # 基础使用示例
    ├── market_analysis.py              # 市场分析示例
    └── data_visualization.py           # 数据可视化示例
```

## 注意事项

### 数据源限制
- **新浪财经**: 重复运行函数会被暂时封IP，建议增加时间间隔
- **东方财富**: 数据质量高，访问无限制，推荐使用
- **腾讯证券**: 数据稳定，但接口相对较少

### 参数格式
- **日期格式**: 通常使用"YYYYMMDD"格式，如"20210301"
- **分时数据**: 使用"YYYY-MM-DD HH:MM:SS"格式
- **股票代码**: A股使用6位数字，如"000001"

### 复权数据说明
- **不复权**: 默认返回原始价格数据
- **前复权(qfq)**: 保持当前价格不变，调整历史价格
- **后复权(hfq)**: 保持历史价格不变，调整当前价格

## 错误处理

所有接口都内置了异常处理机制：

```python
try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
    return pd.DataFrame()
```

## 贡献指南

欢迎对本项目提出建议或贡献代码：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 许可证

本项目采用 MIT 许可证进行授权，详情请参阅 [LICENSE](LICENSE) 文件。

## 致谢

- 感谢 [AKShare](https://github.com/akfamily/akshare) 项目提供的数据接口
- 感谢 [AKTools](https://github.com/akfamily/aktools) 项目提供的API服务

## 联系方式

- 项目地址：https://github.com/yourusername/akshare-api
- 问题反馈：https://github.com/yourusername/akshare-api/issues

如有任何问题或建议，欢迎通过Issue与我们联系。

---

**注意**: 使用前请确保AKTools服务已正确启动，并遵守相关数据源的使用条款。

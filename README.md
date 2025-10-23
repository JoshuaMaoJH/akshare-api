# AKShare-API

基于AKTools公开API的AKShare股票数据接口Python调用库，提供完整的股票数据获取功能。

## 项目简介

本项目基于AKShare股票数据接口完整文档，通过AKTools的公开API，封装了所有股票相关的数据接口调用方法。用户可以通过简洁的Python方法调用，获取包括A股、B股、港股、美股等各类市场的完整数据，涵盖市场总貌、个股信息、行情报价、实时行情、历史行情、分时数据、历史分笔数据、基本面数据、资金流向、概念板块、行业分析等全方位数据。

## 功能特点

- **接口完整**：涵盖AKShare文档中所有股票相关的数据接口（共98个接口）
- **市场全面**：支持A股、B股、港股、美股等多个市场
- **功能丰富**：包含实时行情、历史数据、基本面分析、资金流向等高级功能
- **调用简便**：通过封装的Python方法，一行代码即可获取数据
- **参数灵活**：支持多种参数配置，满足不同分析需求
- **错误处理**：内置异常处理机制，确保程序稳定运行
- **数据格式**：统一返回pandas.DataFrame格式，便于数据分析
- **文档详细**：每个接口都包含完整的参数说明和使用示例

## 支持的接口类型

### 📊 接口统计总览

| 分类 | 接口数量 | 说明 |
|------|----------|------|
| **A股数据接口** | 47个 | 包含市场总貌、个股信息、实时行情、历史数据、分时数据等 |
| **B股数据接口** | 4个 | B股实时行情、历史数据、分时数据 |
| **港股数据接口** | 3个 | 港股实时行情、历史数据 |
| **美股数据接口** | 3个 | 美股实时行情、历史数据 |
| **其他功能接口** | 4个 | 股票比较分析相关接口 |
| **特殊功能接口** | 1个 | CDR历史数据 |
| **高级功能接口** | 36个 | 基本面数据、资金流向、概念板块、行业分析等 |
| **总计** | **98个** | **完整的股票数据接口库** |

### 🏢 A股数据接口 (47个)

#### 1.1 股票市场总貌 (5个接口)
- `stock_sse_summary()` - 上海证券交易所总貌数据
- `stock_szse_summary()` - 深圳证券交易所总貌数据
- `stock_szse_area_summary()` - 深圳证券交易所地区交易排序
- `stock_szse_sector_summary()` - 深圳证券交易所股票行业成交数据
- `stock_sse_deal_daily()` - 上海证券交易所每日概况数据

#### 1.2 个股信息查询 (2个接口)
- `stock_individual_info_em()` - 个股信息查询-东方财富
- `stock_individual_basic_info_xq()` - 个股信息查询-雪球

#### 1.3 行情报价 (1个接口)
- `stock_bid_ask_em()` - 行情报价-东方财富

#### 1.4 实时行情数据 (10个接口)
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

#### 1.5 历史行情数据 (3个接口)
- `stock_zh_a_hist()` - 历史行情数据-东方财富
- `stock_zh_a_daily()` - 历史行情数据-新浪
- `stock_zh_a_hist_tx()` - 历史行情数据-腾讯

#### 1.6 分时数据 (5个接口)
- `stock_zh_a_minute()` - 分时数据-新浪
- `stock_zh_a_hist_min_em()` - 分时数据-东方财富
- `stock_intraday_em()` - 日内分时数据-东方财富
- `stock_intraday_sina()` - 日内分时数据-新浪
- `stock_zh_a_hist_pre_min_em()` - 盘前数据-东方财富

#### 1.7 历史分笔数据 (1个接口)
- `stock_zh_a_tick_tx()` - 历史分笔数据-腾讯

#### 1.8 其他A股相关接口 (20个)
- `stock_zh_growth_comparison_em()` - 股票成长性比较
- `stock_zh_valuation_comparison_em()` - 股票估值比较
- `stock_zh_dupont_comparison_em()` - 股票杜邦分析比较
- `stock_zh_scale_comparison_em()` - 股票规模比较
- `stock_zh_a_cdr_daily()` - CDR历史数据
- `stock_financial_abstract()` - 财务报表数据
- `stock_financial_analysis_indicator()` - 财务指标数据
- `stock_yjbb_em()` - 业绩报表数据
- `stock_hsgt_fund_flow_summary_em()` - 沪深港通资金流向
- `stock_individual_fund_flow_rank()` - 个股资金流向
- `stock_profit_forecast_em()` - 东方财富盈利预测
- `stock_profit_forecast_ths()` - 同花顺盈利预测
- `stock_board_concept_cons_ths()` - 同花顺概念板块指数
- `stock_board_concept_name_em()` - 东方财富概念板块
- `stock_board_concept_hist_em()` - 概念板块历史行情
- `stock_board_industry_name_ths()` - 同花顺行业一览表
- `stock_board_industry_name_em()` - 东方财富行业板块
- `stock_hot_rank_em()` - 股票热度排行
- `stock_market_activity_em()` - 盘口异动数据
- `stock_board_change_em()` - 板块异动详情

### 🌍 其他市场数据接口

#### 2. B股数据接口 (4个)
- `stock_zh_b_spot_em()` - B股实时行情-东方财富
- `stock_zh_b_spot()` - B股实时行情-新浪
- `stock_zh_b_daily()` - B股历史行情数据-新浪
- `stock_zh_b_minute()` - B股分时数据-新浪

#### 3. 港股数据接口 (3个)
- `stock_hk_spot_em()` - 港股实时行情-东方财富
- `stock_hk_spot()` - 港股实时行情-新浪
- `stock_hk_daily()` - 港股历史行情数据-新浪

#### 4. 美股数据接口 (3个)
- `stock_us_spot()` - 美股实时行情-新浪
- `stock_us_spot_em()` - 美股实时行情-东方财富
- `stock_us_daily()` - 美股历史行情数据-新浪

### 🔥 高级功能接口 (36个)

#### 涨停板行情 (3个)
- `stock_zt_pool_em()` - 涨停股池
- `stock_zt_pool_previous_em()` - 昨日涨停股池
- `stock_dt_pool_em()` - 跌停股池

#### 龙虎榜 (2个)
- `stock_lhb_detail_em()` - 龙虎榜详情
- `stock_lhb_stock_statistic_em()` - 个股上榜统计

#### 机构相关 (5个)
- `stock_institute_visit_em()` - 机构调研统计
- `stock_institute_visit_detail_em()` - 机构调研详细
- `stock_institute_hold_detail()` - 机构持股详情
- `stock_institute_recommend()` - 机构推荐池
- `stock_institute_recommend_detail()` - 股票评级记录

#### 研报资讯 (6个)
- `stock_research_report_em()` - 个股研报
- `stock_info_cjzc_em()` - 财经早餐
- `stock_info_global_em()` - 全球财经快讯-东方财富
- `stock_info_global_sina()` - 全球财经快讯-新浪财经
- `stock_news_em()` - 个股新闻-东方财富
- `stock_news_main_cx()` - 财经内容精选-财新网

#### 互动易 (3个)
- `stock_irm_cninfo()` - 互动易-提问
- `stock_irm_ans_cninfo()` - 互动易-回答
- `stock_sns_sseinfo()` - 上证e互动

#### 其他高级功能 (17个)
- `stock_zyjs_ths()` - 主营介绍-同花顺
- `stock_zygc_em()` - 主营构成-东方财富
- `stock_gsrl_gsdt_em()` - 公司动态-东方财富
- `stock_dividend_cninfo()` - 历史分红-巨潮资讯
- `stock_financial_report_sina()` - 财务报表-新浪
- `stock_yjkb_em()` - 业绩快报-东方财富
- `stock_yjyg_em()` - 业绩预告-东方财富
- `stock_yysj_em()` - 预约披露时间-东方财富
- `stock_board_concept_cons_em()` - 概念板块成分股-东方财富
- `stock_board_industry_cons_em()` - 行业板块成分股-东方财富
- `stock_board_industry_hist_em()` - 行业板块指数-东方财富
- `stock_hot_follow_xq()` - 股票热度-雪球关注排行榜
- `stock_hot_rank_detail_em()` - 历史趋势及粉丝特征-东方财富
- `stock_hot_rank_detail_xq()` - 个股人气榜-实时变动
- `stock_hot_rank_latest_em()` - 个股人气榜-最新排名
- `stock_hot_keyword_em()` - 热门关键词-东方财富
- `stock_hot_search_em()` - 热搜股票-东方财富
- `stock_hot_related_em()` - 相关股票-东方财富

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
# 方法1：导入完整接口库（推荐）
from akshare_api import *

# 方法2：导入原有分类文件
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

# 获取港股实时行情
hk_data = stock_hk_spot_em()
print(f"共获取到 {len(hk_data)} 只港股数据")

# 获取美股实时行情
us_data = stock_us_spot_em()
print(f"共获取到 {len(us_data)} 只美股数据")

# 获取概念板块数据
concept_data = stock_board_concept_name_em()
print(f"共获取到 {len(concept_data)} 个概念板块")

# 获取涨停股池
zt_data = stock_zt_pool_em()
print(f"今日涨停股票 {len(zt_data)} 只")
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
├── akshare-api.py                      # 🆕 完整98个接口汇总文件（推荐使用）
├── stock_a_share_api_complete.py      # A股完整接口汇总文件
├── stock_market_summary_api.py         # 股票市场总貌相关接口
├── stock_individual_info_api.py        # 个股信息查询相关接口
├── stock_quotes_api.py                 # 行情报价相关接口
├── stock_realtime_data_api.py          # 实时行情数据相关接口
├── stock_historical_data_api.py        # 历史行情数据相关接口
├── stock_minute_data_api.py            # 分时数据相关接口
├── stock_tick_data_api.py              # 历史分笔数据相关接口
├── AKShare股票数据接口完整文档.md       # AKShare接口完整文档
├── Git操作指南.md                       # Git操作指南
├── aktools官方文档.md                   # AKTools官方文档
└── examples/                           # 使用示例目录
    ├── basic_usage.py                  # 基础使用示例
    ├── market_analysis.py              # 市场分析示例
    └── data_visualization.py           # 数据可视化示例
```

### 📁 文件说明

- **akshare-api.py** 🆕: 包含所有98个接口的完整实现文件，推荐使用
- **stock_a_share_api_complete.py**: A股相关接口的汇总文件
- **AKShare股票数据接口完整文档.md**: 详细的接口文档和使用说明
- **examples/**: 包含各种使用示例的目录

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

## 更新日志

### 🆕 v2.0.0 (最新版本)

**重大更新**：完整98个接口实现

#### ✨ 新增功能
- 🎉 **完整接口库**：新增 `akshare-api.py` 文件，包含所有98个AKShare接口
- 🌍 **多市场支持**：新增B股、港股、美股数据接口
- 🔥 **高级功能**：新增涨停板、龙虎榜、机构调研、研报资讯等高级功能接口
- 📊 **接口统计**：完整的接口分类统计和使用说明

#### 📈 接口数量
- **A股数据接口**：47个（市场总貌、实时行情、历史数据、分时数据等）
- **B股数据接口**：4个（实时行情、历史数据、分时数据）
- **港股数据接口**：3个（实时行情、历史数据）
- **美股数据接口**：3个（实时行情、历史数据）
- **高级功能接口**：36个（基本面、资金流向、概念板块等）
- **其他功能接口**：5个（比较分析、特殊功能等）

#### 📚 文档更新
- 📖 更新完整文档，添加Python实现文件说明
- 🔍 详细的接口验证结果和重复函数列表
- 💡 使用建议和最佳实践指南

#### 🛠️ 技术改进
- 🔧 统一的接口调用格式
- ⚡ 完善的错误处理机制
- 📋 详细的参数说明和示例

### 📋 v1.0.0

**初始版本**：A股数据接口

#### ✨ 基础功能
- 🏢 A股数据接口：27个基础接口
- 📊 市场总貌、实时行情、历史数据等核心功能
- 🐍 Python封装，简单易用

---

**注意**: 使用前请确保AKTools服务已正确启动，并遵守相关数据源的使用条款。

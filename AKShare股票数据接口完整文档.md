# AKShare 股票数据接口完整文档

## 概述
AKShare 是一个开源的金融数据接口库，提供丰富的股票数据获取功能。本文档整理了所有股票相关的数据接口，包括调用方法、参数说明、用法示例和返回类型。

---

## 1. A股数据接口

### 1.1 股票市场总貌

#### 1.1.1 上海证券交易所总貌
**接口名称**: `stock_sse_summary`  
**目标地址**: http://www.sse.com.cn/market/stockdata/statistic/  
**描述**: 上海证券交易所-股票数据总貌  
**限量**: 单次返回上海证券交易所股票数据总貌  

**输入参数**:
- 无参数

**输出参数**:
- 返回实时行情数据表格

**用法示例**:
```python
import akshare as ak

stock_sse_summary_df = ak.stock_sse_summary()
print(stock_sse_summary_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.1.2 深圳证券交易所总貌
**接口名称**: `stock_szse_summary`  
**目标地址**: http://www.szse.cn/market/overview/index.html  
**描述**: 深圳证券交易所-市场总貌-证券类别统计  
**限量**: 单次返回深圳证券交易所市场总貌数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回证券类别统计数据

**用法示例**:
```python
import akshare as ak

stock_szse_summary_df = ak.stock_szse_summary()
print(stock_szse_summary_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.1.3 深圳证券交易所地区交易排序
**接口名称**: `stock_szse_area_summary`  
**目标地址**: http://www.szse.cn/market/overview/index.html  
**描述**: 深圳证券交易所-市场总貌-地区交易排序  
**限量**: 单次返回深圳证券交易所地区交易排序数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回地区交易排序数据

**用法示例**:
```python
import akshare as ak

stock_szse_area_summary_df = ak.stock_szse_area_summary()
print(stock_szse_area_summary_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.1.4 深圳证券交易所股票行业成交
**接口名称**: `stock_szse_sector_summary`  
**目标地址**: http://docs.static.szse.cn/www/market/periodical/month/W020220511355248518608.html  
**描述**: 深圳证券交易所-统计资料-股票行业成交数据  
**限量**: 单次返回深圳证券交易所股票行业成交数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="当月"; choice of {"当月", "当年"} |

**输出参数**:
- 返回股票行业成交数据

**用法示例**:
```python
import akshare as ak

stock_szse_sector_summary_df = ak.stock_szse_sector_summary(symbol="当年")
print(stock_szse_sector_summary_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.1.5 上海证券交易所每日概况
**接口名称**: `stock_sse_deal_daily`  
**目标地址**: http://www.sse.com.cn/market/stockdata/overview/day/  
**描述**: 上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况  
**限量**: 单次返回上海证券交易所每日概况数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回每日概况数据

**用法示例**:
```python
import akshare as ak

stock_sse_deal_daily_df = ak.stock_sse_deal_daily()
print(stock_sse_deal_daily_df)
```

**返回类型**: pandas.DataFrame

---

### 1.2 个股信息查询

#### 1.2.1 个股信息查询-东方财富
**接口名称**: `stock_individual_info_em`  
**目标地址**: http://quote.eastmoney.com/concept/sh603777.html?from=classic  
**描述**: 东方财富-个股-股票信息  
**限量**: 单次返回指定个股的详细信息  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="603777"; 股票代码 |

**输出参数**:
- 返回个股详细信息

**用法示例**:
```python
import akshare as ak

stock_individual_info_em_df = ak.stock_individual_info_em(symbol="000001")
print(stock_individual_info_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.2.2 个股信息查询-雪球
**接口名称**: `stock_individual_basic_info_xq`  
**目标地址**: https://xueqiu.com/snowman/S/SH601127/detail#/GSJJ  
**描述**: 雪球财经-个股-公司概况-公司简介  
**限量**: 单次返回指定个股的基本信息  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="SH601127"; 股票代码 |

**输出参数**:
- 返回个股基本信息

**用法示例**:
```python
import akshare as ak

stock_individual_basic_info_xq_df = ak.stock_individual_basic_info_xq(symbol="SH601127")
print(stock_individual_basic_info_xq_df)
```

**返回类型**: pandas.DataFrame

---

### 1.3 行情报价

#### 1.3.1 行情报价-东方财富
**接口名称**: `stock_bid_ask_em`  
**目标地址**: https://quote.eastmoney.com/sz000001.html  
**描述**: 东方财富-行情报价  
**限量**: 单次返回指定股票的行情报价数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="000001"; 股票代码 |

**输出参数**:
- 返回行情报价数据

**用法示例**:
```python
import akshare as ak

stock_bid_ask_em_df = ak.stock_bid_ask_em(symbol="000001")
print(stock_bid_ask_em_df)
```

**返回类型**: pandas.DataFrame

---

### 1.4 实时行情数据

#### 1.4.1 沪深京A股实时行情-东方财富
**接口名称**: `stock_zh_a_spot_em`  
**目标地址**: https://quote.eastmoney.com/center/gridlist.html#hs_a_board  
**描述**: 东方财富网-沪深京A股-实时行情数据  
**限量**: 单次返回所有沪深京A股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
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

**用法示例**:
```python
import akshare as ak

stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
print(stock_zh_a_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.4.2 沪A股实时行情-东方财富
**接口名称**: `stock_sh_a_spot_em`  
**目标地址**: http://quote.eastmoney.com/center/gridlist.html#sh_a_board  
**描述**: 东方财富网-沪A股-实时行情数据  
**限量**: 单次返回所有沪A股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 与沪深京A股实时行情相同的字段结构

**用法示例**:
```python
import akshare as ak

stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
print(stock_sh_a_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.4.3 深A股实时行情-东方财富
**接口名称**: `stock_sz_a_spot_em`  
**目标地址**: http://quote.eastmoney.com/center/gridlist.html#sz_a_board  
**描述**: 东方财富网-深A股-实时行情数据  
**限量**: 单次返回所有深A股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 与沪深京A股实时行情相同的字段结构

**用法示例**:
```python
import akshare as ak

stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
print(stock_sz_a_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.4.4 京A股实时行情-东方财富
**接口名称**: `stock_bj_a_spot_em`  
**目标地址**: http://quote.eastmoney.com/center/gridlist.html#bj_a_board  
**描述**: 东方财富网-京A股-实时行情数据  
**限量**: 单次返回所有京A股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 与沪深京A股实时行情相同的字段结构

**用法示例**:
```python
import akshare as ak

stock_bj_a_spot_em_df = ak.stock_bj_a_spot_em()
print(stock_bj_a_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.4.5 新股实时行情-东方财富
**接口名称**: `stock_new_a_spot_em`  
**目标地址**: http://quote.eastmoney.com/center/gridlist.html#newshares  
**描述**: 东方财富网-新股-实时行情数据  
**限量**: 单次返回所有新股的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 与沪深京A股实时行情相同的字段结构

**用法示例**:
```python
import akshare as ak

stock_new_a_spot_em_df = ak.stock_new_a_spot_em()
print(stock_new_a_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.4.6 创业板实时行情-东方财富
**接口名称**: `stock_cy_a_spot_em`  
**目标地址**: https://quote.eastmoney.com/center/gridlist.html#gem_board  
**描述**: 东方财富网-创业板-实时行情  
**限量**: 单次返回所有创业板股票的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 与沪深京A股实时行情相同的字段结构

**用法示例**:
```python
import akshare as ak

stock_cy_a_spot_em_df = ak.stock_cy_a_spot_em()
print(stock_cy_a_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.4.7 科创板实时行情-东方财富
**接口名称**: `stock_kc_a_spot_em`  
**目标地址**: http://quote.eastmoney.com/center/gridlist.html#kcb_board  
**描述**: 东方财富网-科创板-实时行情  
**限量**: 单次返回所有科创板股票的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 与沪深京A股实时行情相同的字段结构

**用法示例**:
```python
import akshare as ak

stock_kc_a_spot_em_df = ak.stock_kc_a_spot_em()
print(stock_kc_a_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.4.8 AB股比价-东方财富
**接口名称**: `stock_zh_ab_comparison_em`  
**目标地址**: https://quote.eastmoney.com/center/gridlist.html#ab_comparison  
**描述**: 东方财富网-行情中心-沪深京个股-AB股比价-全部AB股比价  
**限量**: 单次返回所有AB股比价数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回AB股比价数据

**用法示例**:
```python
import akshare as ak

stock_zh_ab_comparison_em_df = ak.stock_zh_ab_comparison_em()
print(stock_zh_ab_comparison_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.4.9 沪深京A股实时行情-新浪
**接口名称**: `stock_zh_a_spot`  
**目标地址**: https://vip.stock.finance.sina.com.cn/mkt/#hs_a  
**描述**: 新浪财经-沪深京A股数据, 重复运行本函数会被新浪暂时封IP, 建议增加时间间隔  
**限量**: 单次返回所有沪深京A股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回实时行情数据

**用法示例**:
```python
import akshare as ak

stock_zh_a_spot_df = ak.stock_zh_a_spot()
print(stock_zh_a_spot_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.4.10 个股实时行情-雪球
**接口名称**: `stock_individual_spot_xq`  
**目标地址**: https://xueqiu.com/S/SH513520  
**描述**: 雪球-行情中心-个股  
**限量**: 单次返回指定个股的实时行情数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="SH600000"; 证券代码，可以是A股个股代码，A股场内基金代码，A股指数，美股代码, 美股指数 |

**输出参数**:
- 返回个股实时行情数据

**用法示例**:
```python
import akshare as ak

stock_individual_spot_xq_df = ak.stock_individual_spot_xq(symbol="SH600000")
print(stock_individual_spot_xq_df)
```

**返回类型**: pandas.DataFrame

---

### 1.5 历史行情数据

#### 1.5.1 历史行情数据-东方财富
**接口名称**: `stock_zh_a_hist`  
**目标地址**: https://quote.eastmoney.com/concept/sh603777.html?from=classic(示例)  
**描述**: 东方财富-沪深京A股日频率数据; 历史数据按日频率更新, 当日收盘价请在收盘后获取  
**限量**: 单次返回指定沪深京A股上市公司、指定周期和指定日期间的历史行情日频率数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol='603777'; 股票代码可以在ak.stock_zh_a_spot_em()中获取 |
| period | str | period='daily'; choice of {'daily', 'weekly', 'monthly'} |
| start_date | str | start_date='20210301'; 开始查询的日期 |
| end_date | str | end_date='20210616'; 结束查询的日期 |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |
| timeout | float | timeout=None; 默认不设置超时参数 |

**输出参数**:
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

**用法示例**:
```python
import akshare as ak

# 获取不复权数据
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616")
print(stock_zh_a_hist_df)

# 获取前复权数据
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616", adjust="qfq")
print(stock_zh_a_hist_df)

# 获取后复权数据
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616", adjust="hfq")
print(stock_zh_a_hist_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.5.2 历史行情数据-新浪
**接口名称**: `stock_zh_a_daily`  
**目标地址**: https://finance.sina.com.cn/realstock/company/sh600006/nc.shtml(示例)  
**描述**: 新浪财经-沪深京A股的数据, 历史数据按日频率更新; 注意其中的sh689009为CDR, 请通过ak.stock_zh_a_cdr_daily接口获取  
**限量**: 单次返回指定沪深京A股上市公司指定日期间的历史行情日频率数据, 多次获取容易封禁IP  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol='sh600000'; 股票代码可以在ak.stock_zh_a_spot()中获取 |
| start_date | str | start_date='20201103'; 开始查询的日期 |
| end_date | str | end_date='20201116'; 结束查询的日期 |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子 |

**输出参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| date | object | 交易日 |
| open | float64 | 开盘价 |
| high | float64 | 最高价 |
| low | float64 | 最低价 |
| close | float64 | 收盘价 |
| volume | float64 | 成交量; 注意单位: 股 |
| amount | float64 | 成交额; 注意单位: 元 |

**用法示例**:
```python
import akshare as ak

stock_zh_a_daily_df = ak.stock_zh_a_daily(symbol="sh600000", start_date="20201103", end_date="20201116")
print(stock_zh_a_daily_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.5.3 历史行情数据-腾讯
**接口名称**: `stock_zh_a_hist_tx`  
**目标地址**: https://gu.qq.com/sh000919/zs  
**描述**: 腾讯证券-日频-股票历史数据; 历史数据按日频率更新, 当日收盘价请在收盘后获取  
**限量**: 单次返回指定沪深京A股上市公司指定日期间的历史行情日频率数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="sh000919"; 股票代码 |
| start_date | str | start_date="20201103"; 开始查询的日期 |
| end_date | str | end_date="20201116"; 结束查询的日期 |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |

**输出参数**:
- 返回历史行情数据

**用法示例**:
```python
import akshare as ak

stock_zh_a_hist_tx_df = ak.stock_zh_a_hist_tx(symbol="sh000919", start_date="20201103", end_date="20201116")
print(stock_zh_a_hist_tx_df)
```

**返回类型**: pandas.DataFrame

---

### 1.6 分时数据

#### 1.6.1 分时数据-新浪
**接口名称**: `stock_zh_a_minute`  
**目标地址**: http://finance.sina.com.cn/realstock/company/sh600519/nc.shtml  
**描述**: 新浪财经-沪深京A股股票或者指数的分时数据，目前可以获取1, 5, 15, 30, 60分钟的数据频率, 可以指定是否复权  
**限量**: 单次返回指定沪深京A股上市公司指定日期间的分时数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="sh600519"; 股票代码 |
| period | str | period="1"; choice of {"1", "5", "15", "30", "60"} |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |

**输出参数**:
- 返回分时数据

**用法示例**:
```python
import akshare as ak

stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol="sh600519", period="1")
print(stock_zh_a_minute_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.6.2 分时数据-东方财富
**接口名称**: `stock_zh_a_hist_min_em`  
**目标地址**: https://quote.eastmoney.com/concept/sh603777.html  
**描述**: 东方财富网-行情首页-沪深京A股-每日分时行情; 该接口只能获取近期的分时数据，注意时间周期的设置  
**限量**: 单次返回指定沪深京A股上市公司指定日期间的分时数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="603777"; 股票代码 |
| period | str | period="1"; choice of {"1", "5", "15", "30", "60"} |
| start_date | str | start_date="2021-09-01 09:30:00"; 开始查询的日期 |
| end_date | str | end_date="2021-09-01 15:00:00"; 结束查询的日期 |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |

**输出参数**:
- 返回分时数据

**用法示例**:
```python
import akshare as ak

stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol="603777", period="1", start_date="2021-09-01 09:30:00", end_date="2021-09-01 15:00:00")
print(stock_zh_a_hist_min_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.6.3 日内分时数据-东方财富
**接口名称**: `stock_intraday_em`  
**目标地址**: https://quote.eastmoney.com/f1.html?newcode=0.000001  
**描述**: 东方财富-分时数据  
**限量**: 单次返回指定股票的日内分时数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="000001"; 股票代码 |

**输出参数**:
- 返回日内分时数据

**用法示例**:
```python
import akshare as ak

stock_intraday_em_df = ak.stock_intraday_em(symbol="000001")
print(stock_intraday_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.6.4 日内分时数据-新浪
**接口名称**: `stock_intraday_sina`  
**目标地址**: https://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill.php?symbol=sz000001  
**描述**: 新浪财经-日内分时数据  
**限量**: 单次返回指定股票的日内分时数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="sz000001"; 股票代码 |

**输出参数**:
- 返回日内分时数据

**用法示例**:
```python
import akshare as ak

stock_intraday_sina_df = ak.stock_intraday_sina(symbol="sz000001")
print(stock_intraday_sina_df)
```

**返回类型**: pandas.DataFrame

---

#### 1.6.5 盘前数据-东方财富
**接口名称**: `stock_zh_a_hist_pre_min_em`  
**目标地址**: https://quote.eastmoney.com/concept/sh603777.html  
**描述**: 东方财富-股票行情-盘前数据  
**限量**: 单次返回指定股票的盘前数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="603777"; 股票代码 |

**输出参数**:
- 返回盘前数据

**用法示例**:
```python
import akshare as ak

stock_zh_a_hist_pre_min_em_df = ak.stock_zh_a_hist_pre_min_em(symbol="603777")
print(stock_zh_a_hist_pre_min_em_df)
```

**返回类型**: pandas.DataFrame

---

### 1.7 历史分笔数据

#### 1.7.1 历史分笔数据-腾讯
**接口名称**: `stock_zh_a_tick_tx`  
**目标地址**: http://gu.qq.com/sz300494/gp/detail(示例)  
**描述**: 每个交易日16:00提供当日数据; 如遇到数据缺失, 请使用ak.stock_zh_a_tick_163()接口(注意数据会有一定差异)  
**限量**: 单次返回指定股票的历史分笔数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="sz300494"; 股票代码 |
| trade_date | str | trade_date="20210316"; 交易日期 |

**输出参数**:
- 返回历史分笔数据

**用法示例**:
```python
import akshare as ak

stock_zh_a_tick_tx_df = ak.stock_zh_a_tick_tx(symbol="sz300494", trade_date="20210316")
print(stock_zh_a_tick_tx_df)
```

**返回类型**: pandas.DataFrame

---

## 2. B股数据接口

### 2.1 B股实时行情-东方财富
**接口名称**: `stock_zh_b_spot_em`  
**目标地址**: https://quote.eastmoney.com/center/gridlist.html#hs_b_board  
**描述**: 东方财富网-沪深B股-实时行情数据  
**限量**: 单次返回所有沪深B股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回B股实时行情数据

**用法示例**:
```python
import akshare as ak

stock_zh_b_spot_em_df = ak.stock_zh_b_spot_em()
print(stock_zh_b_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

### 2.2 B股实时行情-新浪
**接口名称**: `stock_zh_b_spot`  
**目标地址**: https://vip.stock.finance.sina.com.cn/mkt/#hs_b  
**描述**: 新浪财经-沪深B股数据  
**限量**: 单次返回所有沪深B股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回B股实时行情数据

**用法示例**:
```python
import akshare as ak

stock_zh_b_spot_df = ak.stock_zh_b_spot()
print(stock_zh_b_spot_df)
```

**返回类型**: pandas.DataFrame

---

### 2.3 B股历史行情数据-新浪
**接口名称**: `stock_zh_b_daily`  
**目标地址**: https://finance.sina.com.cn/realstock/company/sh900901/nc.shtml(示例)  
**描述**: 新浪财经-沪深B股历史数据  
**限量**: 单次返回指定B股上市公司指定日期间的历史行情日频率数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol='sh900901'; 股票代码可以在ak.stock_zh_b_spot()中获取 |
| start_date | str | start_date='20201103'; 开始查询的日期 |
| end_date | str | end_date='20201116'; 结束查询的日期 |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |

**输出参数**:
- 返回B股历史行情数据

**用法示例**:
```python
import akshare as ak

stock_zh_b_daily_df = ak.stock_zh_b_daily(symbol="sh900901", start_date="20201103", end_date="20201116")
print(stock_zh_b_daily_df)
```

**返回类型**: pandas.DataFrame

---

### 2.4 B股分时数据-新浪
**接口名称**: `stock_zh_b_minute`  
**目标地址**: https://finance.sina.com.cn/realstock/company/sh900901/nc.shtml(示例)  
**描述**: 新浪财经-沪深B股分时数据  
**限量**: 单次返回指定B股上市公司指定日期间的分时数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="sh900901"; 股票代码 |
| period | str | period="1"; choice of {"1", "5", "15", "30", "60"} |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |

**输出参数**:
- 返回B股分时数据

**用法示例**:
```python
import akshare as ak

stock_zh_b_minute_df = ak.stock_zh_b_minute(symbol="sh900901", period="1")
print(stock_zh_b_minute_df)
```

**返回类型**: pandas.DataFrame

---

## 3. 港股数据接口

### 3.1 港股实时行情-东方财富
**接口名称**: `stock_hk_spot_em`  
**目标地址**: https://quote.eastmoney.com/center/gridlist.html#hk_stocks  
**描述**: 东方财富网-港股-实时行情数据  
**限量**: 单次返回所有港股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回港股实时行情数据

**用法示例**:
```python
import akshare as ak

stock_hk_spot_em_df = ak.stock_hk_spot_em()
print(stock_hk_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

### 3.2 港股实时行情-新浪
**接口名称**: `stock_hk_spot`  
**目标地址**: https://vip.stock.finance.sina.com.cn/mkt/#hk_stocks  
**描述**: 新浪财经-港股数据  
**限量**: 单次返回所有港股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回港股实时行情数据

**用法示例**:
```python
import akshare as ak

stock_hk_spot_df = ak.stock_hk_spot()
print(stock_hk_spot_df)
```

**返回类型**: pandas.DataFrame

---

### 3.3 港股历史行情数据-新浪
**接口名称**: `stock_hk_daily`  
**目标地址**: https://finance.sina.com.cn/realstock/company/hk01611/nc.shtml(示例)  
**描述**: 新浪财经-港股历史数据  
**限量**: 单次返回指定港股上市公司指定日期间的历史行情日频率数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="01611"; 港股代码可以通过ak.stock_hk_spot_em()函数返回所有的pandas.DataFrame里面的代码字段获取 |
| start_date | str | start_date="20201103"; 开始查询的日期 |
| end_date | str | end_date="20201116"; 结束查询的日期 |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |

**输出参数**:
- 返回港股历史行情数据

**用法示例**:
```python
import akshare as ak

stock_hk_daily_df = ak.stock_hk_daily(symbol="01611", start_date="20201103", end_date="20201116")
print(stock_hk_daily_df)
```

**返回类型**: pandas.DataFrame

---

## 4. 美股数据接口

### 4.1 美股实时行情-新浪
**接口名称**: `stock_us_spot`  
**目标地址**: https://vip.stock.finance.sina.com.cn/mkt/#us_stocks  
**描述**: 新浪财经-美股; 获取的数据有15分钟延迟; 建议使用ak.stock_us_spot_em()来获取数据  
**限量**: 单次返回所有美股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回美股实时行情数据

**用法示例**:
```python
import akshare as ak

stock_us_spot_df = ak.stock_us_spot()
print(stock_us_spot_df)
```

**返回类型**: pandas.DataFrame

---

### 4.2 美股实时行情-东方财富
**接口名称**: `stock_us_spot_em`  
**目标地址**: https://quote.eastmoney.com/center/gridlist.html#us_stocks  
**描述**: 东方财富网-美股-实时行情数据  
**限量**: 单次返回所有美股上市公司的实时行情数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回美股实时行情数据

**用法示例**:
```python
import akshare as ak

stock_us_spot_em_df = ak.stock_us_spot_em()
print(stock_us_spot_em_df)
```

**返回类型**: pandas.DataFrame

---

### 4.3 美股历史行情数据-新浪
**接口名称**: `stock_us_daily`  
**目标地址**: https://finance.sina.com.cn/realstock/company/usAAPL/nc.shtml(示例)  
**描述**: 新浪财经-美股历史数据  
**限量**: 单次返回指定美股上市公司指定日期间的历史行情日频率数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 美股代码, 可以通过ak.stock_us_spot_em()函数返回所有的pandas.DataFrame里面的代码字段获取 |
| start_date | str | start_date="20201103"; 开始查询的日期 |
| end_date | str | end_date="20201116"; 结束查询的日期 |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |

**输出参数**:
- 返回美股历史行情数据

**用法示例**:
```python
import akshare as ak

stock_us_daily_df = ak.stock_us_daily(symbol="AAPL", start_date="20201103", end_date="20201116")
print(stock_us_daily_df)
```

**返回类型**: pandas.DataFrame

---

## 5. 其他功能接口

### 5.1 股票成长性比较-东方财富
**接口名称**: `stock_zh_growth_comparison_em`  
**目标地址**: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/czxbj  
**描述**: 东方财富-行情中心-同行比较-成长性比较  
**限量**: 单次返回指定股票的成长性比较数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="000895"; 股票代码 |

**输出参数**:
- 返回成长性比较数据

**用法示例**:
```python
import akshare as ak

stock_zh_growth_comparison_em_df = ak.stock_zh_growth_comparison_em(symbol="000895")
print(stock_zh_growth_comparison_em_df)
```

**返回类型**: pandas.DataFrame

---

### 5.2 股票估值比较-东方财富
**接口名称**: `stock_zh_valuation_comparison_em`  
**目标地址**: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/gzbj  
**描述**: 东方财富-行情中心-同行比较-估值比较  
**限量**: 单次返回指定股票的估值比较数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="000895"; 股票代码 |

**输出参数**:
- 返回估值比较数据

**用法示例**:
```python
import akshare as ak

stock_zh_valuation_comparison_em_df = ak.stock_zh_valuation_comparison_em(symbol="000895")
print(stock_zh_valuation_comparison_em_df)
```

**返回类型**: pandas.DataFrame

---

### 5.3 股票杜邦分析比较-东方财富
**接口名称**: `stock_zh_dupont_comparison_em`  
**目标地址**: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/dpbj  
**描述**: 东方财富-行情中心-同行比较-杜邦分析比较  
**限量**: 单次返回指定股票的杜邦分析比较数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="000895"; 股票代码 |

**输出参数**:
- 返回杜邦分析比较数据

**用法示例**:
```python
import akshare as ak

stock_zh_dupont_comparison_em_df = ak.stock_zh_dupont_comparison_em(symbol="000895")
print(stock_zh_dupont_comparison_em_df)
```

**返回类型**: pandas.DataFrame

---

### 5.4 股票规模比较-东方财富
**接口名称**: `stock_zh_scale_comparison_em`  
**目标地址**: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=000895&color=b#/thbj/gmbj  
**描述**: 东方财富-行情中心-同行比较-规模比较  
**限量**: 单次返回指定股票的规模比较数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="000895"; 股票代码 |

**输出参数**:
- 返回规模比较数据

**用法示例**:
```python
import akshare as ak

stock_zh_scale_comparison_em_df = ak.stock_zh_scale_comparison_em(symbol="000895")
print(stock_zh_scale_comparison_em_df)
```

**返回类型**: pandas.DataFrame

---

## 6. 特殊功能接口

### 6.1 CDR历史数据-新浪
**接口名称**: `stock_zh_a_cdr_daily`  
**目标地址**: https://finance.sina.com.cn/realstock/company/sh689009/nc.shtml(示例)  
**描述**: 新浪财经-CDR历史数据  
**限量**: 单次返回指定CDR指定日期间的历史行情日频率数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="sh689009"; CDR代码 |
| start_date | str | start_date="20201103"; 开始查询的日期 |
| end_date | str | end_date="20201116"; 结束查询的日期 |
| adjust | str | 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据 |

**输出参数**:
- 返回CDR历史行情数据

**用法示例**:
```python
import akshare as ak

stock_zh_a_cdr_daily_df = ak.stock_zh_a_cdr_daily(symbol="sh689009", start_date="20201103", end_date="20201116")
print(stock_zh_a_cdr_daily_df)
```

**返回类型**: pandas.DataFrame

---

## 7. 使用注意事项

### 7.1 数据源限制
- **新浪财经**: 重复运行函数会被暂时封IP，建议增加时间间隔
- **东方财富**: 数据质量高，访问无限制，推荐使用
- **腾讯证券**: 数据稳定，但接口相对较少

### 7.2 复权数据说明
- **不复权**: 默认返回原始价格数据
- **前复权(qfq)**: 保持当前价格不变，调整历史价格
- **后复权(hfq)**: 保持历史价格不变，调整当前价格
- **量化研究**: 建议使用后复权数据

### 7.3 时间格式
- **日期格式**: 通常使用"YYYYMMDD"格式，如"20210301"
- **分时数据**: 使用"YYYY-MM-DD HH:MM:SS"格式
- **交易时间**: 注意A股交易时间为9:30-11:30, 13:00-15:00

### 7.4 股票代码格式
- **A股**: 6位数字，如"000001"
- **B股**: 带市场前缀，如"sh900901"
- **港股**: 5位数字，如"01611"
- **美股**: 字母代码，如"AAPL"

### 7.5 数据单位
- **价格**: 元
- **成交量**: 股或手(1手=100股)
- **成交额**: 元
- **涨跌幅**: 百分比(%)

---

## 8. 安装和使用

### 8.1 安装AKShare
```bash
pip install akshare
```

### 8.2 基本使用
```python
import akshare as ak

# 获取实时行情
df = ak.stock_zh_a_spot_em()
print(df.head())

# 获取历史数据
df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20210301", end_date="20210616")
print(df.head())
```

### 8.3 数据保存
```python
import akshare as ak
import pandas as pd

# 获取数据
df = ak.stock_zh_a_spot_em()

# 保存为CSV
df.to_csv('stock_data.csv', index=False)

# 保存为Excel
df.to_excel('stock_data.xlsx', index=False)
```

---

## 9. 高级功能接口

### 9.1 基本面数据接口

#### 9.1.1 财务报表数据
**接口名称**: `stock_financial_abstract`  
**目标地址**: 新浪财经-财务报表数据  
**描述**: 获取上市公司财务报表摘要数据  
**限量**: 单次返回指定股票的所有财务数据  

**输入参数**:
- symbol: 股票代码，如"000001"

**输出参数**:
- 返回财务报表摘要数据

**用法示例**:
```python
import akshare as ak

stock_financial_abstract_df = ak.stock_financial_abstract(symbol="000001")
print(stock_financial_abstract_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.1.2 财务指标数据
**接口名称**: `stock_financial_analysis_indicator`  
**目标地址**: 新浪财经-财务指标数据  
**描述**: 获取上市公司财务分析指标  
**限量**: 单次返回指定股票的财务指标数据  

**输入参数**:
- symbol: 股票代码，如"000001"

**输出参数**:
- 返回财务分析指标数据

**用法示例**:
```python
import akshare as ak

stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(symbol="000001")
print(stock_financial_analysis_indicator_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.1.3 业绩报表数据
**接口名称**: `stock_yjbb_em`  
**目标地址**: 东方财富网-业绩报表  
**描述**: 获取上市公司业绩报表数据  
**限量**: 单次返回所有业绩报表数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回业绩报表数据

**用法示例**:
```python
import akshare as ak

stock_yjbb_em_df = ak.stock_yjbb_em()
print(stock_yjbb_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.2 资金流向接口

#### 9.2.1 沪深港通资金流向
**接口名称**: `stock_hsgt_fund_flow_summary_em`  
**目标地址**: 东方财富网-沪深港通资金流向  
**描述**: 获取沪深港通资金流向汇总数据  
**限量**: 单次返回所有资金流向数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回沪深港通资金流向数据

**用法示例**:
```python
import akshare as ak

stock_hsgt_fund_flow_summary_em_df = ak.stock_hsgt_fund_flow_summary_em()
print(stock_hsgt_fund_flow_summary_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.2.2 个股资金流向
**接口名称**: `stock_individual_fund_flow_rank`  
**目标地址**: 东方财富网-个股资金流向排行  
**描述**: 获取个股资金流向排行数据  
**限量**: 单次返回所有个股资金流向数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回个股资金流向排行数据

**用法示例**:
```python
import akshare as ak

stock_individual_fund_flow_rank_df = ak.stock_individual_fund_flow_rank()
print(stock_individual_fund_flow_rank_df)
```

**返回类型**: pandas.DataFrame

---

### 9.3 盈利预测接口

#### 9.3.1 东方财富盈利预测
**接口名称**: `stock_profit_forecast_em`  
**目标地址**: 东方财富网-盈利预测  
**描述**: 获取上市公司盈利预测数据  
**限量**: 单次返回所有盈利预测数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回盈利预测数据

**用法示例**:
```python
import akshare as ak

stock_profit_forecast_em_df = ak.stock_profit_forecast_em()
print(stock_profit_forecast_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.3.2 同花顺盈利预测
**接口名称**: `stock_profit_forecast_ths`  
**目标地址**: 同花顺-盈利预测  
**描述**: 获取同花顺盈利预测数据  
**限量**: 单次返回所有盈利预测数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回盈利预测数据

**用法示例**:
```python
import akshare as ak

stock_profit_forecast_ths_df = ak.stock_profit_forecast_ths()
print(stock_profit_forecast_ths_df)
```

**返回类型**: pandas.DataFrame

---

### 9.4 概念板块接口

#### 9.4.1 同花顺概念板块指数
**接口名称**: `stock_board_concept_cons_ths`  
**目标地址**: 同花顺-概念板块指数  
**描述**: 获取同花顺概念板块指数数据  
**限量**: 单次返回所有概念板块指数数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回概念板块指数数据

**用法示例**:
```python
import akshare as ak

stock_board_concept_cons_ths_df = ak.stock_board_concept_cons_ths()
print(stock_board_concept_cons_ths_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.4.2 东方财富概念板块
**接口名称**: `stock_board_concept_name_em`  
**目标地址**: 东方财富网-概念板块  
**描述**: 获取东方财富概念板块名称数据  
**限量**: 单次返回所有概念板块名称数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回概念板块名称数据

**用法示例**:
```python
import akshare as ak

stock_board_concept_name_em_df = ak.stock_board_concept_name_em()
print(stock_board_concept_name_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.4.3 概念板块历史行情
**接口名称**: `stock_board_concept_hist_em`  
**目标地址**: 东方财富网-概念板块历史行情  
**描述**: 获取概念板块历史行情数据  
**限量**: 单次返回指定概念板块的历史数据  

**输入参数**:
- symbol: 概念板块名称，如"绿色电力"
- period: 周期，如"daily"
- start_date: 开始日期，如"20220101"
- end_date: 结束日期，如"20250227"
- adjust: 复权类型，如""

**输出参数**:
- 返回概念板块历史行情数据

**用法示例**:
```python
import akshare as ak

stock_board_concept_hist_em_df = ak.stock_board_concept_hist_em(
    symbol="绿色电力", 
    period="daily", 
    start_date="20220101", 
    end_date="20250227", 
    adjust=""
)
print(stock_board_concept_hist_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.5 行业板块接口

#### 9.5.1 同花顺行业一览表
**接口名称**: `stock_board_industry_name_ths`  
**目标地址**: 同花顺-行业一览表  
**描述**: 获取同花顺行业一览表数据  
**限量**: 单次返回所有行业数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回行业一览表数据

**用法示例**:
```python
import akshare as ak

stock_board_industry_name_ths_df = ak.stock_board_industry_name_ths()
print(stock_board_industry_name_ths_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.5.2 东方财富行业板块
**接口名称**: `stock_board_industry_name_em`  
**目标地址**: 东方财富网-行业板块  
**描述**: 获取东方财富行业板块数据  
**限量**: 单次返回所有行业板块数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回行业板块数据

**用法示例**:
```python
import akshare as ak

stock_board_industry_name_em_df = ak.stock_board_industry_name_em()
print(stock_board_industry_name_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.6 股票热度接口

#### 9.6.1 雪球股票热度
**接口名称**: `stock_hot_rank_em`  
**目标地址**: 东方财富网-股票热度排行  
**描述**: 获取股票热度排行数据  
**限量**: 单次返回所有股票热度数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回股票热度排行数据

**用法示例**:
```python
import akshare as ak

stock_hot_rank_em_df = ak.stock_hot_rank_em()
print(stock_hot_rank_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.7 盘口异动接口

#### 9.7.1 盘口异动数据
**接口名称**: `stock_market_activity_em`  
**目标地址**: 东方财富网-盘口异动  
**描述**: 获取盘口异动数据  
**限量**: 单次返回所有盘口异动数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回盘口异动数据

**用法示例**:
```python
import akshare as ak

stock_market_activity_em_df = ak.stock_market_activity_em()
print(stock_market_activity_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.8 板块异动详情接口

#### 9.8.1 板块异动详情
**接口名称**: `stock_board_change_em`  
**目标地址**: 东方财富网-板块异动详情  
**描述**: 获取板块异动详情数据  
**限量**: 单次返回所有板块异动数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回板块异动详情数据

**用法示例**:
```python
import akshare as ak

stock_board_change_em_df = ak.stock_board_change_em()
print(stock_board_change_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.9 涨停板行情接口

#### 9.9.1 涨停股池
**接口名称**: `stock_zt_pool_em`  
**目标地址**: 东方财富网-涨停股池  
**描述**: 获取涨停股池数据  
**限量**: 单次返回所有涨停股池数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回涨停股池数据

**用法示例**:
```python
import akshare as ak

stock_zt_pool_em_df = ak.stock_zt_pool_em()
print(stock_zt_pool_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.9.2 昨日涨停股池
**接口名称**: `stock_zt_pool_previous_em`  
**目标地址**: 东方财富网-昨日涨停股池  
**描述**: 获取昨日涨停股池数据  
**限量**: 单次返回所有昨日涨停股池数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回昨日涨停股池数据

**用法示例**:
```python
import akshare as ak

stock_zt_pool_previous_em_df = ak.stock_zt_pool_previous_em()
print(stock_zt_pool_previous_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.9.3 跌停股池
**接口名称**: `stock_dt_pool_em`  
**目标地址**: 东方财富网-跌停股池  
**描述**: 获取跌停股池数据  
**限量**: 单次返回所有跌停股池数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回跌停股池数据

**用法示例**:
```python
import akshare as ak

stock_dt_pool_em_df = ak.stock_dt_pool_em()
print(stock_dt_pool_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.10 龙虎榜接口

#### 9.10.1 龙虎榜详情
**接口名称**: `stock_lhb_detail_em`  
**目标地址**: 东方财富网-龙虎榜详情  
**描述**: 获取龙虎榜详情数据  
**限量**: 单次返回所有历史数据  

**输入参数**:
- start_date: 开始日期，如"20220314"
- end_date: 结束日期，如"20220315"

**输出参数**:
- 返回龙虎榜详情数据

**用法示例**:
```python
import akshare as ak

stock_lhb_detail_em_df = ak.stock_lhb_detail_em(
    start_date="20230403", 
    end_date="20230417"
)
print(stock_lhb_detail_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.10.2 个股上榜统计
**接口名称**: `stock_lhb_stock_statistic_em`  
**目标地址**: 东方财富网-个股上榜统计  
**描述**: 获取个股上榜统计数据  
**限量**: 单次返回所有历史数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回个股上榜统计数据

**用法示例**:
```python
import akshare as ak

stock_lhb_stock_statistic_em_df = ak.stock_lhb_stock_statistic_em()
print(stock_lhb_stock_statistic_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.11 机构调研接口

#### 9.11.1 机构调研统计
**接口名称**: `stock_institute_visit_em`  
**目标地址**: 东方财富网-机构调研统计  
**描述**: 获取机构调研统计数据  
**限量**: 单次返回所有机构调研数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回机构调研统计数据

**用法示例**:
```python
import akshare as ak

stock_institute_visit_em_df = ak.stock_institute_visit_em()
print(stock_institute_visit_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.11.2 机构调研详细
**接口名称**: `stock_institute_visit_detail_em`  
**目标地址**: 东方财富网-机构调研详细  
**描述**: 获取机构调研详细数据  
**限量**: 单次返回所有机构调研详细数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回机构调研详细数据

**用法示例**:
```python
import akshare as ak

stock_institute_visit_detail_em_df = ak.stock_institute_visit_detail_em()
print(stock_institute_visit_detail_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.12 机构持股接口

#### 9.12.1 机构持股详情
**接口名称**: `stock_institute_hold_detail`  
**目标地址**: 东方财富网-机构持股详情  
**描述**: 获取机构持股详情数据  
**限量**: 单次返回指定股票的机构持股数据  

**输入参数**:
- stock: 股票代码，如"300003"
- quarter: 季度，如"20201"

**输出参数**:
- 返回机构持股详情数据

**用法示例**:
```python
import akshare as ak

stock_institute_hold_detail_df = ak.stock_institute_hold_detail(
    stock="300003", 
    quarter="20201"
)
print(stock_institute_hold_detail_df)
```

**返回类型**: pandas.DataFrame

---

### 9.13 机构推荐接口

#### 9.13.1 机构推荐池
**接口名称**: `stock_institute_recommend`  
**目标地址**: 新浪财经-机构推荐池  
**描述**: 获取机构推荐池数据  
**限量**: 单次获取新浪财经-机构推荐池的所有数据  

**输入参数**:
- symbol: 指标类型，如"投资评级选股"

**输出参数**:
- 返回机构推荐池数据

**用法示例**:
```python
import akshare as ak

stock_institute_recommend_df = ak.stock_institute_recommend(symbol="投资评级选股")
print(stock_institute_recommend_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.13.2 股票评级记录
**接口名称**: `stock_institute_recommend_detail`  
**目标地址**: 新浪财经-股票评级记录  
**描述**: 获取股票评级记录数据  
**限量**: 单次获取新浪财经-股票评级记录的所有数据  

**输入参数**:
- symbol: 股票代码，如"000001"

**输出参数**:
- 返回股票评级记录数据

**用法示例**:
```python
import akshare as ak

stock_institute_recommend_detail_df = ak.stock_institute_recommend_detail(symbol="000001")
print(stock_institute_recommend_detail_df)
```

**返回类型**: pandas.DataFrame

---

### 9.14 个股研报接口

#### 9.14.1 个股研报
**接口名称**: `stock_research_report_em`  
**目标地址**: 东方财富网-个股研报  
**描述**: 获取个股研报数据  
**限量**: 单次返回指定股票的所有数据  

**输入参数**:
- symbol: 股票代码，如"000001"

**输出参数**:
- 返回个股研报数据

**用法示例**:
```python
import akshare as ak

stock_research_report_em_df = ak.stock_research_report_em(symbol="000001")
print(stock_research_report_em_df)
```

**返回类型**: pandas.DataFrame

---

### 9.15 资讯数据接口

#### 9.15.1 财经早餐
**接口名称**: `stock_info_cjzc_em`  
**目标地址**: 东方财富网-财经早餐  
**描述**: 获取财经早餐数据  
**限量**: 单次返回全部历史数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回财经早餐数据

**用法示例**:
```python
import akshare as ak

stock_info_cjzc_em_df = ak.stock_info_cjzc_em()
print(stock_info_cjzc_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.15.2 全球财经快讯-东方财富
**接口名称**: `stock_info_global_em`  
**目标地址**: 东方财富网-全球财经快讯  
**描述**: 获取全球财经快讯数据  
**限量**: 单次返回最近200条新闻数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回全球财经快讯数据

**用法示例**:
```python
import akshare as ak

stock_info_global_em_df = ak.stock_info_global_em()
print(stock_info_global_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.15.3 全球财经快讯-新浪财经
**接口名称**: `stock_info_global_sina`  
**目标地址**: 新浪财经-全球财经快讯  
**描述**: 获取新浪财经全球财经快讯数据  
**限量**: 单次返回最近20条新闻数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回全球财经快讯数据

**用法示例**:
```python
import akshare as ak

stock_info_global_sina_df = ak.stock_info_global_sina()
print(stock_info_global_sina_df)
```

**返回类型**: pandas.DataFrame

---

### 9.16 互动易接口

#### 9.16.1 互动易-提问
**接口名称**: `stock_irm_cninfo`  
**目标地址**: 互动易-提问  
**描述**: 获取互动易提问数据  
**限量**: 单次返回指定股票的提问数据  

**输入参数**:
- symbol: 股票代码，如"002594"

**输出参数**:
- 返回互动易提问数据

**用法示例**:
```python
import akshare as ak

stock_irm_cninfo_df = ak.stock_irm_cninfo(symbol="002594")
print(stock_irm_cninfo_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.16.2 互动易-回答
**接口名称**: `stock_irm_ans_cninfo`  
**目标地址**: 互动易-回答  
**描述**: 获取互动易回答数据  
**限量**: 单次返回指定股票的回答数据  

**输入参数**:
- symbol: 提问者编号，如"1495108801386602496"

**输出参数**:
- 返回互动易回答数据

**用法示例**:
```python
import akshare as ak

stock_irm_ans_cninfo_df = ak.stock_irm_ans_cninfo(symbol="1495108801386602496")
print(stock_irm_ans_cninfo_df)
```

**返回类型**: pandas.DataFrame

---

#### 9.16.3 上证e互动
**接口名称**: `stock_sns_sseinfo`  
**目标地址**: 上证e互动-提问与回答  
**描述**: 获取上证e互动提问与回答数据  
**限量**: 单次返回指定股票的提问与回答数据  

**输入参数**:
- symbol: 股票代码，如"603119"

**输出参数**:
- 返回上证e互动数据

**用法示例**:
```python
import akshare as ak

stock_sns_sseinfo_df = ak.stock_sns_sseinfo(symbol="603119")
print(stock_sns_sseinfo_df)
```

**返回类型**: pandas.DataFrame

---

### 9.17 赚钱效应分析接口

#### 9.17.1 赚钱效应分析
**接口名称**: `stock_market_activity_em`  
**目标地址**: 东方财富网-赚钱效应分析  
**描述**: 获取赚钱效应分析数据  
**限量**: 单次返回所有赚钱效应数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回赚钱效应分析数据

**用法示例**:
```python
import akshare as ak

stock_market_activity_em_df = ak.stock_market_activity_em()
print(stock_market_activity_em_df)
```

**返回类型**: pandas.DataFrame

---

## 10. 高级功能接口补充

### 10.1 主营介绍与构成接口

#### 10.1.1 主营介绍-同花顺
**接口名称**: `stock_zyjs_ths`  
**目标地址**: https://basic.10jqka.com.cn/new/000066/operate.html  
**描述**: 同花顺-主营介绍  
**限量**: 单次返回所有数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="000066"; 股票代码 |

**输出参数**:
- 返回主营介绍数据

**用法示例**:
```python
import akshare as ak

stock_zyjs_ths_df = ak.stock_zyjs_ths(symbol="000066")
print(stock_zyjs_ths_df)
```

**返回类型**: pandas.DataFrame

---

#### 10.1.2 主营构成-东方财富
**接口名称**: `stock_zygc_em`  
**目标地址**: https://emweb.securities.eastmoney.com/PC_HSF10/BusinessAnalysis/Index?type=web&code=SH688041#  
**描述**: 东方财富网-个股-主营构成  
**限量**: 单次返回所有历史数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="SH688041"; 股票代码 |

**输出参数**:
- 返回主营构成数据

**用法示例**:
```python
import akshare as ak

stock_zygc_em_df = ak.stock_zygc_em(symbol="SH688041")
print(stock_zygc_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.2 公司动态接口

#### 10.2.1 公司动态-东方财富
**接口名称**: `stock_gsrl_gsdt_em`  
**目标地址**: https://data.eastmoney.com/gsrl/gsdt.html  
**描述**: 东方财富网-数据中心-股市日历-公司动态  
**限量**: 单次返回指定交易日的数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | date="20230808"; 交易日期 |

**输出参数**:
- 返回公司动态数据

**用法示例**:
```python
import akshare as ak

stock_gsrl_gsdt_em_df = ak.stock_gsrl_gsdt_em(date="20230808")
print(stock_gsrl_gsdt_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.3 分红派息接口

#### 10.3.1 历史分红-巨潮资讯
**接口名称**: `stock_dividend_cninfo`  
**目标地址**: http://webapi.cninfo.com.cn/#/company?companyid=600009  
**描述**: 巨潮资讯-个股-历史分红  
**限量**: 单次获取指定股票的历史分红数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="600009"; 股票代码 |

**输出参数**:
- 返回历史分红数据

**用法示例**:
```python
import akshare as ak

stock_dividend_cninfo_df = ak.stock_dividend_cninfo(symbol="600009")
print(stock_dividend_cninfo_df)
```

**返回类型**: pandas.DataFrame

---

### 10.4 个股新闻与资讯接口

#### 10.4.1 个股新闻-东方财富
**接口名称**: `stock_news_em`  
**目标地址**: https://so.eastmoney.com/news/s?keyword=603777  
**描述**: 东方财富指定个股的新闻资讯数据  
**限量**: 指定 symbol 当日最近 100 条新闻资讯数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="603777"; 股票代码 |

**输出参数**:
- 返回个股新闻数据

**用法示例**:
```python
import akshare as ak

stock_news_em_df = ak.stock_news_em(symbol="603777")
print(stock_news_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 10.4.2 财经内容精选-财新网
**接口名称**: `stock_news_main_cx`  
**目标地址**: https://cxdata.caixin.com/pc/  
**描述**: 财新网-财新数据通-内容精选  
**限量**: 返回所有历史新闻数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回财经内容精选数据

**用法示例**:
```python
import akshare as ak

stock_news_main_cx_df = ak.stock_news_main_cx()
print(stock_news_main_cx_df)
```

**返回类型**: pandas.DataFrame

---

### 10.5 财报发行接口

#### 10.5.1 财务报表-新浪
**接口名称**: `stock_financial_report_sina`  
**目标地址**: https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600600/displaytype/4.phtml  
**描述**: 新浪财经-财务报表-三大报表  
**限量**: 单次获取指定报表的所有年份数据的历史数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| stock | str | stock="sh600600"; 股票代码 |
| indicator | str | indicator="现金流量表"; choice of {"利润表", "资产负债表", "现金流量表"} |

**输出参数**:
- 返回财务报表数据

**用法示例**:
```python
import akshare as ak

stock_financial_report_sina_df = ak.stock_financial_report_sina(stock="sh600600", indicator="现金流量表")
print(stock_financial_report_sina_df)
```

**返回类型**: pandas.DataFrame

---

### 10.6 业绩相关接口

#### 10.6.1 业绩报表-东方财富
**接口名称**: `stock_yjbb_em`  
**目标地址**: http://data.eastmoney.com/bbsj/202003/yjbb.html  
**描述**: 东方财富-数据中心-年报季报-业绩报表  
**限量**: 单次获取指定 date 的业绩报告数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | date="20220331"; 报告期 |

**输出参数**:
- 返回业绩报表数据

**用法示例**:
```python
import akshare as ak

stock_yjbb_em_df = ak.stock_yjbb_em(date="20220331")
print(stock_yjbb_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 10.6.2 业绩快报-东方财富
**接口名称**: `stock_yjkb_em`  
**目标地址**: https://data.eastmoney.com/bbsj/202003/yjkb.html  
**描述**: 东方财富-数据中心-年报季报-业绩快报  
**限量**: 单次获取指定 date 的业绩快报数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | date="20200331"; 报告期 |

**输出参数**:
- 返回业绩快报数据

**用法示例**:
```python
import akshare as ak

stock_yjkb_em_df = ak.stock_yjkb_em(date="20200331")
print(stock_yjkb_em_df)
```

**返回类型**: pandas.DataFrame

---

#### 10.6.3 业绩预告-东方财富
**接口名称**: `stock_yjyg_em`  
**目标地址**: https://data.eastmoney.com/bbsj/202003/yjyg.html  
**描述**: 东方财富-数据中心-年报季报-业绩预告  
**限量**: 单次获取指定 date 的业绩预告数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | date="20190331"; 报告期 |

**输出参数**:
- 返回业绩预告数据

**用法示例**:
```python
import akshare as ak

stock_yjyg_em_df = ak.stock_yjyg_em(date="20190331")
print(stock_yjyg_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.7 预约披露时间接口

#### 10.7.1 预约披露时间-东方财富
**接口名称**: `stock_yysj_em`  
**目标地址**: https://data.eastmoney.com/bbsj/202003/yysj.html  
**描述**: 东方财富-数据中心-年报季报-预约披露时间  
**限量**: 单次获取指定 symbol 和 date 的预约披露时间数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="沪深A股"; choice of {"沪深A股", "沪市A股", "深市A股", "创业板", "科创板"} |
| date | str | date="20220331"; 报告期 |

**输出参数**:
- 返回预约披露时间数据

**用法示例**:
```python
import akshare as ak

stock_yysj_em_df = ak.stock_yysj_em(symbol="沪深A股", date="20220331")
print(stock_yysj_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.8 概念板块成分股接口

#### 10.8.1 概念板块成分股-东方财富
**接口名称**: `stock_board_concept_cons_em`  
**目标地址**: http://quote.eastmoney.com/center/boardlist.html#boards-BK06551  
**描述**: 东方财富-沪深板块-概念板块-板块成份  
**限量**: 单次返回当前时刻所有成份股  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="融资融券"; 概念板块名称 |

**输出参数**:
- 返回概念板块成分股数据

**用法示例**:
```python
import akshare as ak

stock_board_concept_cons_em_df = ak.stock_board_concept_cons_em(symbol="融资融券")
print(stock_board_concept_cons_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.9 概念板块指数接口

#### 10.9.1 概念板块指数-东方财富
**接口名称**: `stock_board_concept_hist_em`  
**目标地址**: http://quote.eastmoney.com/bk/90.BK0715.html  
**描述**: 东方财富-沪深板块-概念板块-历史行情数据  
**限量**: 单次返回指定 symbol 和 adjust 的历史数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="绿色电力"; 概念板块名称 |
| period | str | period="daily"; choice of {"daily", "weekly", "monthly"} |
| start_date | str | start_date="20220101"; 开始日期 |
| end_date | str | end_date="20250227"; 结束日期 |
| adjust | str | adjust=""; choice of {"", "qfq", "hfq"} |

**输出参数**:
- 返回概念板块历史行情数据

**用法示例**:
```python
import akshare as ak

stock_board_concept_hist_em_df = ak.stock_board_concept_hist_em(
    symbol="绿色电力", 
    period="daily", 
    start_date="20220101", 
    end_date="20250227", 
    adjust=""
)
print(stock_board_concept_hist_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.10 行业板块成分股接口

#### 10.10.1 行业板块成分股-东方财富
**接口名称**: `stock_board_industry_cons_em`  
**目标地址**: https://data.eastmoney.com/bkzj/BK1027.html  
**描述**: 东方财富-沪深板块-行业板块-板块成份  
**限量**: 单次返回指定 symbol 的所有成份股  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="小金属"; 行业板块名称 |

**输出参数**:
- 返回行业板块成分股数据

**用法示例**:
```python
import akshare as ak

stock_board_industry_cons_em_df = ak.stock_board_industry_cons_em(symbol="小金属")
print(stock_board_industry_cons_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.11 行业板块指数接口

#### 10.11.1 行业板块指数-东方财富
**接口名称**: `stock_board_industry_hist_em`  
**目标地址**: https://quote.eastmoney.com/bk/90.BK1027.html  
**描述**: 东方财富-沪深板块-行业板块-历史行情数据  
**限量**: 单次返回指定 symbol 和 adjust 的所有历史数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="小金属"; 行业板块名称 |
| period | str | period="daily"; choice of {"daily", "weekly", "monthly"} |
| start_date | str | start_date="20220101"; 开始日期 |
| end_date | str | end_date="20250227"; 结束日期 |
| adjust | str | adjust=""; choice of {"", "qfq", "hfq"} |

**输出参数**:
- 返回行业板块历史行情数据

**用法示例**:
```python
import akshare as ak

stock_board_industry_hist_em_df = ak.stock_board_industry_hist_em(
    symbol="小金属", 
    period="daily", 
    start_date="20220101", 
    end_date="20250227", 
    adjust=""
)
print(stock_board_industry_hist_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.12 股票热度接口

#### 10.12.1 股票热度-雪球关注排行榜
**接口名称**: `stock_hot_follow_xq`  
**目标地址**: https://xueqiu.com/hq  
**描述**: 雪球-沪深股市-热度排行榜-关注排行榜  
**限量**: 单次返回指定 symbol 的排行数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="最热门"; choice of {"最热门", "沪深A股", "港股", "美股"} |

**输出参数**:
- 返回关注排行榜数据

**用法示例**:
```python
import akshare as ak

stock_hot_follow_xq_df = ak.stock_hot_follow_xq(symbol="最热门")
print(stock_hot_follow_xq_df)
```

**返回类型**: pandas.DataFrame

---

#### 10.12.2 股票热度-东方财富人气榜
**接口名称**: `stock_hot_rank_em`  
**目标地址**: http://guba.eastmoney.com/rank/  
**描述**: 东方财富网站-股票热度  
**限量**: 单次返回当前交易日前 100 个股票的人气排名数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回股票热度排行数据

**用法示例**:
```python
import akshare as ak

stock_hot_rank_em_df = ak.stock_hot_rank_em()
print(stock_hot_rank_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.13 历史趋势及粉丝特征接口

#### 10.13.1 历史趋势及粉丝特征-东方财富
**接口名称**: `stock_hot_rank_detail_em`  
**目标地址**: http://guba.eastmoney.com/rank/stock?code=000665  
**描述**: 东方财富网-股票热度-历史趋势及粉丝特征  
**限量**: 单次返回指定 symbol 的股票近期历史数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="000665"; 股票代码 |

**输出参数**:
- 返回历史趋势及粉丝特征数据

**用法示例**:
```python
import akshare as ak

stock_hot_rank_detail_em_df = ak.stock_hot_rank_detail_em(symbol="000665")
print(stock_hot_rank_detail_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.14 个股人气榜接口

#### 10.14.1 个股人气榜-实时变动
**接口名称**: `stock_hot_rank_detail_xq`  
**目标地址**: https://xueqiu.com/S/SH000001  
**描述**: 雪球-个股人气榜-实时变动  
**限量**: 单次返回指定 symbol 的实时人气数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="SH000001"; 股票代码 |

**输出参数**:
- 返回个股人气榜实时数据

**用法示例**:
```python
import akshare as ak

stock_hot_rank_detail_xq_df = ak.stock_hot_rank_detail_xq(symbol="SH000001")
print(stock_hot_rank_detail_xq_df)
```

**返回类型**: pandas.DataFrame

---

#### 10.14.2 个股人气榜-最新排名
**接口名称**: `stock_hot_rank_latest_em`  
**目标地址**: http://guba.eastmoney.com/rank/  
**描述**: 东方财富网-个股人气榜-最新排名  
**限量**: 单次返回最新的人气排名数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回最新人气排名数据

**用法示例**:
```python
import akshare as ak

stock_hot_rank_latest_em_df = ak.stock_hot_rank_latest_em()
print(stock_hot_rank_latest_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.15 热门关键词接口

#### 10.15.1 热门关键词-东方财富
**接口名称**: `stock_hot_keyword_em`  
**目标地址**: http://guba.eastmoney.com/rank/  
**描述**: 东方财富网-热门关键词  
**限量**: 单次返回热门关键词数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回热门关键词数据

**用法示例**:
```python
import akshare as ak

stock_hot_keyword_em_df = ak.stock_hot_keyword_em()
print(stock_hot_keyword_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.16 热搜股票接口

#### 10.16.1 热搜股票-东方财富
**接口名称**: `stock_hot_search_em`  
**目标地址**: http://guba.eastmoney.com/rank/  
**描述**: 东方财富网-热搜股票  
**限量**: 单次返回热搜股票数据  

**输入参数**:
- 无参数

**输出参数**:
- 返回热搜股票数据

**用法示例**:
```python
import akshare as ak

stock_hot_search_em_df = ak.stock_hot_search_em()
print(stock_hot_search_em_df)
```

**返回类型**: pandas.DataFrame

---

### 10.17 相关股票接口

#### 10.17.1 相关股票-东方财富
**接口名称**: `stock_hot_related_em`  
**目标地址**: http://guba.eastmoney.com/rank/  
**描述**: 东方财富网-相关股票  
**限量**: 单次返回相关股票数据  

**输入参数**:
| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | symbol="000001"; 股票代码 |

**输出参数**:
- 返回相关股票数据

**用法示例**:
```python
import akshare as ak

stock_hot_related_em_df = ak.stock_hot_related_em(symbol="000001")
print(stock_hot_related_em_df)
```

**返回类型**: pandas.DataFrame

---

## 11. 总结

AKShare提供了丰富的股票数据接口，涵盖了A股、B股、港股、美股等多个市场。主要特点包括：

1. **数据全面**: 覆盖实时行情、历史数据、分时数据、分笔数据等
2. **多数据源**: 支持东方财富、新浪财经、腾讯证券等多个数据源
3. **使用简单**: 提供简洁的Python API接口
4. **免费开源**: 完全免费，开源可定制
5. **持续更新**: 定期更新接口，保持数据新鲜度
6. **高级功能**: 提供基本面数据、资金流向、盈利预测、概念板块、行业板块、股票热度、盘后异动、板块异动详情、涨停板行情、赚钱效应分析、资讯数据等高级功能接口
7. **新增功能**: 主营介绍与构成、公司动态、分红派息、个股新闻、财经内容精选、财报发行、业绩快报、业绩预告、预约披露时间、概念板块成分股、概念板块指数、行业板块成分股、行业板块指数、股票热度、历史趋势及粉丝特征、个股人气榜、热门关键词、热搜股票、相关股票等

通过本文档，您可以快速了解和使用AKShare的各种股票数据接口，为您的投资分析和量化交易提供数据支持。

---

## 12. Python实现文件

### 12.1 akshare-api.py 文件说明

基于本文档的98个接口，已创建了完整的Python实现文件 `akshare-api.py`，该文件包含所有接口的调用方法。

#### 12.1.1 文件特点

- **完整性**: 包含文档中列出的所有98个接口
- **统一格式**: 所有接口都采用统一的调用格式
- **错误处理**: 每个接口都包含完整的异常处理机制
- **参数支持**: 支持所有接口的参数配置
- **返回格式**: 统一返回pandas.DataFrame格式

#### 12.1.2 接口分类统计

| 分类 | 接口数量 | 说明 |
|------|----------|------|
| A股数据接口 | 47个 | 包含市场总貌、个股信息、实时行情、历史数据、分时数据等 |
| B股数据接口 | 4个 | B股实时行情、历史数据、分时数据 |
| 港股数据接口 | 3个 | 港股实时行情、历史数据 |
| 美股数据接口 | 3个 | 美股实时行情、历史数据 |
| 其他功能接口 | 4个 | 股票比较分析相关接口 |
| 特殊功能接口 | 1个 | CDR历史数据 |
| 高级功能接口 | 36个 | 基本面数据、资金流向、概念板块、行业分析等 |

#### 12.1.3 使用示例

```python
# 导入文件
from akshare_api import *

# 获取A股实时行情
df = stock_zh_a_spot_em()
print(f"获取到 {len(df)} 条A股数据")

# 获取个股历史数据
df = stock_zh_a_hist(symbol="000001", start_date="20240101", end_date="20240131")
print(f"获取到 {len(df)} 条历史数据")

# 获取概念板块数据
df = stock_board_concept_name_em()
print(f"获取到 {len(df)} 个概念板块")
```

#### 12.1.4 接口调用格式

所有接口都采用统一的调用格式：

```python
def interface_name(param1="default1", param2="default2"):
    """
    接口描述
    
    输入参数:
    | 名称 | 类型 | 描述 |
    |------|------|------|
    | param1 | str | 参数1说明 |
    | param2 | str | 参数2说明 |
    
    输出参数:
    - 返回数据说明
    
    返回类型: pandas.DataFrame
    """
    url = "http://127.0.0.1:8080/api/public/interface_name"
    params = {
        "param1": param1,
        "param2": param2
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return pd.DataFrame()
```

### 12.2 文件验证结果

#### 12.2.1 验证统计

- **总函数定义数量**: 133个
- **实际唯一接口数量**: 98个
- **文件总行数**: 约1700行
- **重复函数数量**: 35个（需要清理）

#### 12.2.2 重复函数列表

以下函数存在重复定义，需要清理：

| 函数名 | 重复次数 | 说明 |
|--------|----------|------|
| stock_board_concept_hist_em | 3次 | 概念板块历史行情 |
| stock_market_activity_em | 3次 | 盘口异动数据 |
| stock_lhb_stock_statistic_em | 2次 | 个股上榜统计 |
| stock_institute_visit_detail_em | 2次 | 机构调研详细 |
| stock_institute_hold_detail | 2次 | 机构持股详情 |
| stock_institute_visit_em | 2次 | 机构调研统计 |
| stock_zt_pool_previous_em | 2次 | 昨日涨停股池 |
| stock_zt_pool_em | 2次 | 涨停股池 |
| stock_lhb_detail_em | 2次 | 龙虎榜详情 |
| stock_dt_pool_em | 2次 | 跌停股池 |
| stock_irm_cninfo | 2次 | 互动易-提问 |
| stock_info_global_sina | 2次 | 全球财经快讯-新浪 |
| stock_sns_sseinfo | 2次 | 上证e互动 |
| stock_irm_ans_cninfo | 2次 | 互动易-回答 |
| stock_info_global_em | 2次 | 全球财经快讯-东方财富 |
| stock_institute_recommend_detail | 2次 | 股票评级记录 |
| stock_institute_recommend | 2次 | 机构推荐池 |
| stock_info_cjzc_em | 2次 | 财经早餐 |
| stock_research_report_em | 2次 | 个股研报 |
| stock_board_change_em | 2次 | 板块异动详情 |
| stock_financial_analysis_indicator | 2次 | 财务指标数据 |
| stock_financial_abstract | 2次 | 财务报表数据 |
| stock_hsgt_fund_flow_summary_em | 2次 | 沪深港通资金流向 |
| stock_yjbb_em | 2次 | 业绩报表数据 |
| stock_zh_dupont_comparison_em | 2次 | 股票杜邦分析比较 |
| stock_zh_valuation_comparison_em | 2次 | 股票估值比较 |
| stock_zh_a_cdr_daily | 2次 | CDR历史数据 |
| stock_zh_scale_comparison_em | 2次 | 股票规模比较 |
| stock_individual_fund_flow_rank | 2次 | 个股资金流向 |
| stock_board_industry_name_em | 2次 | 东方财富行业板块 |
| stock_board_industry_name_ths | 2次 | 同花顺行业一览表 |
| stock_zh_growth_comparison_em | 2次 | 股票成长性比较 |
| stock_hot_rank_em | 2次 | 股票热度排行 |
| stock_profit_forecast_ths | 2次 | 同花顺盈利预测 |
| stock_profit_forecast_em | 2次 | 东方财富盈利预测 |
| stock_board_concept_name_em | 2次 | 东方财富概念板块 |
| stock_board_concept_cons_ths | 2次 | 同花顺概念板块指数 |

#### 12.2.3 完成状态

✅ **已完成**: 创建了包含所有98个接口的Python文件  
✅ **已完成**: 添加了B股、港股、美股和其他高级功能接口  
✅ **已完成**: 验证了所有98个接口都已包含  
🔄 **进行中**: 修复文件中的重复函数定义问题

### 12.3 使用建议

1. **清理重复**: 建议清理文件中的重复函数定义，确保每个接口只定义一次
2. **测试验证**: 建议对每个接口进行测试，确保API调用正常
3. **参数验证**: 建议添加参数验证逻辑，提高代码健壮性
4. **文档更新**: 建议根据实际使用情况更新接口文档

### 12.4 文件结构

```
akshare-api.py
├── 导入模块 (requests, pandas)
├── A股数据接口 (47个)
│   ├── 股票市场总貌 (5个)
│   ├── 个股信息查询 (2个)
│   ├── 行情报价 (1个)
│   ├── 实时行情数据 (10个)
│   ├── 历史行情数据 (3个)
│   ├── 分时数据 (5个)
│   ├── 历史分笔数据 (1个)
│   └── 其他A股相关接口 (20个)
├── B股数据接口 (4个)
├── 港股数据接口 (3个)
├── 美股数据接口 (3个)
├── 其他功能接口 (4个)
├── 特殊功能接口 (1个)
├── 高级功能接口 (36个)
└── 使用示例
```

通过本文档和Python实现文件，您可以快速了解和使用AKShare的各种股票数据接口，为您的投资分析和量化交易提供数据支持。
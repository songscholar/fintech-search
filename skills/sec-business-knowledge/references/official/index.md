# 官方文档来源

以下四个网站为证券业务官方权威来源，查询时优先访问。

## 一、上海证券交易所 (SSE)

**网址**: https://www.sse.com.cn/

### 常用栏目
- **业务规则**: https://www.sse.com.cn/lawandrules/
- **股票业务**: https://www.sse.com.cn/assortment/stock/
- **债券业务**: https://www.sse.com.cn/assortment/bonds/
- **ETF业务**: https://www.sse.com.cn/assortment/fund/etf/
- **科创板**: https://www.sse.com.cn/star/
- **港股通**: https://www.sse.com.cn/services/hkex/
- **大宗交易**: https://www.sse.com.cn/services/training/

### 搜索用法
```
web_fetch "https://www.sse.com.cn/lawandrules/"
web_search "site:sse.com.cn ETF 申购赎回"
```

---

## 二、深圳证券交易所 (SZSE)

**网址**: https://www.szse.cn/

### 常用栏目
- **业务规则**: https://www.szse.cn/lawrules/index.html
- **股票业务**: https://www.szse.cn/market/
- **债券业务**: https://www.szse.cn/market/bond/
- **基金业务**: https://www.szse.cn/market/fund/
- **创业板**: https://www.szse.cn/market/gem/
- **港股通**: https://www.szse.cn/services/hkex/

### 搜索用法
```
web_fetch "https://www.szse.cn/lawrules/index.html"
web_search "site:szse.cn 创业板 交易规则"
```

---

## 三、北京证券交易所 (BSE)

**网址**: https://www.bse.cn/

### 常用栏目
- **业务规则**: https://www.bse.cn/nq/business_rules.html
- **上市公司**: https://www.bse.cn/nq/listed.html
- **市场数据**: https://www.bse.cn/market/

### 搜索用法
```
web_fetch "https://www.bse.cn/nq/business_rules.html"
web_search "site:bse.cn 交易规则"
```

---

## 四、中国证券登记结算有限公司 (CSDC/中国结算)

**网址**: http://www.chinaclear.cn/

### 常用栏目
- **业务规则**: http://www.chinaclear.cn/zdjs/ggfzyw/home.shtml
- **证券账户**: http://www.chinaclear.cn/zdjs/account_index.shtml
- **结算业务**: http://www.chinaclear.cn/zdjs/jiesuan/
- **登记业务**: http://www.chinaclear.cn/zdjs/dengji/

### 搜索用法
```
web_fetch "http://www.chinaclear.cn/zdjs/ggfzyw/home.shtml"
web_search "site:chinaclear.cn 结算规则"
```

---

## 查询优先级

1. 先根据业务类型确定交易所（沪/深/北）
2. 搜索对应交易所官网
3. 中国结算用于查询登记结算规则
4. 涉及跨市场业务时，需查阅多方规则

## 注意事项

- 官方文档更新后旧版本可能失效
- 搜索时注意发布日期，优先使用最新版本
- 规则冲突时以官网最新公告为准
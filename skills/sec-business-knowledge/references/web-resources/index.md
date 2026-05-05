# 权威网络资源

以下为证券行业权威网站，在本地知识库和官方文档都未找到时，优先访问这些网站。

## 一、监管机构

### 中国证监会 (CSRC)
**网址**: http://www.csrc.gov.cn/

- 监管政策、法规公告
- 证券期货监管规则
- 投资者保护

```
web_search "site:csrc.gov.cn 证券期货监管"
```

---

## 二、行业自律组织

### 中国证券业协会 (SAC)
**网址**: https://www.sac.net.cn/

- 行业自律规则
- 从业人员管理
- 业务指引

```
web_search "site:sac.net.cn 自律规则"
```

### 中国期货业协会 (CFA)
**网址**: http://www.cfachina.org/

- 期货行业规则
- 从业资格管理

```
web_search "site:cfachina.org 期货规则"
```

### 中国证券投资基金业协会 (AMAC)
**网址**: https://www.amac.org.cn/

- 基金行业规则
- 私募基金管理

```
web_search "site:amac.org.cn 私募基金"
```

---

## 三、期货交易所

### 上海期货交易所 (SHFE)
**网址**: https://www.shfe.com.cn/

- 金属、能源期货
- 交易规则、交割规则

```
web_search "site:shfe.com.cn 交割规则"
```

### 大连商品交易所 (DCE)
**网址**: http://www.dce.com.cn/

- 农产品、化工期货
- 交易规则

```
web_search "site:dce.com.cn 交易规则"
```

### 郑州商品交易所 (CZCE)
**网址**: http://www.czce.com.cn/

- 农产品期货
- 期权交易

```
web_search "site:czce.com.cn 期权规则"
```

### 中国金融期货交易所 (CFFEX)
**网址**: http://www.cffex.com.cn/

- 股指期货、国债期货
- 金融衍生品

```
web_search "site:cffex.com.cn 股指期货"
```

### 广州期货交易所 (GFEX)
**网址**: http://www.gfex.com.cn/

- 碳排放权、商品指数

```
web_search "site:gfex.com.cn 交易规则"
```

---

## 四、其他重要机构

### 全国中小企业股份转让系统 (NEEQ/新三板)
**网址**: https://www.neeq.com.cn/

- 挂牌公司管理
- 交易规则

```
web_search "site:neeq.com.cn 挂牌规则"
```

### 中证指数有限公司
**网址**: https://www.csindex.com.cn/

- 指数编制规则
- 指数成分股

```
web_search "site:csindex.com.cn 指数编制"
```

### 中国证券投资者保护基金
**网址**: http://www.sipf.com.cn/

- 投资者保护
- 风险处置

---

## 搜索优先级

在 `references/web-resources/` 层级：

1. **监管机构**: csrc.gov.cn（证监会）
2. **交易所**: sse/szse/bse/shfe/dce/czce/cffex/gfex
3. **自律组织**: sac/cfachina/amac
4. **其他机构**: neeq/csindex/sipf

---

## 使用建议

```bash
# 按优先级搜索
web_search "site:csrc.gov.cn 关键词"          # 优先监管机构
web_search "site:sse.com.cn OR site:szse.cn 关键词"  # 交易所
web_search "site:sac.net.cn 关键词"           # 行业协会
web_search "关键词 证券"                      # 全网搜索
```
# Worklog

## 2026-04-09

### 阶段 1：项目初始化

- 创建项目目录结构
- 明确项目目标：先做 DSL 解析层，再做索引层
- 结合完整代码目录 `uses_codes` 的真实结构确认了第一版范围

### 阶段 2：当前优先级

- 优先实现 XML + CDATA DSL 解析器
- 优先沉淀文档，而不是最后再补说明
- 优先支持最核心的结构：
  - 文件元数据
  - 参数
  - 历史记录
  - DSL 动作
  - 过程调用
  - 基础控制流

### 阶段 3：第一版解析器完成并验证

- 增加 CLI：
  - `parse-file`
  - `scan-dir`
- 增加单元测试，当前已通过
- 对完整目录 `/Users/songzuoqiang/Documents/agent/code/uses_codes` 做全量扫描
- 当前扫描结果：
  - 文件数 `2564`
  - `Function` `1858`
  - `Service` `703`
  - `FactorService` `3`
- 当前语句抽取结果：
  - `action` `18140`
  - `call` `8085`
  - `control` `21326`
  - `assignment` `16406`
  - `comment` `33196`

### 阶段 4：本轮补强

- 增加对 `break / continue` 的控制流识别
- 增加对 `++@var / --@var` 的写入识别
- 增加对 `hs_strcpy / sprintf / hs_snprintf / substr` 等常见输出参数写入识别

### 后续计划

- 用真实仓库跑第一版解析
- 校验输出质量
- 再把结果接到 SQLite 索引层

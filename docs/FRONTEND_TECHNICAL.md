# Frontend Technical Notes

## 目标

在不引入额外前端框架和构建链的前提下，为 `uses-indexer` 提供第一版内置 Web UI。

## 选型结论

本版采用：

- 原生 `HTML + CSS + JavaScript`
- 由现有 `ThreadingHTTPServer` 直接托管
- 继续复用现有 JSON API

不采用：

- React / Vue / Next / Vite
- 额外 Node 构建流程
- 独立前端部署链路

## 为什么这样选

### 1. 仓库当前没有前端栈

项目现在是一个 Python 工具项目，不是 Web App 项目。  
如果直接引入前端框架，会同时带来：

- 新依赖管理
- 新构建流程
- 新产物目录
- 新运行方式

这对第一版前端并不划算。

### 2. 当前最需要的是“先有一个真入口”

项目已经有：

- `GET /health`
- `GET /db-summary`
- `POST /query`
- `POST /evidence`
- `POST /ask`
- `POST /answer`
- `POST /debug-bundle`

所以最自然的做法，是先做一个能直连这些接口的控制台。

### 3. 零依赖静态 UI 最利于快速验证

这版前端的主要价值是：

- 验证页面结构是否顺手
- 验证数据展示是否清楚
- 验证结果面板的布局和交互是否合理

而不是一开始就建立完整 SPA 工程体系。

## 实现位置

### 静态资源

位于：

- [index.html](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/web/index.html)
- [styles.css](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/web/styles.css)
- [app.js](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/web/app.js)

### API 入口

由 [api.py](/Users/songzuoqiang/Documents/agent/condex/codes/src/uses_indexer/api.py) 负责：

- `GET /`
- `GET /ui`
- `GET /assets/styles.css`
- `GET /assets/app.js`

JSON API 保持不变。

## 路由策略

### 页面路由

- `/`
- `/ui`

都返回同一个控制台页面。

### 静态资源路由

- `/assets/styles.css`
- `/assets/app.js`

### 数据路由

继续复用现有接口，不另外引入 UI 专用 API。

## 页面模块

### 1. Hero

数据来源：

- `/health`
- `/db-summary`

用途：

- 显示默认数据库
- 显示文件数、语义块数、调用关系数

### 2. Summary Panel

数据来源：

- `/db-summary`

用途：

- 显示 `procedures / statements / chunks / blocks / calls_procedure / publishes_mc_topic`

### 3. Query / Evidence / Answer

数据来源：

- `/query`
- `/evidence`
- `/answer`

说明：

- `query` 默认开启 `debug=true`
- `evidence` 默认开启 `debug=true`
- `answer` 使用 `allow_draft_fallback=true`

### 4. Trace

数据来源：

- `query.debug`
- `evidence.debug`
- `answer.final_answer`
- `debug-bundle`

用途：

- 以轻量卡片方式显示 query type、candidate count、evidence count、pruned blocks、answer source 等摘要

## 交互说明

### 支持的主动作

- 运行整套分析
- 仅看检索
- 仅看证据
- 仅看回答
- 生成 bundle
- 刷新数据库概览

### 辅助交互

- Prompt chips 快速填充问题
- `Cmd/Ctrl + Enter` 直接运行整套分析
- 状态条显示当前动作和错误信息

## 动画策略

为了保持柔和风格，本版动效约束如下：

- 大面积背景只做慢速漂浮
- 卡片 hover 只轻微上抬
- 数字动画使用短时长缓动
- 加载效果只在面板层出现，不覆盖全屏

## 打包说明

为了确保安装后静态资源可用，在 [pyproject.toml](/Users/songzuoqiang/Documents/agent/condex/codes/pyproject.toml) 中补充了：

- `tool.setuptools.package-data`

用于把 `src/uses_indexer/web/*` 一起打包进发行物。

## 测试覆盖

本轮新增 API 层回归，覆盖：

- `GET /` 返回 HTML
- `GET /assets/styles.css` 返回 CSS
- `GET /assets/app.js` 返回 JS

这样至少可以保证：

- 前端入口可访问
- 静态资源能被服务
- 不会因为后续 API 改动把页面入口悄悄弄坏

## 后续技术演进建议

如果后面页面继续扩展到多视图、多状态和更复杂的交互，建议升级为：

- 保留当前 API
- 单独引入轻量前端工程
- 保留 `/ui` 作为最终打包产物入口

这样可以保持：

- 本地使用路径不变
- 文档路径不变
- 现有 CLI/API 用户不受影响

## 2026-04-22 单屏技术调整

这次前端没有改 API 结构，但对页面组织方式做了明显调整。

### 布局层变化

从：

- 多 section 纵向堆叠

调整为：

- 固定高度 `app-shell`
- 顶部控制条
- 上方 Hero + Command
- 下方单个 `workspace-panel`

### 视图切换机制

新增两层前端切换：

1. 一级视图切换
   - `results-view`
   - `system-view`
   - `insights-view`

2. 二级结果切换
   - 左侧：
     - `query-panel`
     - `evidence-panel`
   - 右侧：
     - `answer-panel`
     - `trace-panel`

这两层都只在前端完成，不需要额外后端接口。

### 交互层变化

新增：

- `setView(viewId)`
- `setSubpanel(button)`
- `activatePanelById(panelId)`
- `activateDefaultPanels()`

这样：

- 点击顶部按钮会切主视图
- 点击结果区页签会切子面板
- 运行不同动作时可以自动把用户带到最合理的结果页签

### 2026-04-22 交互修复补充

在单屏重构后，又补了一轮切换稳定性修复：

- 主视图切换不再只靠 class，而是同时显式控制 `hidden`
- 子面板切换同样显式控制 `hidden`
- 顶部视图按钮同步更新 `aria-selected`
- 静态资源响应增加 `Cache-Control: no-store`

这样可以避免两类问题：

- 点按钮后内容区看起来没有切换
- 浏览器继续使用旧版 JS/CSS，导致“已经改了但页面没变”

### 2026-04-22 横屏导航模式调整

根据横屏网页模式下的使用反馈，又做了一次导航结构调整：

- 顶部改成四个页面按钮：
  - `主页`
  - `结果视图`
  - `系统视图`
  - `设计说明`
- `主页` 保留当前首屏结构：
  - Hero
  - 主操作区
  - 概览型主页内容
- 其余三个页面变成独立详情页面
- 外层框架继续固定
- 每个详情页面内部单独 `overflow: auto`

这样就能同时满足：

- 首页结构稳定
- 横屏下不依赖整页纵向滚动
- 结果、系统、设计三个页面都能各自滚动查看更多内容

### 样式层变化

新版本样式从“长页面展示风”转成“控制台风”，核心变化包括：

- `body` 默认 `overflow: hidden`
- `console-grid` 使用固定工作区
- `workspace-view` / `subpanel` 使用绝对定位和过渡切换
- 新增 mesh / halo / pulse grid 背景动画
- 新增按钮组状态同步样式

### 响应式策略

桌面端：

- 优先保证单屏完整体验

窄屏：

- 自动退回可滚动布局
- 通过媒体查询取消绝对定位切换
- 保持功能完整，而不是强行维持单屏

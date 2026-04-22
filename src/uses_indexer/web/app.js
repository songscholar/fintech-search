const state = {
  health: null,
  summary: null,
  query: null,
  evidence: null,
  answer: null,
  bundle: null,
  agentProviders: [],
  agentConversation: [],
  agentLastResponse: null,
  currentView: "home",
};

const nodes = {};

document.addEventListener("DOMContentLoaded", () => {
  bindNodes();
  bindEvents();
  renderEmptyStates();
  setPage("home");
  activateDefaultPanels();
  initializeConsole();
});

function bindNodes() {
  [
    "server-pill",
    "server-status-text",
    "metric-db-path",
    "metric-files",
    "metric-chunks",
    "metric-calls",
    "db-path",
    "question-input",
    "limit-input",
    "context-window-input",
    "related-limit-input",
    "status-strip",
    "status-text",
    "summary-procedures",
    "summary-statements",
    "summary-chunks",
    "summary-blocks",
    "summary-calls",
    "summary-topics",
    "query-results",
    "evidence-results",
    "answer-results",
    "trace-results",
    "query-meta",
    "evidence-meta",
    "answer-meta",
    "route-cloud",
    "agent-meta",
    "agent-transcript",
    "agent-input",
    "agent-send",
    "agent-clear",
    "agent-provider-select",
    "agent-include-retrieval",
    "agent-include-evidence",
    "agent-include-answer-draft",
    "agent-limit-input",
    "agent-context-window-input",
    "agent-related-limit-input",
    "agent-context-preview",
  ].forEach((id) => {
    nodes[id] = document.getElementById(id);
  });
}

function bindEvents() {
  document.querySelectorAll(".prompt-chip").forEach((chip) => {
    chip.addEventListener("click", () => {
      nodes["question-input"].value = chip.dataset.prompt || "";
      nodes["question-input"].focus();
      nodes["question-input"].animate(
        [
          { transform: "scale(1)" },
          { transform: "scale(1.03)" },
          { transform: "scale(1)" },
        ],
        { duration: 400, easing: "cubic-bezier(.175, .885, .32, 1.275)" },
      );
      // 添加点击反馈动画
      chip.animate(
        [
          { transform: "scale(1)" },
          { transform: "scale(0.95)" },
          { transform: "scale(1)" },
        ],
        { duration: 300, easing: "cubic-bezier(.22,1,.36,1)" },
      );
    });
  });

  document.querySelectorAll(".run-button").forEach((button) => {
    button.addEventListener("click", () => {
      // 添加点击反馈动画
      button.animate(
        [
          { transform: "scale(1)" },
          { transform: "scale(0.95)" },
          { transform: "scale(1)" },
        ],
        { duration: 300, easing: "cubic-bezier(.22,1,.36,1)" },
      );
      runAction(button.dataset.action);
    });
  });

  document.querySelectorAll("[data-page-target]").forEach((button) => {
    button.addEventListener("click", () => {
      // 添加点击反馈动画
      button.animate(
        [
          { transform: "scale(1)" },
          { transform: "scale(0.95)" },
          { transform: "scale(1)" },
        ],
        { duration: 300, easing: "cubic-bezier(.22,1,.36,1)" },
      );
      setPage(button.dataset.pageTarget);
    });
  });

  document.querySelectorAll(".subtab").forEach((button) => {
    button.addEventListener("click", () => {
      // 添加点击反馈动画
      button.animate(
        [
          { transform: "scale(1)" },
          { transform: "scale(0.95)" },
          { transform: "scale(1)" },
        ],
        { duration: 300, easing: "cubic-bezier(.22,1,.36,1)" },
      );
      setSubpanel(button);
    });
  });

  document.getElementById("refresh-summary").addEventListener("click", () => {
    // 添加点击反馈动画
    document.getElementById("refresh-summary").animate(
      [
        { transform: "scale(1)" },
        { transform: "scale(0.95)" },
        { transform: "scale(1)" },
      ],
      { duration: 300, easing: "cubic-bezier(.22,1,.36,1)" },
    );
    refreshSummary();
  });

  document.getElementById("hero-refresh").addEventListener("click", () => {
    // 添加点击反馈动画
    document.getElementById("hero-refresh").animate(
      [
        { transform: "scale(1)" },
        { transform: "scale(0.95)" },
        { transform: "scale(1)" },
      ],
      { duration: 300, easing: "cubic-bezier(.22,1,.36,1)" },
    );
    refreshSummary();
  });

  nodes["agent-send"].addEventListener("click", () => {
    runAgentChat();
  });

  nodes["agent-clear"].addEventListener("click", () => {
    state.agentConversation = [];
    state.agentLastResponse = null;
    nodes["agent-input"].value = "";
    renderAgentConversation();
    renderAgentContextPreview();
    nodes["agent-meta"].textContent = "会话已清空";
  });

  nodes["agent-provider-select"].addEventListener("change", () => {
    renderAgentContextPreview();
    renderAgentMeta();
  });

  [
    "agent-include-retrieval",
    "agent-include-evidence",
    "agent-include-answer-draft",
    "agent-limit-input",
    "agent-context-window-input",
    "agent-related-limit-input",
  ].forEach((id) => {
    nodes[id].addEventListener("change", () => {
      renderAgentContextPreview();
    });
  });

  document.addEventListener("keydown", (event) => {
    const modifier = event.metaKey || event.ctrlKey;
    if (modifier && event.key === "Enter") {
      event.preventDefault();
      if (state.currentView === "agent-view") {
        runAgentChat();
        return;
      }
      runAction("all");
    }
  });

  // 添加滚动动画效果
  window.addEventListener("scroll", () => {
    const scrolled = window.pageYOffset;
    const rate = scrolled * -0.5;
    document.querySelectorAll(".mesh").forEach((mesh) => {
      mesh.style.transform = `translateY(${rate}px)`;
    });
  });
}

async function initializeConsole() {
  setStatus("连接服务中，正在读取健康状态和数据库摘要…", "loading");
  try {
    await loadHealth();
    await refreshSummary();
    await loadAgentProviders();
    renderAgentConversation();
    renderAgentContextPreview();
    setStatus("控制台已就绪，可以直接开始检索。", "ready");
  } catch (error) {
    setStatus(error.message, "error");
  }
}

async function loadHealth() {
  const health = await fetchJson("/health", { method: "GET" });
  state.health = health;
  nodes["server-pill"].classList.remove("is-error");
  nodes["server-pill"].classList.add("is-ready");
  nodes["server-status-text"].textContent = "服务在线";
  nodes["metric-db-path"].textContent = health.default_db_path || "未设置默认数据库";
  renderCounter(nodes["metric-files"], 0);
  renderCounter(nodes["metric-chunks"], 0);
  renderCounter(nodes["metric-calls"], 0);
  renderRoutes(health.routes || []);
}

async function refreshSummary() {
  const dbPath = currentDbPath();
  const query = dbPath ? `?db_path=${encodeURIComponent(dbPath)}` : "";
  document.querySelectorAll(".summary-panel").forEach((panel) => panel.classList.add("is-loading"));
  try {
    const summary = await fetchJson(`/db-summary${query}`, { method: "GET" });
    state.summary = summary;
    renderSummary(summary);
    renderMetricSnapshot(summary);
  } finally {
    document.querySelectorAll(".summary-panel").forEach((panel) => panel.classList.remove("is-loading"));
  }
}

async function loadAgentProviders() {
  const payload = await fetchJson("/agent/providers", { method: "GET" });
  state.agentProviders = payload.items || [];
  renderAgentProviders(payload);
}

async function runAction(action) {
  const question = nodes["question-input"].value.trim();
  if (!question) {
    setStatus("先输入一个问题，再运行检索或回答。", "error");
    nodes["question-input"].focus();
    return;
  }

  setPage("results-view");
  setStatus(`正在执行 ${labelForAction(action)}…`, "loading");
  toggleResultLoading(true);

  try {
    if (action === "all") {
      const [query, evidence, answer] = await Promise.all([
        fetchQuery(question),
        fetchEvidence(question),
        fetchAnswer(question),
      ]);
      state.query = query;
      state.evidence = evidence;
      state.answer = answer;
      renderQuery(query);
      renderEvidence(evidence);
      renderAnswer(answer);
      renderTrace(query, evidence, answer, null);
      activateDefaultPanels();
    } else if (action === "query") {
      state.query = await fetchQuery(question);
      renderQuery(state.query);
      renderTrace(state.query, state.evidence, state.answer, state.bundle);
      activatePanelById("query-panel");
    } else if (action === "evidence") {
      state.evidence = await fetchEvidence(question);
      renderEvidence(state.evidence);
      renderTrace(state.query, state.evidence, state.answer, state.bundle);
      activatePanelById("evidence-panel");
    } else if (action === "answer") {
      state.answer = await fetchAnswer(question);
      renderAnswer(state.answer);
      renderTrace(state.query, state.evidence, state.answer, state.bundle);
      activatePanelById("answer-panel");
    } else if (action === "bundle") {
      state.bundle = await fetchBundle(question);
      renderTrace(state.query, state.evidence, state.answer, state.bundle);
      activatePanelById("trace-panel");
    }
    setStatus(`${labelForAction(action)}已完成。`, "ready");
  } catch (error) {
    setStatus(error.message, "error");
  } finally {
    toggleResultLoading(false);
  }
}

async function fetchQuery(question) {
  return fetchJson("/query", {
    method: "POST",
    body: JSON.stringify({
      query: question,
      limit: numberValue(nodes["limit-input"], 6),
      db_path: currentDbPathOrUndefined(),
      debug: true,
    }),
  });
}

async function fetchEvidence(question) {
  return fetchJson("/evidence", {
    method: "POST",
    body: JSON.stringify({
      query: question,
      limit: numberValue(nodes["limit-input"], 6),
      context_window: numberValue(nodes["context-window-input"], 2),
      related_limit: numberValue(nodes["related-limit-input"], 3),
      db_path: currentDbPathOrUndefined(),
      debug: true,
    }),
  });
}

async function fetchAnswer(question) {
  return fetchJson("/answer", {
    method: "POST",
    body: JSON.stringify({
      question,
      evidence_limit: numberValue(nodes["limit-input"], 6),
      context_window: numberValue(nodes["context-window-input"], 2),
      related_limit: numberValue(nodes["related-limit-input"], 3),
      db_path: currentDbPathOrUndefined(),
      allow_draft_fallback: true,
    }),
  });
}

async function fetchBundle(question) {
  return fetchJson("/debug-bundle", {
    method: "POST",
    body: JSON.stringify({
      question,
      limit: numberValue(nodes["limit-input"], 6),
      context_window: numberValue(nodes["context-window-input"], 2),
      related_limit: numberValue(nodes["related-limit-input"], 3),
      db_path: currentDbPathOrUndefined(),
    }),
  });
}

async function fetchAgentChat(message) {
  return fetchJson("/agent/chat", {
    method: "POST",
    body: JSON.stringify({
      provider: nodes["agent-provider-select"].value || undefined,
      message,
      history: state.agentConversation.slice(-6),
      db_path: currentDbPathOrUndefined(),
      include_retrieval: nodes["agent-include-retrieval"].checked,
      include_evidence: nodes["agent-include-evidence"].checked,
      include_answer_draft: nodes["agent-include-answer-draft"].checked,
      limit: numberValue(nodes["agent-limit-input"], 6),
      context_window: numberValue(nodes["agent-context-window-input"], 2),
      related_limit: numberValue(nodes["agent-related-limit-input"], 3),
    }),
  });
}

async function fetchJson(url, options) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  const text = await response.text();
  let data = {};
  if (text) {
    data = JSON.parse(text);
  }
  if (!response.ok) {
    throw new Error(data.error || `请求失败：${response.status}`);
  }
  return data;
}

function setPage(pageId) {
  const isHome = pageId === "home";
  state.currentView = pageId;
  document.querySelector(".app-shell")?.classList.toggle("page-home", isHome);
  document.querySelector(".app-shell")?.classList.toggle("page-detail", !isHome);
  document.querySelectorAll(".workspace-view").forEach((view) => {
    const isActive = !isHome && view.id === pageId;
    view.hidden = !isActive;
    view.classList.toggle("workspace-view-active", isActive);
    if (!isActive) {
      view.classList.remove("workspace-view-active");
    }
  });
  document.querySelectorAll("[data-page-target]").forEach((button) => {
    const target = button.dataset.pageTarget;
    const isActive = target === pageId;
    button.classList.toggle("nav-pill-active", isActive);
    button.setAttribute("aria-selected", isActive ? "true" : "false");
  });
}

function setSubpanel(button) {
  activatePanelById(button.dataset.panelTarget);
}

function activatePanelById(panelId) {
  const panel = document.getElementById(panelId);
  if (!panel) return;

  const container = panel.closest(".subpanel-wrap");
  container.querySelectorAll(".subpanel").forEach((item) => {
    const isActive = item.id === panelId;
    item.hidden = !isActive;
    item.classList.toggle("subpanel-active", isActive);
    if (!isActive) {
      item.classList.remove("subpanel-active");
    }
  });

  const tabs = panel.closest(".results-main, .results-side").querySelectorAll(".subtab");
  tabs.forEach((tab) => {
    tab.classList.toggle("subtab-active", tab.dataset.panelTarget === panelId);
  });
}

function activateDefaultPanels() {
  activatePanelById("query-panel");
  activatePanelById("answer-panel");
}

function renderSummary(summary) {
  renderCounter(nodes["summary-procedures"], summary.procedures || 0);
  renderCounter(nodes["summary-statements"], summary.statements || 0);
  renderCounter(nodes["summary-chunks"], summary.chunks || 0);
  renderCounter(nodes["summary-blocks"], summary.blocks || 0);
  renderCounter(nodes["summary-calls"], summary.calls_procedure || 0);
  renderCounter(nodes["summary-topics"], summary.publishes_mc_topic || 0);
}

function renderMetricSnapshot(summary) {
  renderCounter(nodes["metric-files"], summary.files || 0);
  renderCounter(nodes["metric-chunks"], summary.chunks || 0);
  renderCounter(nodes["metric-calls"], summary.calls_procedure || 0);
}

function renderQuery(query) {
  nodes["query-meta"].textContent = `${query.hit_count || 0} 个命中 · ${query.candidate_count || 0} 个候选`;
  const hits = query.hits || [];
  if (!hits.length) {
    renderEmpty(nodes["query-results"], "还没有命中结果。");
    return;
  }
  nodes["query-results"].innerHTML = hits
    .slice(0, 8)
    .map(
      (hit, index) => `
        <article class="result-item">
          <h4>${index + 1}. ${escapeHtml(hit.procedure_name || hit.title || "未命名过程")}</h4>
          <p class="result-meta">${escapeHtml(hit.file_path || "未知文件")} · ${escapeHtml(hit.retrieval_source || hit.match_source || "unknown")}</p>
          <div class="result-code">${escapeHtml(hit.matched_text || hit.excerpt || "没有摘要文本")}</div>
        </article>
      `,
    )
    .join("");
}

function renderEvidence(evidence) {
  nodes["evidence-meta"].textContent = `${evidence.evidence_count || 0} 个证据块`;
  const items = evidence.evidence || [];
  if (!items.length) {
    renderEmpty(nodes["evidence-results"], "还没有证据块。");
    return;
  }
  nodes["evidence-results"].innerHTML = items
    .slice(0, 6)
    .map((item, index) => {
      const relatedTables = (item.related_tables || []).slice(0, 4).join(" / ");
      const relatedCalls = (item.related_calls || []).slice(0, 4).join(" / ");
      return `
        <article class="result-item">
          <h4>${index + 1}. ${escapeHtml(item.procedure_name || "未命名过程")}</h4>
          <p class="result-meta">${escapeHtml(item.file_path || "未知文件")} · 行 ${escapeHtml(String(item.line_start || "?"))}</p>
          <div class="result-code">${escapeHtml(item.matched_text || item.excerpt || "没有证据摘要")}</div>
          ${relatedTables ? `<p class="result-meta">相关表：${escapeHtml(relatedTables)}</p>` : ""}
          ${relatedCalls ? `<p class="result-meta">相关调用：${escapeHtml(relatedCalls)}</p>` : ""}
        </article>
      `;
    })
    .join("");
}

function renderAnswer(answer) {
  const finalAnswer = answer.final_answer || {};
  const text = finalAnswer.text || answer.draft_answer?.text || "还没有回答内容。";
  nodes["answer-meta"].textContent = `${answer.answer_source || finalAnswer.source || "draft"} · ${answer.response_kind || "answer"}`;
  const locations = finalAnswer.supporting_locations || answer.supporting_locations || [];
  const uncertainties = finalAnswer.uncertainties || [];
  nodes["answer-results"].innerHTML = `
    <article class="answer-card">
      <h4>回答内容</h4>
      <p class="answer-text">${escapeHtml(text)}</p>
      ${
        locations.length
          ? `<div class="citation-list">${locations
              .slice(0, 6)
              .map((item) => `<span class="citation-pill">${escapeHtml(item.procedure_name || item.file_path || "support")}</span>`)
              .join("")}</div>`
          : ""
      }
      ${
        uncertainties.length
          ? `<div class="result-code">${escapeHtml(uncertainties.join("\n"))}</div>`
          : ""
      }
    </article>
  `;
}

function renderTrace(query, evidence, answer, bundle) {
  const cards = [];
  if (query) {
    const analysis = query.debug?.query_analysis || {};
    cards.push(traceCard("Query Type", analysis.query_type || "unknown", `${query.hit_count || 0} 个命中`));
    cards.push(traceCard("Candidate Count", String(query.candidate_count || 0), "观察粗召回规模"));
  }
  if (evidence) {
    cards.push(traceCard("Evidence Blocks", String(evidence.evidence_count || 0), "观察证据筛选后的保留量"));
    const pruned = evidence.debug?.pruning?.dropped_count;
    if (pruned !== undefined) {
      cards.push(traceCard("Pruned Blocks", String(pruned), "判断裁剪是否过于激进"));
    }
  }
  if (answer) {
    cards.push(traceCard("Answer Source", answer.answer_source || "draft", answer.final_answer?.tier || "grounded summary"));
  }
  if (bundle) {
    cards.push(traceCard("Bundle Kind", bundle.bundle_kind || "debug_bundle", "适合导出和后续复盘"));
  }
  if (!cards.length) {
    renderEmpty(nodes["trace-results"], "运行一次查询后，这里会出现 query type、命中量、evidence pruning 等调试摘要。");
    return;
  }
  nodes["trace-results"].innerHTML = cards.join("");
}

function renderAgentProviders(payload) {
  const providers = payload.items || [];
  const select = nodes["agent-provider-select"];
  if (!providers.length) {
    select.innerHTML = `<option value="">未配置可用智能体</option>`;
    select.disabled = true;
    nodes["agent-send"].disabled = true;
    nodes["agent-meta"].textContent = "当前还没有配置智能体服务";
    return;
  }

  const defaultProvider = payload.default_provider || providers[0].name;
  select.innerHTML = providers
    .map((provider) => {
      const selected = provider.name === defaultProvider ? " selected" : "";
      return `<option value="${escapeHtml(provider.name)}"${selected}>${escapeHtml(provider.label)} · ${escapeHtml(provider.model)}</option>`;
    })
    .join("");
  select.disabled = false;
  nodes["agent-send"].disabled = false;
  renderAgentMeta();
}

function renderAgentConversation() {
  const transcript = nodes["agent-transcript"];
  if (!state.agentConversation.length) {
    renderEmpty(transcript, "这里会显示你和外部智能体的往返消息，以及它实际拿到的本地代码证据摘要。");
    return;
  }
  transcript.innerHTML = state.agentConversation
    .map((item, index) => {
      const roleLabel = item.role === "assistant" ? "智能体" : "你";
      const extra = item.meta ? escapeHtml(item.meta) : `第 ${index + 1} 条消息`;
      return `
        <article class="agent-message ${escapeHtml(item.role)}">
          <div class="agent-message-header">
            <strong>${escapeHtml(roleLabel)}</strong>
            <span>${extra}</span>
          </div>
          <p>${escapeHtml(item.content)}</p>
        </article>
      `;
    })
    .join("");
  transcript.scrollTop = transcript.scrollHeight;
}

function renderAgentContextPreview() {
  const cards = [
    traceCard("Provider", selectedAgentProviderLabel(), "当前前端会把请求发给这个外部智能体"),
    traceCard(
      "Retrieval",
      nodes["agent-include-retrieval"].checked ? "included" : "off",
      nodes["agent-include-retrieval"].checked ? "会附带 query 命中和 query type" : "不附带 query 命中"
    ),
    traceCard(
      "Evidence",
      nodes["agent-include-evidence"].checked ? "included" : "off",
      nodes["agent-include-evidence"].checked ? "会附带证据块、相关表和调用" : "不附带证据块"
    ),
    traceCard(
      "Draft",
      nodes["agent-include-answer-draft"].checked ? "included" : "off",
      nodes["agent-include-answer-draft"].checked ? "会附带本地 draft answer" : "只给外部智能体检索证据"
    ),
    traceCard("Window", String(numberValue(nodes["agent-context-window-input"], 2)), "控制证据展开的上下文范围"),
    traceCard("Related", String(numberValue(nodes["agent-related-limit-input"], 3)), "控制 related context 的条数"),
  ];
  nodes["agent-context-preview"].innerHTML = cards.join("");
}

function renderAgentMeta() {
  const provider = selectedAgentProvider();
  if (!provider) {
    nodes["agent-meta"].textContent = "当前还没有配置智能体服务";
    return;
  }
  nodes["agent-meta"].textContent = `${provider.label} · ${provider.model}`;
}

function renderRoutes(routes) {
  if (!routes.length) {
    renderEmpty(nodes["route-cloud"], "当前没有可展示的接口。");
    return;
  }
  const html = routes.map((route) => `<span class="route-pill">${escapeHtml(route)}</span>`).join("");
  nodes["route-cloud"].innerHTML = html;
}

function renderCounter(node, target) {
  const end = Number(target) || 0;
  const start = Number(node.dataset.value || 0);
  node.dataset.value = String(end);
  const duration = 600;
  const startedAt = performance.now();

  function frame(now) {
    const progress = Math.min((now - startedAt) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(start + (end - start) * eased);
    node.textContent = current.toLocaleString("zh-CN");
    if (progress < 1) {
      requestAnimationFrame(frame);
    }
  }

  requestAnimationFrame(frame);
}

function renderEmptyStates() {
  renderEmpty(nodes["query-results"], "输入一个问题之后，这里会展示检索命中。");
  renderEmpty(nodes["evidence-results"], "切到证据页签后，这里会展示证据块与上下文。");
  renderEmpty(nodes["answer-results"], "运行 answer 后，这里会展示 grounded 回答。");
  renderEmpty(nodes["trace-results"], "Bundle、query debug 和 evidence pruning 摘要会显示在这里。");
  renderEmpty(nodes["route-cloud"], "正在读取 API 路由。");
  renderEmpty(nodes["agent-transcript"], "正在初始化智能体面板。");
  nodes["agent-context-preview"].innerHTML = "";
}

function renderEmpty(node, message) {
  const template = document.getElementById("empty-state-template");
  const fragment = template.content.cloneNode(true);
  fragment.querySelector("p").textContent = message;
  node.innerHTML = "";
  node.appendChild(fragment);
}

function setStatus(message, mode) {
  nodes["status-text"].textContent = message;
  nodes["status-strip"].classList.toggle("is-loading", mode === "loading");
  const badge = nodes["status-strip"].querySelector(".status-badge");
  badge.textContent = mode === "loading" ? "处理中" : mode === "error" ? "异常" : "就绪";
}

function toggleResultLoading(loading) {
  document.querySelectorAll(".result-panel").forEach((panel) => {
    panel.classList.toggle("is-loading", loading);
  });
}

function traceCard(title, value, detail) {
  return `<article class="trace-card"><h4>${escapeHtml(title)}</h4><strong>${escapeHtml(value)}</strong><p>${escapeHtml(detail)}</p></article>`;
}

function currentDbPath() {
  return nodes["db-path"].value.trim();
}

function currentDbPathOrUndefined() {
  const value = currentDbPath();
  return value || undefined;
}

function numberValue(node, fallbackValue) {
  const parsed = Number(node.value);
  return Number.isFinite(parsed) && parsed > 0 ? parsed : fallbackValue;
}

function labelForAction(action) {
  return {
    all: "整套分析",
    query: "检索查询",
    evidence: "证据组装",
    answer: "回答生成",
    bundle: "Bundle 打包",
  }[action] || action;
}

async function runAgentChat() {
  const message = nodes["agent-input"].value.trim();
  if (!message) {
    setStatus("先输入一个问题，再发送给智能体。", "error");
    nodes["agent-input"].focus();
    return;
  }
  if (!selectedAgentProvider()) {
    setStatus("当前没有可用的智能体 provider，请先配置 .env。", "error");
    setPage("agent-view");
    return;
  }

  setPage("agent-view");
  state.agentConversation.push({ role: "user", content: message, meta: "本次问题" });
  renderAgentConversation();
  setStatus("正在把问题和本地代码证据一起发送给智能体…", "loading");
  nodes["agent-send"].disabled = true;

  try {
    const response = await fetchAgentChat(message);
    state.agentLastResponse = response;
    state.agentConversation.push({
      role: "assistant",
      content: response.reply || "智能体没有返回文本内容。",
      meta: `${response.provider?.label || response.provider?.name || "agent"} · ${response.latency_ms || 0}ms`,
    });
    nodes["agent-input"].value = "";
    renderAgentConversation();
    renderAgentMeta();
    setStatus("智能体回答已返回。", "ready");
  } catch (error) {
    setStatus(error.message, "error");
  } finally {
    nodes["agent-send"].disabled = !selectedAgentProvider();
  }
}

function selectedAgentProvider() {
  const value = nodes["agent-provider-select"].value;
  return state.agentProviders.find((item) => item.name === value) || null;
}

function selectedAgentProviderLabel() {
  const provider = selectedAgentProvider();
  if (!provider) {
    return "not configured";
  }
  return `${provider.label} (${provider.model})`;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

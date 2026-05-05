/* browse.js — 代码库文件浏览面板
 * 适配后端 GET /browse 和 GET /file 接口
 */

(function () {
  const UI = window.__ui || {};

  let currentPath = '';
  let rootPath    = '';
  let treeCache   = null;
  let fileCache   = {};

  function init() {
    const btn = document.getElementById('browseReloadBtn');
    if (btn) btn.addEventListener('click', () => load(currentPath));
    load('');
  }

  async function load(path) {
    showBusy('preview-body', '正在加载目录…');

    // Ensure we always send relative paths to the API
    const relPath = (path || '').replace(/^\//, '');
    const dir = await fetchDirectory(relPath);
    if (!dir) {
      renderPath('');
      renderTree([]);
      showError('preview-body', '无法读取目录。');
      return;
    }
    treeCache = dir;

    // 首次加载记录 root 路径 (from absolute dir.path)
    if (!rootPath && dir.path) {
      rootPath = dir.path.replace(/\/?$/, '/');
    }

    // Always store currentPath as relative to root
    if (dir.path && rootPath && dir.path.startsWith(rootPath)) {
      currentPath = dir.path.slice(rootPath.length).replace(/^\//, '');
    } else {
      currentPath = relPath;
    }

    renderPath(dir.path || relPath);
    renderTree(dir.entries || []);

    if (dir.entries && dir.entries.length) {
      const first = dir.entries[0];
      if (first.kind === 'file') preview(first.name);
      else showIdle('preview-body', '选择文件预览');
    } else {
      showIdle('preview-body', '空目录');
    }
  }

  async function fetchDirectory(path) {
    // 后端 GET /browse?path=xxx
    let resp = await getJSON('/browse?path=' + encodeURIComponent(path || '')).catch(() => null);
    if (resp && !resp.error) {
      // 标准化 kind 字段
      if (resp.entries) {
        resp.entries.forEach(e => {
          e.is_dir = e.kind === 'dir';
          e.is_file = e.kind === 'file';
        });
      }
      return resp;
    }

    // Fallback：从 query 结果构造目录
    const db = UI.getDbPath && UI.getDbPath();
    resp = await postJSON('/query', { query: '', limit: 200, db_path: db }).catch(() => null);
    if (resp && resp.hits) {
      const seen = new Set();
      const prefix = path ? path + '/' : '';
      const entries = [];
      for (const h of resp.hits) {
        const fp = h.file_path || h.path || '';
        if (!fp.startsWith(prefix)) continue;
        const rest = fp.slice(prefix.length);
        if (!rest) continue;
        const slash = rest.indexOf('/');
        const name = slash === -1 ? rest : rest.slice(0, slash);
        const isDir = slash !== -1;
        const key = name + (isDir ? '/' : '');
        if (seen.has(key)) continue;
        seen.add(key);
        entries.push({ name, kind: isDir ? 'dir' : 'file', is_dir: isDir, is_file: !isDir });
      }
      return { path: prefix || '/', entries };
    }

    // 再 fallback：db-summary
    resp = await postJSON('/db-summary', { db_path: db }).catch(() => null);
    if (resp && resp.files) {
      const prefix = path ? path + '/' : '';
      const seen = new Set();
      const entries = [];
      for (const f of resp.files) {
        const fp = f.path || '';
        if (!fp.startsWith(prefix)) continue;
        const rest = fp.slice(prefix.length);
        if (!rest) continue;
        const slash = rest.indexOf('/');
        const name = slash === -1 ? rest : rest.slice(0, slash);
        const isDir = slash !== -1;
        const key = name + (isDir ? '/' : '');
        if (seen.has(key)) continue;
        seen.add(key);
        entries.push({ name, kind: isDir ? 'dir' : 'file', is_dir: isDir, is_file: !isDir });
      }
      return { path: prefix || '/', entries };
    }

    return null;
  }

  function renderPath(path) {
    const el = document.getElementById('browse-path');
    if (!el) return;
    // Convert absolute path to relative for breadcrumb navigation
    let relPath = path || '';
    if (rootPath && relPath.startsWith(rootPath)) {
      relPath = relPath.slice(rootPath.length).replace(/^\//, '');
    }
    const parts = relPath.split('/').filter(Boolean);
    let html = '<span data-path="" style="cursor:pointer;color:#60a5fa">根目录</span>';
    let acc = '';
    for (const p of parts) {
      acc += (acc ? '/' : '') + p;
      html += ' / <span data-path="' + esc(acc) + '" style="cursor:pointer;color:#60a5fa">' + esc(p) + '</span>';
    }
    el.innerHTML = html;
    el.querySelectorAll('span[data-path]').forEach(span => {
      span.addEventListener('click', () => load(span.dataset.path));
    });
  }

  function renderTree(entries) {
    const el = document.getElementById('browse-tree');
    if (!el) return;
    if (!entries.length) {
      el.innerHTML = '<div style="color:#7a94ad;font-size:.85rem;padding:8px">空目录</div>';
      return;
    }
    const sorted = [...entries].sort((a, b) => {
      if (a.is_dir && !b.is_dir) return -1;
      if (!a.is_dir && b.is_dir) return 1;
      return a.name.localeCompare(b.name);
    });
    el.innerHTML = sorted.map(e => {
      const icon = e.is_dir ? '📁' : getFileIcon(e.name);
      return (
        '<div class="browse-item" data-dir="' + (e.is_dir ? '1' : '0') +
        '" data-name="' + esc(e.name) + '">' +
        '<span class="bicon">' + icon + '</span>' +
        '<span class="bname">' + esc(e.name) + '</span></div>'
      );
    }).join('');

    el.querySelectorAll('.browse-item').forEach(item => {
      item.addEventListener('click', () => {
        const name = item.dataset.name;
        const isDir = item.dataset.dir === '1';
        if (isDir) {
          load(currentPath ? currentPath + '/' + name : name);
        } else {
          preview(name);
        }
      });
    });
  }

  async function preview(name) {
    const fullPath = currentPath ? currentPath + '/' + name : name;
    const headerEl = document.getElementById('preview-filename');
    const bodyEl   = document.getElementById('preview-body');

    if (headerEl) headerEl.textContent = fullPath;
    if (!bodyEl) return;

    bodyEl.innerHTML = '<div class="loading">加载中…</div>';

    const cacheKey = fullPath;

    if (fileCache[cacheKey]) {
      renderPreviewBody(bodyEl, fileCache[cacheKey], fullPath);
      return;
    }

    let text = null;
    let resp = await getJSON('/file?path=' + encodeURIComponent(fullPath)).catch(() => null);
    if (resp && resp.content !== undefined) {
      text = resp.content;
    } else {
      // fallback：从 query 匹配文本还原
      const db = UI.getDbPath && UI.getDbPath();
      resp = await postJSON('/query', { query: fullPath, limit: 10, db_path: db }).catch(() => null);
      if (resp && resp.hits) {
        const hit = resp.hits.find(h => h.file_path === fullPath || h.procedure_name === name);
        if (hit) text = hit.matched_text || hit.excerpt || JSON.stringify(hit, null, 2);
      }
    }

    if (text === null) {
      bodyEl.innerHTML = '<div class="error">无法读取文件内容。</div>';
      return;
    }

    fileCache[cacheKey] = text;
    renderPreviewBody(bodyEl, text, fullPath);
  }

  function renderPreviewBody(el, text, path) {
    const ext = (path.split('.').pop() || '').toLowerCase();
    const langMap = {
      'py':'python','js':'javascript','ts':'typescript','java':'java',
      'json':'json','sql':'sql','sh':'bash','md':'markdown',
      'go':'go','rs':'rust','c':'c','cpp':'cpp','h':'c','hpp':'cpp'
    };
    const codeLang = langMap[ext] || 'java';

    el.innerHTML = '<pre><code class="language-' + esc(codeLang) + '">' + esc(text) + '</code></pre>';
    if (window.hljs) {
      el.querySelectorAll('code').forEach(function(block) { hljs.highlightElement(block); });
    }
  }

  function copyPath() {
    const el = document.getElementById('preview-filename');
    if (!el) return;
    const path = el.textContent;
    navigator.clipboard.writeText(path).then(() => {
      notify('已复制: ' + path, 'success');
    }).catch(() => {
      notify('复制失败', 'error');
    });
  }

  function getFileIcon(name) {
    if (name.endsWith('.py')) return '🐍';
    if (name.endsWith('.js')) return '🟨';
    if (name.endsWith('.java')) return '☕';
    if (name.endsWith('.xml')) return '📄';
    if (name.endsWith('.json')) return '📋';
    if (name.endsWith('.md')) return '📝';
    if (name.endsWith('.sql')) return '🗃️';
    return '📄';
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, c =>
      c==='&'?'&amp;':c==='<'?'&lt;':c==='>'?'&gt;':c==='"'?'&quot;':'&#39;'
    );
  }

  function getJSON(url) {
    return fetch(url).then(r => r.ok ? r.json() : Promise.reject(r.status + ' ' + r.statusText));
  }
  function postJSON(url, body) {
    return fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body || {})
    }).then(r => r.ok ? r.json() : Promise.reject(r.status + ' ' + r.statusText));
  }

  function showBusy(id, msg) {
    const el = document.getElementById(id);
    if (el) el.innerHTML = '<div class="loading">' + esc(msg) + '</div>';
  }
  function showError(id, msg) {
    const el = document.getElementById(id);
    if (el) el.innerHTML = '<div class="error">' + esc(msg) + '</div>';
  }
  function showIdle(id, msg) {
    const el = document.getElementById(id);
    if (el) el.innerHTML = '<div class="text-center" style="color:#7a94ad">' + esc(msg) + '</div>';
  }
  function notify(msg, type) {
    if (window.notify) window.notify(msg, type);
    else if (window.__ui && window.__ui.notify) window.__ui.notify(msg, type);
  }

  window.__browse = { init, load, preview, copyPath, refresh: () => load(currentPath) };
  document.addEventListener('DOMContentLoaded', init);
})();

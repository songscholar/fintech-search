import { marked } from 'https://cdn.jsdelivr.net/npm/marked@12/lib/marked.esm.js';

let hljsReady = false;

function loadHljs() {
  return new Promise(function(resolve) {
    if (window.hljs) {
      hljsReady = true;
      return resolve(window.hljs);
    }
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js';
    script.onload = function() {
      hljsReady = true;
      resolve(window.hljs);
    };
    script.onerror = function() {
      console.warn('[markdown-renderer] highlight.js failed to load');
      resolve(null);
    };
    document.head.appendChild(script);
  });
}

const hljsPromise = loadHljs();

function escapeHtml(str) {
  return String(str)
    .replace(/\u0026/g, "\u0026amp;")
    .replace(/\u003c/g, "\u0026lt;")
    .replace(/\u003e/g, "\u0026gt;")
    .replace(/"/g, "\u0026quot;")
    .replace(/'/g, "\u0026#39;");
}

function highlightCode(code, lang) {
  if (!hljsReady || !window.hljs) return escapeHtml(code);
  try {
    if (window.hljs.getLanguage && window.hljs.getLanguage(lang)) {
      return window.hljs.highlight(code, { language: lang, ignoreIllegals: true }).value;
    }
    return window.hljs.highlightAuto(code).value;
  } catch (e) {
    return escapeHtml(code);
  }
}

function renderCodeBlock(code, infostring) {
  var lang = (infostring || '').trim() || 'text';
  var trimmedCode = code.trimEnd();
  var lines = trimmedCode.split('\n');
  var lineCount = lines.length;

  // Build gutter (line numbers)
  var gutterHtml = '';
  for (var i = 1; i <= lineCount; i++) {
    gutterHtml += '<span class="line">' + i + '</span><br>';
  }

  // Highlight code
  var highlighted = highlightCode(trimmedCode, lang);

  // Wrap each line
  var codeLines = highlighted.split('\n');
  if (codeLines.length > 0 && codeLines[codeLines.length - 1].trim() === '') {
    codeLines.pop();
  }
  var codeHtml = codeLines.map(function(line) {
    return '<span class="line">' + line + '</span><br>';
  }).join('');

  var toolsHtml = '<div class="highlight-tools">' +
    '<span class="code-lang">' + escapeHtml(lang).toUpperCase() + '</span>' +
    '<div class="copy-notice"></div>' +
    '<div class="toolbar-actions">' +
      '<span class="action-btn copy-button">Copy</span>' +
      '<span class="action-btn expand">&#9662;</span>' +
    '</div>' +
    '</div>';

  return '<figure class="highlight ' + escapeHtml(lang) + '" data-line-count="' + lineCount + '">' +
    toolsHtml +
    '<table><tbody><tr>' +
    '<td class="gutter"><pre><code>' + gutterHtml + '</code></pre></td>' +
    '<td class="code"><pre><code class="hljs">' + codeHtml + '</code></pre></td>' +
    '</tr></tbody></table>' +
    '</figure>';
}

marked.use({
  renderer: {
    code(code, infostring, escaped) {
      return renderCodeBlock(code, infostring);
    }
  }
});

export async function renderMarkdown(markdown) {
  await hljsPromise;
  return Promise.resolve(marked.parse(String(markdown || '').replace(/\r\n/g, '\n')));
}

window.__renderMarkdown = renderMarkdown;

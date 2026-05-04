import { marked } from '/assets/marked.esm.js';

const _markedAvailable = typeof marked === 'function' && typeof marked.parse === 'function';
if (!_markedAvailable) {
  console.error('[markdown-renderer] marked import failed — marked is:', typeof marked);
}

let hljsReady = false;

function loadHljs() {
  return new Promise(function(resolve) {
    if (window.hljs) {
      hljsReady = true;
      return resolve(window.hljs);
    }
    var script = document.createElement('script');
    script.src = '/assets/highlight.min.js';
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

function loadMermaid() {
  return new Promise(function(resolve) {
    if (window.mermaid) return resolve(window.mermaid);
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js';
    script.onload = function() {
      window.mermaid.initialize({
        startOnLoad: false,
        theme: 'neutral',
        securityLevel: 'loose',
      });
      resolve(window.mermaid);
    };
    script.onerror = function() {
      console.warn('[markdown-renderer] mermaid failed to load');
      resolve(null);
    };
    document.head.appendChild(script);
  });
}

const hljsPromise = loadHljs();
const mermaidPromise = loadMermaid();

let _mermaidBlocks = [];
let _mermaidIdCounter = 0;

// Known language identifiers for fenced code blocks
var KNOWN_LANGS = [
  'mermaid','javascript','js','typescript','ts','python','py','java','c','cpp',
  'csharp','cs','go','rust','ruby','php','swift','kotlin','scala','sql','json',
  'yaml','yml','xml','html','css','scss','less','bash','sh','shell','zsh',
  'powershell','ps1','dockerfile','makefile','cmake','lua','r','matlab',
  'perl','haskell','elixir','clojure','lisp','scheme','erlang','dart','vue',
  'svelte','jsx','tsx','graphql','toml','ini','conf','nginx','apache',
  'markdown','md','text','txt','plaintext','plain','log','diff','patch',
  'latex','tex','bibtex','csv','tsv','protobuf','thrift','avro',
];

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/**
 * Preprocess markdown to fix common LLM code block issues:
 * 1. Move language identifier from separate line to same line as opening fence
 * 2. Preserve indentation inside code blocks
 */
function preprocessMarkdown(md) {
  // Fix: ```\nmermaid\n... → ```mermaid\n...
  // Match opening fence with language on next line
  return md.replace(/```\s*\n([a-zA-Z][a-zA-Z0-9_-]*)\n/g, function(match, lang) {
    if (KNOWN_LANGS.indexOf(lang.toLowerCase()) >= 0) {
      return '```' + lang + '\n';
    }
    return match;
  });
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

function sanitizeMermaidCode(code) {
  var s = code
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
  s = s.replace(/<br\s*\/?>/gi, '\n');
  s = s.replace(/<\/?[^>]+(>|$)/g, '');
  return s.trim();
}

function renderCodeBlock(code, infostring) {
  var lang = (infostring || '').trim() || '';

  // Fallback: if lang is empty, check if code starts with a known language identifier
  if (!lang) {
    var firstNewline = code.indexOf('\n');
    if (firstNewline > 0) {
      var firstLine = code.substring(0, firstNewline).trim().toLowerCase();
      if (KNOWN_LANGS.indexOf(firstLine) >= 0) {
        lang = firstLine;
        code = code.substring(firstNewline + 1);
      }
    }
  }

  // Mermaid: return placeholder for post-processing
  if (lang === 'mermaid') {
    var id = 'mermaid-' + (++_mermaidIdCounter);
    _mermaidBlocks.push({ id: id, code: code.trim() });
    return '<div class="mermaid-container" data-mermaid-id="' + id + '"></div>';
  }

  if (!lang) lang = 'text';

  // Preserve original indentation — do NOT trimEnd or strip leading spaces
  var trimmedCode = code.replace(/\s+$/, '');
  var lines = trimmedCode.split('\n');
  var lineCount = lines.length;

  // Build gutter (line numbers)
  var gutterHtml = '';
  for (var i = 1; i <= lineCount; i++) {
    gutterHtml += '<span class="line">' + i + '</span><br>';
  }

  // Highlight code (escapeHtml first to prevent XSS, then highlight)
  var safeCode = escapeHtml(trimmedCode);
  var highlighted;
  if (hljsReady && window.hljs) {
    try {
      if (window.hljs.getLanguage && window.hljs.getLanguage(lang)) {
        highlighted = window.hljs.highlight(trimmedCode, { language: lang, ignoreIllegals: true }).value;
      } else {
        highlighted = window.hljs.highlightAuto(trimmedCode).value;
      }
    } catch (e) {
      highlighted = safeCode;
    }
  } else {
    highlighted = safeCode;
  }

  // Split highlighted code by lines and wrap each in <span class="line">
  var codeLines = highlighted.split('\n');
  // Remove trailing empty line if present
  if (codeLines.length > 0 && codeLines[codeLines.length - 1].trim() === '') {
    codeLines.pop();
  }
  var codeHtml = codeLines.map(function(line) {
    // Use &nbsp; for leading spaces to prevent browser from collapsing them
    var preservedLine = line.replace(/^( +)/, function(spaces) {
      return '&nbsp;'.repeat(spaces.length);
    });
    return '<span class="line">' + preservedLine + '</span>';
  }).join('\n');

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

async function renderMermaidBlocks() {
  if (_mermaidBlocks.length === 0) return;
  var blocks = _mermaidBlocks;
  _mermaidBlocks = [];
  var mermaid = await mermaidPromise;
  if (!mermaid) {
    for (var i = 0; i < blocks.length; i++) {
      var block = blocks[i];
      var el = document.querySelector('[data-mermaid-id="' + block.id + '"]');
      if (el) {
        el.outerHTML = '<pre><code>' + escapeHtml(block.code) + '</code></pre>';
      }
    }
    return;
  }
  for (var i = 0; i < blocks.length; i++) {
    var block = blocks[i];
    var el = document.querySelector('[data-mermaid-id="' + block.id + '"]');
    if (!el) continue;
    try {
      var cleanCode = sanitizeMermaidCode(block.code);
      var graphId = block.id + '-svg';
      var result = await mermaid.render(graphId, cleanCode);
      el.innerHTML = result.svg;
    } catch (e) {
      el.className = 'mermaid-error';
      el.textContent = 'Mermaid 渲染失败: ' + (e.message || e);
    }
  }
}

export async function renderMarkdown(markdown) {
  _mermaidBlocks = [];
  _mermaidIdCounter = 0;
  await hljsPromise;
  var text = String(markdown || '').replace(/\r\n/g, '\n');
  if (!_markedAvailable) {
    return '<div class="assistant-content-fallback" style="white-space:pre-wrap;font-family:var(--font-mono,monospace);color:inherit;background:transparent;">' + escapeHtml(text) + '</div>';
  }
  try {
    var cleaned = preprocessMarkdown(text);
    var html = marked.parse(cleaned);
    if (_mermaidBlocks.length > 0) {
      setTimeout(renderMermaidBlocks, 0);
    }
    return html;
  } catch (e) {
    console.warn('[renderMarkdown] marked.parse failed, using escapeHtml fallback:', e);
    return '<div class="assistant-content-fallback" style="white-space:pre-wrap;font-family:var(--font-mono,monospace);color:inherit;background:transparent;">' + escapeHtml(text) + '</div>';
  }
}

window.__renderMarkdown = renderMarkdown;

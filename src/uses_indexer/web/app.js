let renderMarkdown = async function(md) {
  var text = String(md || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  return '<pre style="white-space:pre-wrap;font-family:var(--font-mono,monospace);color:#b0c4de;">' + text + '</pre>';
};
import('/assets/markdown-renderer.js').then(function(mod) {
  if (mod && mod.renderMarkdown) renderMarkdown = mod.renderMarkdown;
}).catch(function(err) {
  console.warn('[app] markdown-renderer unavailable, using fallback:', err);
});

// Compatibility marker for legacy smoke tests: initializeConsole.

/* ==========================================================================
   USES Indexer — Frontend App
   Rain glass effect + real API calls
   ========================================================================== */

// ========================================================================
// Rain Effect (WebGL) — adapted from personal-website rain-effect.js
// ========================================================================
(function() {
  'use strict';
  var canvas, gl, prog, u, texture, bgCanvas;
  var rafId;
  var startTime = performance.now();
  var isRunning = false;
  var needsTextureUpdate = true;

  // Media state
  var defaultImg = null;
  var uploadImg = null;
  var uploadVid = null;
  var uploadUrl = null;
  var currentMode = 'gradient'; // 'gradient' | 'uploadImage' | 'uploadVideo'

  window.__rainConfig = {
    rain: 0.55,
    fog: 0.25,
    refract: 1.0,
    glass: 0.0,
    speed: 0.2
  };

  window.__rainMedia = {
    mode: function() { return currentMode; },
    setMode: function(m) { setMediaMode(m); },
    reset: function() { setMediaMode('gradient'); },
    setUpload: function(file) { loadUpload(file); }
  };

  var VERT = [
    'precision highp float;',
    'attribute vec2 a_pos;',
    'varying vec2 v_uv;',
    'void main(){',
    '  v_uv = a_pos * 0.5 + 0.5;',
    '  gl_Position = vec4(a_pos, 0.0, 1.0);',
    '}'
  ].join('\n');

  var FRAG = [
    'precision highp float;',
    'uniform float u_time;',
    'uniform vec2 u_res;',
    'uniform float u_rain;',
    'uniform float u_fog;',
    'uniform float u_refract;',
    'uniform float u_glass;',
    'uniform float u_speed;',
    'uniform sampler2D u_tex;',
    'varying vec2 v_uv;',
    '#define S(a,b,t) smoothstep(a,b,t)',
    'vec3 N13(float p){',
    '  vec3 p3 = fract(vec3(p)*vec3(.1031,.11369,.13787));',
    '  p3 += dot(p3,p3.yzx+19.19);',
    '  return fract(vec3((p3.x+p3.y)*p3.z,(p3.x+p3.z)*p3.y,(p3.y+p3.z)*p3.x));',
    '}',
    'float N(float t){return fract(sin(t*12345.564)*7658.76);}',
    'float Saw(float b,float t){return S(0.,b,t)*S(1.,b,t);}',
    'vec2 DropLayer2(vec2 uv,float t){',
    '  vec2 UV=uv;',
    '  uv.y += t*0.75;',
    '  vec2 a=vec2(6.,3.);',
    '  vec2 grid=a*2.;',
    '  vec2 id=floor(uv*grid);',
    '  float colShift=N(id.x);',
    '  uv.y += colShift;',
    '  id=floor(uv*grid);',
    '  vec3 n=N13(id.x*35.2+id.y*2376.1);',
    '  vec2 st=fract(uv*grid)-vec2(.5,0);',
    '  float x=n.x-.5;',
    '  float y=UV.y*20.;',
    '  float wiggle=sin(y+sin(y));',
    '  x += wiggle*(.5-abs(x))*(n.z-.5);',
    '  x *= .7;',
    '  float ti=fract(t+n.z);',
    '  y=(Saw(.85,ti)-.5)*.9+.5;',
    '  vec2 p=vec2(x,y);',
    '  float d=length((st-p)*a.yx);',
    '  float mainDrop=S(.35,.0,d);',
    '  float r=sqrt(S(1.,y,st.y));',
    '  float cd=abs(st.x-x);',
    '  float trail=S(.23*r,.15*r*r,cd);',
    '  float trailFront=S(-.02,.02,st.y-y);',
    '  trail *= trailFront*r*r;',
    '  y=UV.y;',
    '  float trail2=S(.2*r,.0,cd);',
    '  float droplets=max(0.,(sin(y*(1.-y)*120.)-st.y))*trail2*trailFront*n.z;',
    '  y=fract(y*10.)+(st.y-.5);',
    '  float dd=length(st-vec2(x,y));',
    '  droplets=S(.3,0.,dd);',
    '  float m=mainDrop+droplets*r*trailFront;',
    '  return vec2(m,trail);',
    '}',
    'float StaticDrops(vec2 uv,float t){',
    '  uv *= 40.;',
    '  vec2 id=floor(uv);',
    '  uv=fract(uv)-.5;',
    '  vec3 n=N13(id.x*107.45+id.y*3543.654);',
    '  vec2 p=(n.xy-.5)*.7;',
    '  float d=length(uv-p);',
    '  float fade=Saw(.025,fract(t+n.z));',
    '  float c=S(.25,0.,d)*fract(n.z*10.)*fade;',
    '  return c*1.2;',
    '}',
    'vec2 Drops(vec2 uv,float t,float l0,float l1,float l2){',
    '  float s=StaticDrops(uv,t)*l0;',
    '  vec2 m1=DropLayer2(uv,t)*l1;',
    '  vec2 m2=DropLayer2(uv*1.85,t)*l2;',
    '  float c=s+m1.x+m2.x;',
    '  c=S(.2,.95,c);',
    '  return vec2(c,max(m1.y*l0,max(m2.y*l1,s)));',
    '}',
    'void main(){',
    '  vec2 uv=(v_uv-.5)*u_res/min(u_res.x,u_res.y);',
    '  float t=u_time*u_speed;',
    '  float rain=u_rain;',
    '  float staticDrops=S(-.5,1.,rain)*1.0;',
    '  float layer1=S(.25,.75,rain);',
    '  float layer2=S(.0,.5,rain);',
    '  vec2 c=Drops(uv,t,staticDrops,layer1,layer2);',
    '  vec2 e=vec2(.001,0.);',
    '  float cx=Drops(uv+e,t,staticDrops,layer1,layer2).x;',
    '  float cy=Drops(uv+e.yx,t,staticDrops,layer1,layer2).x;',
    '  vec2 n=vec2(cx-c.x,cy-c.x)*u_refract;',
    '  float focus=mix(max(0.,1.-c.x*2.2),0.,0.45);',
    '  vec2 texUV=v_uv;',
    '  texUV.y=1.0-texUV.y;',
    '  vec3 col=texture2D(u_tex,texUV+n).rgb;',
    '  float glassFactor=max(0.1,pow(max(0.0,1.0-u_glass),0.35));',
    '  vec3 blurredCol=vec3(0.);',
    '  float total=0.;',
    '  float radius=0.007*(0.5+u_fog*1.8)*glassFactor;',
    '  for(float i=-1.;i<=1.;i++){',
    '    for(float j=-1.;j<=1.;j++){',
    '      vec2 off=vec2(i,j)*radius;',
    '      blurredCol += texture2D(u_tex,texUV+n+off).rgb;',
    '      total += 1.;',
    '    }',
    '  }',
    '  blurredCol /= total;',
    '  col=mix(col,blurredCol,S(0.,1.,c.y*2.2));',
    '  col=mix(col,blurredCol,(1.-focus)*(1.0-u_glass*0.85));',
    '  col=(col-.5)*1.08+.5;',
    '  float spec=pow(max(0.,dot(normalize(vec3(n,1.)),normalize(vec3(.3,.5,1.)))),12.);',
    '  col += spec*c.x*.65;',
    '  col += c.x*vec3(.04,.06,.10);',
    '  col += c.x*0.04;',
    '  gl_FragColor=vec4(col,1.);',
    '}'
  ].join('\n');

  function compile(type, src) {
    var s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
      console.error('Rain shader error:', gl.getShaderInfoLog(s));
      gl.deleteShader(s);
      return null;
    }
    return s;
  }

  function initGL() {
    canvas = document.getElementById('rainCanvas');
    if (!canvas) return false;
    gl = canvas.getContext('webgl', { antialias: false, alpha: false, premultipliedAlpha: false });
    if (!gl) { console.warn('WebGL not supported'); return false; }

    var vs = compile(gl.VERTEX_SHADER, VERT);
    var fs = compile(gl.FRAGMENT_SHADER, FRAG);
    if (!vs || !fs) return false;

    prog = gl.createProgram();
    gl.attachShader(prog, vs);
    gl.attachShader(prog, fs);
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) {
      console.error('Rain link error:', gl.getProgramInfoLog(prog));
      return false;
    }
    gl.useProgram(prog);

    var pos = new Float32Array([-1,-1, 1,-1, -1,1, 1,1]);
    var pb = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, pb);
    gl.bufferData(gl.ARRAY_BUFFER, pos, gl.STATIC_DRAW);
    var pl = gl.getAttribLocation(prog, 'a_pos');
    gl.enableVertexAttribArray(pl);
    gl.vertexAttribPointer(pl, 2, gl.FLOAT, false, 0, 0);

    u = {
      time: gl.getUniformLocation(prog, 'u_time'),
      res: gl.getUniformLocation(prog, 'u_res'),
      rain: gl.getUniformLocation(prog, 'u_rain'),
      fog: gl.getUniformLocation(prog, 'u_fog'),
      refract: gl.getUniformLocation(prog, 'u_refract'),
      glass: gl.getUniformLocation(prog, 'u_glass'),
      speed: gl.getUniformLocation(prog, 'u_speed'),
      tex: gl.getUniformLocation(prog, 'u_tex')
    };
    gl.uniform1i(u.tex, 0);
    bgCanvas = document.createElement('canvas');
    return true;
  }

  function resize() {
    if (!canvas || !gl) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 1.5);
    var w = Math.floor(window.innerWidth * dpr);
    var h = Math.floor(window.innerHeight * dpr);
    canvas.width = w; canvas.height = h;
    canvas.style.width = window.innerWidth + 'px';
    canvas.style.height = window.innerHeight + 'px';
    gl.viewport(0, 0, w, h);
  }

  // ============ Default background image ============

  function createDefaultImage() {
    var img = new Image();
    img.onload = function() {
      defaultImg = img;
      needsTextureUpdate = true;
    };
    img.onerror = function() {
      console.warn('Default background image failed to load');
      defaultImg = null;
      needsTextureUpdate = true;
    };
    img.src = '/assets/bg.png';
  }

  // ============ Media loading ============

  function loadUpload(file) {
    if (!file) return;
    if (uploadUrl) { URL.revokeObjectURL(uploadUrl); uploadUrl = null; }
    if (uploadImg) { uploadImg = null; }
    if (uploadVid) { uploadVid.pause(); uploadVid = null; }

    uploadUrl = URL.createObjectURL(file);

    if (file.type.startsWith('video/')) {
      uploadVid = document.createElement('video');
      uploadVid.src = uploadUrl;
      uploadVid.loop = true;
      uploadVid.muted = true;
      uploadVid.playsInline = true;
      uploadVid.autoplay = true;
      uploadVid.play().catch(function(){});
      currentMode = 'uploadVideo';
    } else {
      uploadImg = new Image();
      uploadImg.onload = function() { needsTextureUpdate = true; };
      uploadImg.src = uploadUrl;
      currentMode = 'uploadImage';
    }
    needsTextureUpdate = true;
  }

  function setMediaMode(mode) {
    currentMode = mode;
    needsTextureUpdate = true;
  }

  // ============ Texture update ============

  function drawMedia(ctx, w, h, media) {
    if (!media) return false;
    var mw = media.videoWidth || media.naturalWidth || media.width || 1;
    var mh = media.videoHeight || media.naturalHeight || media.height || 1;
    var mr = mw / mh;
    var cr = w / h;
    var dw = w, dh = h;
    if (cr > mr) dh = w / mr;
    else dw = h * mr;
    ctx.drawImage(media, (w - dw) / 2, (h - dh) / 2, dw, dh);
    return true;
  }

  function drawDefaultBackground(ctx, w, h) {
    if (defaultImg) {
      drawMedia(ctx, w, h, defaultImg);
      return;
    }
    // Fallback gradient
    var grad = ctx.createLinearGradient(0, 0, w, h);
    grad.addColorStop(0, '#0f172a');
    grad.addColorStop(0.5, '#1e293b');
    grad.addColorStop(1, '#0b1221');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);
  }

  function updateTexture() {
    if (!gl || !bgCanvas) return;
    var w = Math.floor(window.innerWidth);
    var h = Math.floor(window.innerHeight);
    bgCanvas.width = w; bgCanvas.height = h;
    var ctx = bgCanvas.getContext('2d');

    var drawn = false;
    if (currentMode === 'uploadVideo' && uploadVid && uploadVid.readyState >= 2) {
      drawn = drawMedia(ctx, w, h, uploadVid);
    } else if (currentMode === 'uploadImage' && uploadImg && uploadImg.complete) {
      drawn = drawMedia(ctx, w, h, uploadImg);
    }

    if (!drawn) {
      drawDefaultBackground(ctx, w, h);
    }

    if (!texture) texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, bgCanvas);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
  }

  // ============ Render loop ============

  function render() {
    if (!isRunning || !gl) return;
    var elapsed = (performance.now() - startTime) / 1000.0;
    var w = canvas.width, h = canvas.height;
    var cfg = window.__rainConfig || {};

    var isVideo = currentMode === 'uploadVideo';
    if (needsTextureUpdate || isVideo) {
      updateTexture();
      needsTextureUpdate = false;
    }

    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.uniform1f(u.time, elapsed);
    gl.uniform2f(u.res, w, h);
    gl.uniform1f(u.rain, cfg.rain != null ? cfg.rain : 0.55);
    gl.uniform1f(u.fog, cfg.fog != null ? cfg.fog : 0.25);
    gl.uniform1f(u.refract, cfg.refract != null ? cfg.refract : 1.0);
    gl.uniform1f(u.glass, cfg.glass != null ? cfg.glass : 0.0);
    gl.uniform1f(u.speed, cfg.speed != null ? cfg.speed : 0.2);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    rafId = requestAnimationFrame(render);
  }

  function onResize() { resize(); needsTextureUpdate = true; }

  window.initRain = function() {
    if (isRunning) return;
    if (!document.getElementById('rainCanvas')) {
      var rc = document.createElement('canvas');
      rc.id = 'rainCanvas';
      rc.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;pointer-events:none;';
      document.body.insertBefore(rc, document.body.firstChild);
    }
    if (!initGL()) return;
    resize();
    createDefaultImage();
    needsTextureUpdate = true;
    startTime = performance.now();
    isRunning = true;
    window.addEventListener('resize', onResize);
    rafId = requestAnimationFrame(render);
  };

  window.destroyRain = function() {
    isRunning = false;
    if (rafId) { cancelAnimationFrame(rafId); rafId = null; }
    window.removeEventListener('resize', onResize);
    var rc = document.getElementById('rainCanvas');
    if (rc && rc.parentNode) rc.parentNode.removeChild(rc);
    canvas = null; gl = null; prog = null; texture = null; bgCanvas = null;
    defaultImg = null;
    if (uploadVid) { uploadVid.pause(); uploadVid = null; }
    if (uploadUrl) { URL.revokeObjectURL(uploadUrl); uploadUrl = null; }
    uploadImg = null;
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { setTimeout(window.initRain, 50); });
  } else {
    setTimeout(window.initRain, 50);
  }
})();


// ========================================================================
// App Logic
// ========================================================================

const API_BASE = '';

// State
let currentView = 'search';
let currentTab = 'query';
let providers = [];
let lastRetrieval = null;
let lastEvidence = null;
let lastAnswer = null;
window.lastRetrieval = lastRetrieval;
window.lastEvidence = lastEvidence;
window.lastAnswer = lastAnswer;

// Chat history state
let chatHistories = [];
let currentChatId = null;
const CHAT_STORAGE_KEY = 'uses_indexer_chat_histories';

// DOM refs
const els = {};

function $(id) { return document.getElementById(id); }

// Agent chat state
let contextMode = 'codebase';
let chatAttachments = [];

// Command dropdown state
let commandDropdownVisible = false;
let commandDropdownIndex = -1;
let commandDropdownItems = [];

// MCP tools state
let mcpTools = [];

// Agent loop state
let agentAbortController = null;
let isAgentRunning = false;
let toolCallMap = new Map();

function initRefs() {
  els.statusDot = $('status-dot');
  els.statusText = $('status-text');
  els.dbPath = $('db-path');
  els.question = $('question-input');
  els.limit = $('limit-input');
  els.context = $('context-input');
  els.related = $('related-input');
  els.resultsCard = $('results-card');
  els.vectorStatusBar = $('vector-status-bar');
  els.queryResults = $('query-results');
  els.evidenceResults = $('evidence-results');
  els.answerResults = $('answer-results');
  els.traceResults = $('trace-results');
  els.queryMeta = $('query-meta');
  els.evidenceMeta = $('evidence-meta');
  els.answerMeta = $('answer-meta');
  els.chatTranscript = $('chat-transcript');
  els.chatInput = $('chat-input');
  els.agentProvider = $('agent-provider');
  els.toast = $('toast');
  // settings
  els.settingsOverlay = $('settingsOverlay');
  els.settingsPanel = $('settingsPanel');
  // context status tags
  els.ctxRetrieval = $('ctx-retrieval');
  els.ctxEvidence = $('ctx-evidence');
  els.ctxDraft = $('ctx-draft');
  // stats
  els.statProcedures = $('stat-procedures');
  els.statStatements = $('stat-statements');
  els.statChunks = $('stat-chunks');
  els.statBlocks = $('stat-blocks');
  els.statCalls = $('stat-calls');
  els.statTopics = $('stat-topics');
  els.routeList = $('route-list');
  // docs
  els.docsList = $('docs-list');
  els.docsPagination = $('docs-pagination');
  els.docDetailTitle = $('doc-detail-title');
  els.docDetailBody = $('doc-detail-body');
  els.docDetailEyebrow = $('doc-detail-eyebrow');
  // agent chat
  els.retrievalHints = $('retrieval-hints');
  els.attachmentList = $('attachment-list');
  els.chatHistoryList = $('chat-history-list');
  els.commandDropdown = $('command-dropdown');
  els.contextMode = $('context-mode');
}

// ========================================================================
// API helpers
// ========================================================================

async function apiPost(path, body) {
  const res = await fetch(API_BASE + path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });
  if (!res.ok) {
    const text = await res.text().catch(() => res.statusText);
    throw new Error(`${res.status}: ${text}`);
  }
  return res.json();
}

async function apiGet(path) {
  const res = await fetch(API_BASE + path);
  if (!res.ok) {
    const text = await res.text().catch(() => res.statusText);
    throw new Error(`${res.status}: ${text}`);
  }
  return res.json();
}

function postClientLog(level, event, message, context) {
  const payload = {
    level,
    event,
    message,
    context: {
      ...context,
      url: window.location.href,
      user_agent: navigator.userAgent,
      occurred_at: new Date().toISOString()
    }
  };
  fetch(API_BASE + '/client-log', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    keepalive: true
  }).catch(() => {});
}

window.addEventListener('error', event => {
  postClientLog('error', 'frontend_error', event.message || 'Frontend error', {
    filename: event.filename,
    lineno: event.lineno,
    colno: event.colno,
    stack: event.error && event.error.stack
  });
});

window.addEventListener('unhandledrejection', event => {
  const reason = event.reason;
  postClientLog('error', 'frontend_unhandledrejection', reason && reason.message ? reason.message : String(reason), {
    stack: reason && reason.stack
  });
});

// ========================================================================
// UI helpers
// ========================================================================

function showToast(msg, type) {
  els.toast.textContent = msg;
  els.toast.className = 'toast' + (type === 'error' ? ' error' : '');
  els.toast.classList.add('show');
  setTimeout(() => els.toast.classList.remove('show'), 2800);
}

function setLoading(btnId, loading) {
  const btn = $(btnId);
  if (!btn) return;
  btn.disabled = loading;
  const icon = btn.querySelector('.btn-icon');
  if (loading) {
    if (icon) icon.style.display = 'none';
    if (!btn.querySelector('.loading-spinner')) {
      const s = document.createElement('span');
      s.className = 'loading-spinner';
      btn.insertBefore(s, btn.firstChild);
    }
  } else {
    const s = btn.querySelector('.loading-spinner');
    if (s) s.remove();
    if (icon) icon.style.display = '';
  }
}

function setServerStatus(ok, msg) {
  els.statusDot.className = 'status-dot' + (ok ? ' ready' : ' error');
  els.statusText.textContent = msg || (ok ? '就绪' : '异常');
}

// ========================================================================
// Navigation & Views
// ========================================================================

function setView(viewId) {
  currentView = viewId;
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  const view = $('view-' + viewId);
  const link = document.querySelector('.nav-link[data-view="' + viewId + '"]');
  if (view) view.classList.add('active');
  if (link) link.classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
  updateContextStatus();
  if (viewId === 'docs' && (!docFiles || docFiles.length === 0)) {
    loadDocs();
  }
}

function switchTab(tabId) {
  currentTab = tabId;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  const btn = document.querySelector('.tab-btn[data-tab="' + tabId + '"]');
  const pane = $('tab-' + tabId);
  if (btn) btn.classList.add('active');
  if (pane) pane.classList.add('active');
}

// ========================================================================
// Data fetching
// ========================================================================

async function checkHealth() {
  try {
    const data = await apiGet('/health');
    setServerStatus(true, data.status === 'ok' ? '就绪' : data.status);
  } catch (e) {
    setServerStatus(false, '未连接');
  }
}

async function loadDbSummary() {
  try {
    const data = await apiGet('/db-summary');
    const s = data || {};
    els.statProcedures.textContent = fmtNum(s.procedures);
    els.statStatements.textContent = fmtNum(s.statements);
    els.statChunks.textContent = fmtNum(s.chunks);
    els.statBlocks.textContent = fmtNum(s.blocks);
    const edgeTypes = s.edge_type_counts || {};
    els.statCalls.textContent = fmtNum(edgeTypes.calls_procedure);
    els.statTopics.textContent = fmtNum(edgeTypes.publishes_mc_topic);

    // route list from /health
    try {
      const health = await apiGet('/health');
      if (health.routes) {
        els.routeList.innerHTML = health.routes.map(r => {
          const method = r.split(' ')[0].toLowerCase();
          const path = r.split(' ').slice(1).join(' ');
          return `<span class="route-tag"><span class="route-method ${method}">${method}</span>${escapeHtml(path)}</span>`;
        }).join('');
      }
    } catch (_e) { /* ignore */ }

    // default db path
    if (s.db_path && !els.dbPath.value) {
      els.dbPath.placeholder = s.db_path;
    }
  } catch (e) {
    console.error('db-summary error', e);
  }
}

async function loadProviders() {
  try {
    const data = await apiGet('/agent/providers');
    providers = data.items || [];
    els.agentProvider.innerHTML = providers.map(p =>
      `<option value="${escapeHtml(p.name)}">${escapeHtml(p.label || p.name)}</option>`
    ).join('') || '<option value="">无可用模型</option>';
  } catch (e) {
    els.agentProvider.innerHTML = '<option value="">加载失败</option>';
  }
}

async function loadMcpTools() {
  try {
    const data = await apiGet('/agent/tools');
    mcpTools = data.tools || [];
    renderMcpToolSidebar();
  } catch (_e) {
    mcpTools = [];
  }
}

function renderMcpToolSidebar() {
  const container = document.getElementById('mcp-tool-list');
  if (!container) return;
  if (mcpTools.length === 0) {
    container.innerHTML = '<span class="sidebar-hint">暂无 MCP 工具</span>';
    return;
  }
  // Group tools by source
  const groups = {};
  for (const t of mcpTools) {
    const prefix = (t.source || 'other');
    if (!groups[prefix]) groups[prefix] = [];
    groups[prefix].push(t);
  }
  let html = '';
  for (const [source, tools] of Object.entries(groups)) {
    html += '<div class="tool-source-group">';
    html += '<div class="tool-source-label">' + escapeHtml(source) + '</div>';
    html += '<div class="tool-source-items">';
    for (const t of tools) {
      html += `<button class="mcp-tool-tag" onclick="insertToolCommand('${escapeHtml(t.name)}')" title="${escapeHtml(t.description || '')}">${escapeHtml(t.name)}</button>`;
    }
    html += '</div></div>';
  }
  container.innerHTML = html;
}

function insertToolCommand(toolName) {
  const input = els.chatInput;
  input.value = '/tool ' + toolName + ' ';
  input.focus();
}

function fmtNum(n) {
  if (n == null) return '—';
  return n.toLocaleString();
}

function escapeHtml(s) {
  if (s == null) return '';
  return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

// ========================================================================
// Search actions
// ========================================================================

function getPayload() {
  return {
    db_path: els.dbPath.value.trim() || undefined,
    query: els.question.value.trim(),
    limit: parseInt(els.limit.value, 10) || 6,
    context_window: parseInt(els.context.value, 10) || 2,
    related_limit: parseInt(els.related.value, 10) || 3
  };
}

function validateQuery() {
  if (!els.question.value.trim()) {
    showToast('请输入问题', 'error');
    els.question.focus();
    return false;
  }
  return true;
}

function renderVectorStatus(status) {
  if (!els.vectorStatusBar) return;
  if (!status) {
    els.vectorStatusBar.hidden = true;
    return;
  }
  const enabled = status.enabled;
  const reason = status.reason || '';
  const indexModel = status.index_model || '?';
  const queryModel = status.query_model || '?';
  let cls = 'vector-status-ok';
  let html = '';
  if (enabled) {
    html = `<span class="vstatus-dot ok"></span> 向量召回已启用 · 模型: ${escapeHtml(String(indexModel))}`;
  } else if (reason === 'embedding_space_mismatch') {
    cls = 'vector-status-warn';
    html = `<span class="vstatus-dot warn"></span> 向量召回已降级 · 索引模型: ${escapeHtml(String(indexModel))} · 查询模型: ${escapeHtml(String(queryModel))} · 不匹配`;
  } else {
    cls = 'vector-status-warn';
    html = `<span class="vstatus-dot warn"></span> 向量召回不可用 · ${escapeHtml(String(reason))}`;
  }
  els.vectorStatusBar.className = 'vector-status-bar ' + cls;
  els.vectorStatusBar.innerHTML = html;
  els.vectorStatusBar.hidden = false;
}

async function runQuery() {
  if (!validateQuery()) return;
  setLoading('btn-query', true);
  try {
    const data = await apiPost('/query', { ...getPayload(), debug: true });
    lastRetrieval = data;
    window.lastRetrieval = data;
    renderQuery(data);
    renderVectorStatus(data.vector_status);
    renderTrace(data.debug, 'query');
    els.resultsCard.hidden = false;
    switchTab('query');
    showToast(`检索完成，${(data.hits || []).length} 条命中`);
  } catch (e) {
    showToast('检索失败: ' + e.message, 'error');
  } finally {
    setLoading('btn-query', false);
  }
}

async function runEvidence() {
  if (!validateQuery()) return;
  setLoading('btn-evidence', true);
  try {
    const data = await apiPost('/evidence', { ...getPayload(), debug: true });
    lastEvidence = data;
    window.lastEvidence = data;
    renderEvidence(data);
    renderVectorStatus(data.vector_status);
    renderTrace(data.debug, 'evidence');
    els.resultsCard.hidden = false;
    switchTab('evidence');
    showToast(`证据组装完成，${(data.evidence || []).length} 条`);
  } catch (e) {
    showToast('证据失败: ' + e.message, 'error');
  } finally {
    setLoading('btn-evidence', false);
  }
}

async function runAnswer() {
  if (!validateQuery()) return;
  setLoading('btn-answer', true);
  try {
    const p = getPayload();
    const data = await apiPost('/answer', { db_path: p.db_path, question: p.query, evidence_limit: p.limit, context_window: p.context_window, related_limit: p.related_limit, allow_draft_fallback: true });
    lastAnswer = data;
    window.lastAnswer = data;
    renderAnswer(data);
    els.resultsCard.hidden = false;
    switchTab('answer');
    showToast('回答生成完成');
  } catch (e) {
    showToast('回答失败: ' + e.message, 'error');
  } finally {
    setLoading('btn-answer', false);
  }
}

async function runAll() {
  if (!validateQuery()) return;
  setLoading('btn-all', true);
  try {
    const payload = getPayload();
    // Run sequentially: query -> evidence -> answer
    const q = await apiPost('/query', { ...payload, debug: true });
    lastRetrieval = q;
    renderQuery(q);
    renderTrace(q.debug, 'query');

    const e = await apiPost('/evidence', { ...payload, debug: true });
    lastEvidence = e;
    renderEvidence(e);
    renderTrace(e.debug, 'evidence');

    const a = await apiPost('/answer', { db_path: payload.db_path, question: payload.query, evidence_limit: payload.limit, context_window: payload.context_window, related_limit: payload.related_limit, allow_draft_fallback: true });
    lastAnswer = a;
    renderAnswer(a);

    els.resultsCard.hidden = false;
    switchTab('answer');
    showToast('整套分析完成');
  } catch (err) {
    showToast('分析失败: ' + err.message, 'error');
  } finally {
    setLoading('btn-all', false);
  }
}

async function runBundle() {
  if (!validateQuery()) return;
  setLoading('btn-bundle', true);
  try {
    const payload = getPayload();
    await apiPost('/debug-bundle', { db_path: payload.db_path, question: payload.query, limit: payload.limit, context_window: payload.context_window, related_limit: payload.related_limit });
    showToast('Debug Bundle 已生成');
  } catch (e) {
    showToast('Bundle 失败: ' + e.message, 'error');
  } finally {
    setLoading('btn-bundle', false);
  }
}

// ========================================================================
// Rendering
// ========================================================================

function renderQuery(data) {
  const results = data.hits || [];
  els.queryMeta.textContent = results.length + ' 条';
  if (!results.length) {
    els.queryResults.innerHTML = '<div class="empty-state">无命中结果</div>';
    return;
  }
  els.queryResults.innerHTML = results.map((r, i) => {
    const meta = [r.hit_type, r.retrieval_source, r.procedure_name, r.object_id].filter(Boolean).join(' · ');
    const text = (r.matched_text || '').substring(0, 320);
    return `
      <div class="result-item">
        <h4>${escapeHtml(r.procedure_name || '命中项 #' + (i+1))}</h4>
        <div class="result-meta">${escapeHtml(meta)}</div>
        <div class="result-code">${escapeHtml(text)}</div>
      </div>
    `;
  }).join('');
}

function renderEvidence(data) {
  const ev = data.evidence || [];
  els.evidenceMeta.textContent = ev.length + ' 条';
  if (!ev.length) {
    els.evidenceResults.innerHTML = '<div class="empty-state">无证据块</div>';
    return;
  }
  els.evidenceResults.innerHTML = ev.map((item, i) => {
    const text = (item.excerpt || item.matched_text || '').substring(0, 400);
    const meta = [item.procedure_name, item.retrieval_source, item.match_source, item.rank ? 'rank:' + item.rank : null].filter(Boolean).join(' · ');
    return `
      <div class="result-item">
        <h4>证据 #${i+1}${item.procedure_name ? ' — ' + escapeHtml(item.procedure_name) : ''}</h4>
        <div class="result-meta">${escapeHtml(meta)}</div>
        <div class="result-code">${escapeHtml(text)}</div>
      </div>
    `;
  }).join('');
}

function renderAnswer(data) {
  const text = data.answer || data.final_answer || data.draft_answer || '无回答';
  const source = data.answer_source || (data.draft_answer ? 'draft' : 'unknown');
  els.answerMeta.textContent = source;
  // Simple markdown-ish formatting
  let html = escapeHtml(text)
    .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/\*([^*]+)\*/g, '<em>$1</em>')
    .replace(/^#{1,6}\s+(.+)$/gm, '<strong>$1</strong>')
    .replace(/\n/g, '<br>');
  // Fix pre blocks
  html = html.replace(/<pre><code>([\s\S]*?)<\/code><\/pre>/g, (m, code) => {
    return '<pre><code>' + code.replace(/<br>/g, '\n') + '</code></pre>';
  });
  els.answerResults.innerHTML = `<div class="answer-body">${html}</div>`;
}

function renderTrace(debug, phase) {
  if (!debug) return;
  const items = [];
  if (debug.query_type) items.push({ label: 'Query Type', value: debug.query_type });
  if (debug.candidate_count != null) items.push({ label: 'Candidates', value: String(debug.candidate_count) });
  if (debug.evidence_count != null) items.push({ label: 'Evidence', value: String(debug.evidence_count) });
  if (debug.pruned_blocks != null) items.push({ label: 'Pruned', value: String(debug.pruned_blocks) });
  if (debug.rerank_strategy) items.push({ label: 'Rerank', value: debug.rerank_strategy });
  if (debug.answer_source) items.push({ label: 'Source', value: debug.answer_source });
  if (phase) items.push({ label: 'Phase', value: phase });

  if (!items.length) {
    els.traceResults.innerHTML = '<div class="empty-state">无调试信息</div>';
    return;
  }
  els.traceResults.innerHTML = items.map(it => `
    <div class="trace-item">
      <h4>${escapeHtml(it.label)}</h4>
      <strong>${escapeHtml(it.value)}</strong>
    </div>
  `).join('');
}

// ========================================================================
// Chat History Management
// ========================================================================

function loadChatHistories() {
  try {
    const raw = localStorage.getItem(CHAT_STORAGE_KEY);
    if (raw) {
      chatHistories = JSON.parse(raw);
    }
  } catch (e) {
    console.error('Failed to load chat histories', e);
    chatHistories = [];
  }
}

function saveChatHistories() {
  try {
    localStorage.setItem(CHAT_STORAGE_KEY, JSON.stringify(chatHistories));
  } catch (e) {
    console.error('Failed to save chat histories', e);
  }
}

function generateChatId() {
  return 'chat_' + Date.now() + '_' + Math.random().toString(36).slice(2, 8);
}

function generateChatTitle(text) {
  if (!text) return '新对话';
  const t = text.trim().replace(/\s+/g, ' ');
  return t.length > 24 ? t.slice(0, 24) + '…' : t;
}

function createNewChat() {
  const chat = {
    id: generateChatId(),
    title: '新对话',
    messages: [],
    mode: contextMode,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
  chatHistories.unshift(chat);
  saveChatHistories();
  currentChatId = chat.id;
  renderChatHistoryList();
  clearTranscript();
  chatAttachments = [];
  renderAttachmentList();
  showToast('已创建新对话');
}

function clearTranscript() {
  if (els.chatTranscript) els.chatTranscript.innerHTML = '';
}

function loadChat(chatId) {
  const chat = chatHistories.find(c => c.id === chatId);
  if (!chat) return;
  currentChatId = chatId;
  renderChatHistoryList();
  clearTranscript();
  chatAttachments = [];
  renderAttachmentList();
  // Restore mode
  if (chat.mode && chat.mode !== contextMode) {
    setContextMode(chat.mode);
  }
  // Restore messages
  for (const msg of chat.messages) {
    appendMessage(msg.text, msg.role === 'user' ? 'user' : 'assistant');
  }
}

function renameChat(chatId) {
  const chat = chatHistories.find(c => c.id === chatId);
  if (!chat) return;
  const input = document.getElementById('rename-input-' + chatId);
  if (input) {
    const newTitle = input.value.trim();
    if (newTitle) {
      chat.title = newTitle;
      saveChatHistories();
      renderChatHistoryList();
    }
    return;
  }
  // Enter rename mode
  renderChatHistoryList(chatId);
  const newInput = document.getElementById('rename-input-' + chatId);
  if (newInput) {
    newInput.focus();
    newInput.select();
  }
}

function cancelRename(chatId) {
  renderChatHistoryList();
}

function deleteChat(chatId) {
  if (!confirm('确定要删除这个对话吗？')) return;
  chatHistories = chatHistories.filter(c => c.id !== chatId);
  saveChatHistories();
  if (currentChatId === chatId) {
    if (chatHistories.length > 0) {
      loadChat(chatHistories[0].id);
    } else {
      currentChatId = null;
      clearTranscript();
      createNewChat();
    }
  } else {
    renderChatHistoryList();
  }
}

function addMessageToHistory(role, text) {
  if (!currentChatId) {
    createNewChat();
  }
  const chat = chatHistories.find(c => c.id === currentChatId);
  if (!chat) return;
  chat.messages.push({
    role: role,
    text: text,
    time: new Date().toISOString(),
  });
  // Auto-update title from first user message
  if (role === 'user' && chat.title === '新对话' && chat.messages.length <= 2) {
    chat.title = generateChatTitle(text);
  }
  chat.updatedAt = new Date().toISOString();
  // Move to top
  const idx = chatHistories.findIndex(c => c.id === currentChatId);
  if (idx > 0) {
    chatHistories.splice(idx, 1);
    chatHistories.unshift(chat);
  }
  saveChatHistories();
  renderChatHistoryList();
}

function renderChatHistoryList(renamingId) {
  if (!els.chatHistoryList) return;
  if (chatHistories.length === 0) {
    els.chatHistoryList.innerHTML = '<div class="empty-state" style="padding:20px 0;font-size:0.78rem;">暂无历史对话</div>';
    return;
  }
  els.chatHistoryList.innerHTML = chatHistories.map(chat => {
    const isActive = chat.id === currentChatId;
    const dateStr = new Date(chat.updatedAt).toLocaleDateString('zh-CN', { month: 'short', day: 'numeric' });
    if (renamingId === chat.id) {
      return `<div class="chat-history-item active">
        <input type="text" id="rename-input-${chat.id}" class="history-rename-input" value="${escapeHtml(chat.title)}" onkeydown="if(event.key==='Enter'){renameChat('${chat.id}')}else if(event.key==='Escape'){cancelRename('${chat.id}')}" onblur="renameChat('${chat.id}')" />
      </div>`;
    }
    return `<div class="chat-history-item ${isActive ? 'active' : ''}" onclick="loadChat('${chat.id}')">
      <div class="history-info">
        <span class="history-title">${escapeHtml(chat.title)}</span>
        <span class="history-meta">${dateStr} · ${chat.messages.length} 条</span>
      </div>
      <div class="history-actions" onclick="event.stopPropagation()">
        <button class="history-action-btn" onclick="renameChat('${chat.id}')" title="重命名">✎</button>
        <button class="history-action-btn delete" onclick="deleteChat('${chat.id}')" title="删除">×</button>
      </div>
    </div>`;
  }).join('');
}

function initChatHistory() {
  loadChatHistories();
  if (chatHistories.length === 0) {
    createNewChat();
  } else {
    currentChatId = chatHistories[0].id;
    loadChat(currentChatId);
  }
}

// ========================================================================
// Chat / Agent
// ========================================================================

function appendMessage(text, sender) {
  const div = document.createElement('div');
  div.className = 'chat-message ' + sender;
  const time = new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' });
  let html = escapeHtml(text)
    .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  div.innerHTML = html + `<div class="msg-time">${time}</div>`;
  els.chatTranscript.appendChild(div);
  els.chatTranscript.scrollTop = els.chatTranscript.scrollHeight;
}

function updateContextStatus() {
  if (els.ctxRetrieval) {
    const hasR = lastRetrieval && lastRetrieval.results && lastRetrieval.results.length;
    els.ctxRetrieval.textContent = '检索: ' + (hasR ? lastRetrieval.results.length + ' 条' : '无');
    els.ctxRetrieval.classList.toggle('active', !!hasR);
  }
  if (els.ctxEvidence) {
    const hasE = lastEvidence && lastEvidence.evidence && lastEvidence.evidence.length;
    els.ctxEvidence.textContent = '证据: ' + (hasE ? lastEvidence.evidence.length + ' 条' : '无');
    els.ctxEvidence.classList.toggle('active', !!hasE);
  }
  if (els.ctxDraft) {
    const hasD = lastAnswer && (lastAnswer.answer || lastAnswer.draft_answer);
    els.ctxDraft.textContent = '草稿: ' + (hasD ? '有' : '无');
    els.ctxDraft.classList.toggle('active', !!hasD);
  }
}

function toggleSettings() {
  const open = els.settingsPanel.classList.toggle('open');
  els.settingsOverlay.classList.toggle('open', open);
}

function updateRainConfig() {
  const cfg = window.__rainConfig || {};
  cfg.rain = parseFloat($('cfg-rain').value);
  cfg.fog = parseFloat($('cfg-fog').value);
  cfg.refract = parseFloat($('cfg-refract').value);
  cfg.speed = parseFloat($('cfg-speed').value);
  cfg.glass = parseFloat($('cfg-glass').value);
  $('val-rain').textContent = cfg.rain.toFixed(2);
  $('val-fog').textContent = cfg.fog.toFixed(2);
  $('val-refract').textContent = cfg.refract.toFixed(1);
  $('val-speed').textContent = cfg.speed.toFixed(2);
  $('val-glass').textContent = cfg.glass.toFixed(2);
}

function onBgModeClick(btn) {
  const mode = btn.dataset.mode;
  document.querySelectorAll('#bg-mode button').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  if (mode === 'gradient') {
    $('bg-upload-row').style.display = 'none';
    window.__rainMedia.setMode('gradient');
  } else {
    $('bg-upload-row').style.display = 'block';
    window.__rainMedia.setMode(mode);
  }
}

function onBgUpload(input) {
  const file = input.files[0];
  if (!file) return;
  window.__rainMedia.setUpload(file);
}

function setContextMode(mode) {
  contextMode = mode;
  const badge = document.getElementById('context-mode-badge');
  if (badge) badge.textContent = mode === 'codebase' ? '代码库模式' : '通用模式';
  const placeholder = mode === 'general'
    ? '输入问题，智能助手将基于通用知识回答...'
    : '输入问题，智能助手将结合代码库工具检索回答...';
  if (els.chatInput) els.chatInput.placeholder = placeholder;
  if (currentChatId) {
    const chat = chatHistories.find(c => c.id === currentChatId);
    if (chat && chat.mode !== mode) {
      chat.mode = mode;
      saveChatHistories();
    }
  }
}

function triggerFileUpload() {
  const input = $('file-upload');
  if (input) input.click();
}

function onFileSelected(event) {
  const files = event.target.files;
  if (!files || !files.length) return;
  const MAX_ATTACHMENTS = 5;
  const MAX_IMAGE_SIZE = 2 * 1024 * 1024; // 2MB

  for (const file of files) {
    if (chatAttachments.length >= MAX_ATTACHMENTS) {
      showToast('最多支持 5 个附件', 'error');
      break;
    }
    if (file.type.startsWith('image/')) {
      if (file.size > MAX_IMAGE_SIZE) {
        showToast('图片大小不能超过 2MB: ' + file.name, 'error');
        continue;
      }
      const reader = new FileReader();
      reader.onload = function(e) {
        chatAttachments.push({
          name: file.name,
          media_kind: 'image',
          mime_type: file.type,
          size_bytes: file.size,
          data_url: e.target.result
        });
        renderAttachmentList();
      };
      reader.readAsDataURL(file);
    } else {
      const reader = new FileReader();
      reader.onload = function(e) {
        chatAttachments.push({
          name: file.name,
          media_kind: 'file',
          mime_type: file.type || 'application/octet-stream',
          size_bytes: file.size,
          text_content: e.target.result
        });
        renderAttachmentList();
      };
      reader.readAsText(file);
    }
  }
  event.target.value = '';
}

function renderAttachmentList() {
  if (!els.attachmentList) return;
  els.attachmentList.innerHTML = chatAttachments.map((att, i) => {
    const thumb = att.media_kind === 'image' && att.data_url
      ? `<img src="${escapeHtml(att.data_url)}" class="attachment-thumb" alt="" />`
      : `<span style="font-size:1rem">📄</span>`;
    return `<div class="attachment-item">${thumb}<span class="attachment-name">${escapeHtml(att.name)}</span><button class="attachment-remove" onclick="removeAttachment(${i})">&times;</button></div>`;
  }).join('');
}

function removeAttachment(index) {
  chatAttachments.splice(index, 1);
  renderAttachmentList();
}

function clearChat() {
  if (!currentChatId) return;
  const chat = chatHistories.find(c => c.id === currentChatId);
  if (chat) {
    chat.messages = [];
    chat.title = '新对话';
    chat.updatedAt = new Date().toISOString();
    saveChatHistories();
    renderChatHistoryList();
  }
  els.chatTranscript.innerHTML = '';
  chatAttachments = [];
  renderAttachmentList();
}

// ========================================================================
// Global Document Search — dynamically injected (ported from blog)
// ========================================================================

(function installGlobalSearch() {
  var searchPanel = document.getElementById('globalSearchPanel');
  if (!searchPanel) {
    searchPanel = document.createElement('div');
    searchPanel.id = 'globalSearchPanel';
    searchPanel.className = 'global-search-panel';
    searchPanel.innerHTML = '' +
      '<div class="global-search-dialog" role="dialog" aria-modal="true" aria-label="Global search">' +
        '<div class="global-search-header">' +
          '<input id="globalSearchInput" class="global-search-input" type="search" placeholder="搜索说明文档..." autocomplete="off">' +
          '<button id="globalSearchClose" class="global-search-close" type="button" aria-label="Close search">' +
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><line x1="6" y1="6" x2="18" y2="18"></line><line x1="6" y1="18" x2="18" y2="6"></line></svg>' +
          '</button>' +
        '</div>' +
        '<div class="global-search-meta"><span id="globalSearchCount">0 entries</span><span>ESC / Ctrl+K</span></div>' +
        '<div id="globalSearchResults" class="global-search-results"></div>' +
      '</div>';
    document.body.appendChild(searchPanel);
  }

  // Inject search trigger button into nav-right (before settings button)
  if (!document.getElementById('globalSearchTrigger')) {
    var trigger = document.createElement('button');
    trigger.id = 'globalSearchTrigger';
    trigger.className = 'nav-icon-btn';
    trigger.type = 'button';
    trigger.setAttribute('aria-label', 'Open search');
    trigger.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"></circle><line x1="20" y1="20" x2="16.65" y2="16.65"></line></svg>';
    var navRight = document.querySelector('#navbar .nav-right');
    if (navRight && navRight.firstChild) {
      navRight.insertBefore(trigger, navRight.firstChild);
    } else if (navRight) {
      navRight.appendChild(trigger);
    }
  }

  // Search state
  var docSearchIndex = [];
  var docSearchIndexReady = false;
  var docSearchIndexBuilding = false;

  function buildDocSearchIndex() {
    if (docSearchIndexReady || docSearchIndexBuilding) return Promise.resolve();
    docSearchIndexBuilding = true;
    return apiGet('/docs').then(function(list) {
      var files = list.files || [];
      var results = [];
      function fetchBatch(start) {
        if (start >= files.length) {
          docSearchIndex = results;
          docSearchIndexReady = true;
          docSearchIndexBuilding = false;
          return;
        }
        var batch = files.slice(start, start + 5);
        return Promise.all(batch.map(function(f) {
          return apiGet('/docs/' + encodeURIComponent(f.name)).catch(function() { return null; });
        })).then(function(contents) {
          batch.forEach(function(f, idx) {
            var content = contents[idx];
            var body = content ? (content.content || '') : '';
            var excerpt = body.replace(/[#*`>\-]/g, ' ').replace(/\s+/g, ' ').trim().substring(0, 500);
            results.push({
              kind: '文档',
              title: f.title || f.name,
              excerpt: excerpt,
              meta: f.path || '',
              tags: '',
              name: f.name
            });
          });
          return fetchBatch(start + 5);
        });
      }
      return fetchBatch(0);
    }).catch(function(e) {
      console.error('Failed to build search index:', e);
      docSearchIndexBuilding = false;
    });
  }

  function highlightSearch(text, terms) {
    var result = escapeHtml(text || '');
    terms.forEach(function(term) {
      var escaped = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      result = result.replace(new RegExp('(' + escaped + ')', 'gi'), '<span class="global-search-keyword">$1</span>');
    });
    return result;
  }

  function renderSearchResults(query) {
    var resultsEl = document.getElementById('globalSearchResults');
    var countEl = document.getElementById('globalSearchCount');
    if (!resultsEl || !countEl) return;

    if (!docSearchIndexReady) {
      countEl.textContent = 'Loading...';
      resultsEl.innerHTML = '<div class="global-search-empty">正在构建索引...</div>';
      return;
    }

    var terms = String(query || '').trim().toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) {
      countEl.textContent = docSearchIndex.length + ' entries';
      resultsEl.innerHTML = '<div class="global-search-empty">输入关键词搜索说明文档...</div>';
      return;
    }

    var matches = docSearchIndex.filter(function(item) {
      var haystack = (item.title + ' ' + item.excerpt + ' ' + item.meta + ' ' + item.tags).toLowerCase();
      return terms.every(function(term) { return haystack.indexOf(term) !== -1; });
    });

    countEl.textContent = matches.length + ' results';
    if (!matches.length) {
      resultsEl.innerHTML = '<div class="global-search-empty">No results for "' + escapeHtml(query) + '".</div>';
      return;
    }

    resultsEl.innerHTML = matches.map(function(item) {
      return '' +
        '<div class="global-search-item" onclick="window.__openDocFromSearch(\'' + escapeHtml(item.name).replace(/'/g, "\\'") + '\')">' +
          '<div class="global-search-item-meta"><span>' + escapeHtml(item.kind) + '</span><span>' + escapeHtml(item.meta) + '</span></div>' +
          '<div class="global-search-item-title">' + highlightSearch(item.title, terms) + '</div>' +
          '<div class="global-search-item-excerpt">' + highlightSearch(item.excerpt, terms) + '</div>' +
        '</div>';
    }).join('');

    var items = resultsEl.querySelectorAll('.global-search-item');
    items.forEach(function(item, i) {
      item.style.animationDelay = (i * 0.04) + 's';
    });
  }

  var panel = document.getElementById('globalSearchPanel');
  var input = document.getElementById('globalSearchInput');
  var results = document.getElementById('globalSearchResults');
  var count = document.getElementById('globalSearchCount');
  var close = document.getElementById('globalSearchClose');
  var triggerEl = document.getElementById('globalSearchTrigger');

  function openSearch() {
    if (!panel || !input) {
      console.warn('[search] panel or input missing, aborting');
      return;
    }
    panel.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow = 'hidden';
    input.value = '';
    renderSearchResults('');
    setTimeout(function() {
      try { input.focus({ preventScroll: true }); } catch (err) { input.focus(); }
    }, 50);
    buildDocSearchIndex().then(function() {
      renderSearchResults(input.value);
    });
  }

  function closeSearch() {
    if (!panel) return;
    panel.classList.remove('is-open');
    document.documentElement.style.overflow = '';
    document.body.style.overflow = '';
    setTimeout(function() {
      panel.style.backdropFilter = '';
      panel.style.webkitBackdropFilter = '';
      panel.style.background = '';
    }, 350);
  }

  window.openGlobalSearch = openSearch;
  window.closeGlobalSearch = closeSearch;

  window.__openDocFromSearch = function(name) {
    closeSearch();
    renderDocDetail(name);
  };

  if (triggerEl) triggerEl.addEventListener('click', openSearch);
  if (close) close.addEventListener('click', closeSearch);
  if (panel) {
    panel.addEventListener('click', function(event) {
      if (event.target === panel) closeSearch();
    });
  }
  if (input) {
    input.addEventListener('input', function() {
      renderSearchResults(input.value);
    });
  }

  document.addEventListener('keydown', function(event) {
    if (!panel) return;
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault();
      if (panel.classList.contains('is-open')) {
        closeSearch();
      } else {
        openSearch();
      }
      return;
    }
    if (event.key === 'Escape' && panel.classList.contains('is-open')) {
      closeSearch();
      return;
    }
    if (event.key === 'Tab' && panel.classList.contains('is-open')) {
      var focusable = panel.querySelectorAll('input, button, .global-search-item');
      if (focusable.length === 0) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });
})();

// ========================================================================
// Command Dropdown
// ========================================================================

function showCommandDropdown(query) {
  if (!els.commandDropdown) return;
  const filtered = window.filterCommands ? window.filterCommands(query) : [];
  commandDropdownItems = filtered;
  commandDropdownIndex = -1;
  if (filtered.length === 0) {
    els.commandDropdown.innerHTML = '<div class="command-empty">无匹配命令</div>';
  } else {
    let html = '';
    let lastCat = '';
    for (const cmd of filtered) {
      if (cmd.category !== lastCat) {
        lastCat = cmd.category;
        html += `<div class="command-category">${lastCat}</div>`;
      }
      const typeClass = cmd.type === 'prompt' ? 'prompt' : '';
      const typeLabel = cmd.type === 'prompt' ? '技能' : '本地';
      html += `<div class="command-item" data-name="${cmd.name}" onclick="selectCommandItem('${cmd.name}')">
        <span class="command-item-name">${cmd.name}</span>
        <span class="command-item-desc">${cmd.label || cmd.description || ''}</span>
        <span class="command-item-type ${typeClass}">${typeLabel}</span>
      </div>`;
    }
    els.commandDropdown.innerHTML = html;
  }
  els.commandDropdown.classList.remove('hidden');
  commandDropdownVisible = true;
}

function hideCommandDropdown() {
  if (els.commandDropdown) els.commandDropdown.classList.add('hidden');
  commandDropdownVisible = false;
  commandDropdownIndex = -1;
  commandDropdownItems = [];
}

function navigateCommandDropdown(direction) {
  if (!commandDropdownVisible || commandDropdownItems.length === 0) return;
  const items = els.commandDropdown.querySelectorAll('.command-item');
  if (items.length === 0) return;
  items.forEach(i => i.classList.remove('selected'));
  commandDropdownIndex += direction;
  if (commandDropdownIndex < 0) commandDropdownIndex = items.length - 1;
  if (commandDropdownIndex >= items.length) commandDropdownIndex = 0;
  items[commandDropdownIndex].classList.add('selected');
  items[commandDropdownIndex].scrollIntoView({ block: 'nearest' });
}

function selectCurrentCommandItem() {
  if (!commandDropdownVisible || commandDropdownItems.length === 0) return false;
  const idx = commandDropdownIndex >= 0 ? commandDropdownIndex : 0;
  const cmd = commandDropdownItems[idx];
  if (!cmd) return false;
  selectCommandItem(cmd.name);
  return true;
}

function selectCommandItem(name) {
  const cmd = window.findCommand ? window.findCommand(name) : null;
  hideCommandDropdown();
  if (!cmd) return;
  if (cmd.type === 'local') {
    els.chatInput.value = '';
    if (window.executeLocalCommand) window.executeLocalCommand(name);
  } else {
    // Prompt command: insert command name + space into input
    els.chatInput.value = name + ' ';
    els.chatInput.focus();
  }
}

function handleChatInputChange() {
  const text = els.chatInput.value;
  if (text.startsWith('/') && text.indexOf(' ') < 0) {
    showCommandDropdown(text);
  } else if (commandDropdownVisible) {
    hideCommandDropdown();
  }
}

// Attach input listener for command dropdown
document.addEventListener('DOMContentLoaded', () => {
  const chatInput = document.getElementById('chat-input');
  if (chatInput) {
    chatInput.addEventListener('input', handleChatInputChange);
  }
});

function looksLikeFunctionQuery(text) {
  // 匹配 5-6 位纯数字（功能号）或包含"功能号"关键词
  return /\b\d{5,6}\b/.test(text) || /功能号/.test(text);
}

async function sendChat() {
  const text = els.chatInput.value.trim();
  if (!text) return;
  hideCommandDropdown();
  const provider = els.agentProvider.value;
  if (!provider) { showToast('请选择一个模型', 'error'); return; }

  // Handle slash commands
  if (text.startsWith('/')) {
    const spaceIdx = text.indexOf(' ');
    const cmdName = spaceIdx > 0 ? text.substring(0, spaceIdx) : text;
    const cmdArgs = spaceIdx > 0 ? text.substring(spaceIdx + 1).trim() : '';
    const cmd = window.findCommand ? window.findCommand(cmdName) : null;

    if (cmd && cmd.type === 'local') {
      els.chatInput.value = '';
      if (window.executeLocalCommand) window.executeLocalCommand(cmdName);
      return;
    }

    // Prompt command: augment the user message with skill context and run agent loop
    if (cmd && cmd.type === 'prompt') {
      els.chatInput.value = '';
      appendMessage(text, 'user');
      addMessageToHistory('user', text);
      const skillHint = `[Using skill: ${cmd.label || cmd.name}]\n${cmd.description || ''}\n\n`;
      await sendAgentRun(cmdArgs || text, provider, {
        context_mode: 'codebase',
        system_prompt: skillHint + '你是一个代码库智能助手，请基于检索到的证据和上下文回答问题。',
      });
      return;
    }

    // /tool command: call MCP tool directly
    if (cmdName === '/tool') {
      els.chatInput.value = '';
      if (!cmdArgs) {
        showToast('用法: /tool <工具名> [参数JSON]', 'error');
        return;
      }
      const toolSpaceIdx = cmdArgs.indexOf(' ');
      const toolName = toolSpaceIdx > 0 ? cmdArgs.substring(0, toolSpaceIdx) : cmdArgs;
      const toolArgsStr = toolSpaceIdx > 0 ? cmdArgs.substring(toolSpaceIdx + 1).trim() : '{}';
      let toolArgs;
      try {
        toolArgs = JSON.parse(toolArgsStr);
      } catch (_e) {
        toolArgs = { query: toolArgsStr };
      }
      appendMessage(text, 'user');
      addMessageToHistory('user', text);
      try {
        const data = await apiPost('/agent/tool-call', {
          tool_name: toolName,
          arguments: toolArgs
        });
        const resultStr = data.is_error
          ? '❌ ' + (data.result || '工具调用失败')
          : data.result || '无结果';
        const latencyHint = data.latency_ms ? ` (${data.latency_ms}ms)` : '';
        const msg = `🔧 **${toolName}**${latencyHint}\n\`\`\`\n${resultStr}\n\`\`\``;
        const html = await renderMarkdown(msg);
        const div = document.createElement('div');
        div.className = 'chat-message assistant';
        const time = new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' });
        div.innerHTML = html + '<div class="msg-time">' + time + '</div>';
        els.chatTranscript.appendChild(div);
        els.chatTranscript.scrollTop = els.chatTranscript.scrollHeight;
        addMessageToHistory('assistant', msg);
        if (window.SiteUtils && window.SiteUtils.bindCodeBlockInteractions) {
          window.SiteUtils.bindCodeBlockInteractions(div);
        }
      } catch (e) {
        appendMessage('工具调用失败: ' + e.message, 'assistant');
        addMessageToHistory('assistant', '工具调用失败: ' + e.message);
      }
      return;
    }

    // Unknown command — show help
    showToast('未知命令: ' + cmdName + '。输入 /help 查看所有命令', 'error');
    return;
  }

  appendMessage(text, 'user');
  addMessageToHistory('user', text);
  els.chatInput.value = '';

  // All non-command chat goes through the agent loop
  await sendAgentRun(text, provider);
}

// ========================================================================
// Agent Loop — SSE streaming with tool call cards
// ========================================================================

function updateComposerState() {
  const sendBtn = document.getElementById('send-btn');
  const cancelBtn = document.getElementById('cancel-btn');
  if (isAgentRunning) {
    if (sendBtn) sendBtn.disabled = true;
    if (cancelBtn) cancelBtn.classList.remove('hidden');
    if (els.chatInput) els.chatInput.disabled = true;
  } else {
    if (sendBtn) sendBtn.disabled = false;
    if (cancelBtn) cancelBtn.classList.add('hidden');
    if (els.chatInput) {
      // Prevent browser from auto-restoring focus to chatInput when disabled
      // becomes false by moving focus to a temporary trap element first.
      var trap = document.createElement('div');
      trap.tabIndex = -1;
      trap.style.position = 'fixed';
      trap.style.opacity = '0';
      trap.style.pointerEvents = 'none';
      document.body.appendChild(trap);
      trap.focus();

      els.chatInput.disabled = false;

      // Remove trap and ensure chatInput is not focused.
      setTimeout(function() {
        trap.remove();
        if (els.chatInput && document.activeElement === els.chatInput) {
          els.chatInput.blur();
        }
      }, 50);
      // Second check as insurance.
      setTimeout(function() {
        if (els.chatInput && document.activeElement === els.chatInput) {
          els.chatInput.blur();
        }
      }, 250);
    }
  }
}

function cancelAgentRun() {
  if (agentAbortController) agentAbortController.abort();
  isAgentRunning = false;
  updateComposerState();
}

async function sendAgentRun(text, provider, options) {
  agentAbortController = new AbortController();
  isAgentRunning = true;
  toolCallMap = new Map();
  updateComposerState();

  let currentAssistantEl = null;
  let currentTextBuffer = '';

  try {
    const response = await fetch(API_BASE + '/agent/run', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: text,
        provider: provider,
        history: getHistoryForApi(),
        context_mode: (options && options.context_mode) || contextMode,
        system_prompt: options && options.system_prompt,
      }),
      signal: agentAbortController.signal,
    });

    if (!response.ok) {
      const errText = await response.text().catch(() => response.statusText);
      throw new Error(`${response.status}: ${errText}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let sseBuffer = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      sseBuffer += decoder.decode(value, { stream: true });

      const events = parseSSE(sseBuffer);
      sseBuffer = events.remaining;

      for (const event of events.parsed) {
        if (event.type === 'tool_use') {
          renderToolCallCard(event);
        } else if (event.type === 'tool_result') {
          updateToolCallCard(event);
        } else if (event.type === 'thinking') {
          if (!currentAssistantEl) {
            currentAssistantEl = createAssistantMessageEl();
          }
          appendStreamingText(currentAssistantEl, event.content, 'thinking');
        } else if (event.type === 'text') {
          if (!currentAssistantEl) {
            currentAssistantEl = createAssistantMessageEl();
          }
          currentTextBuffer += event.content;
          appendStreamingText(currentAssistantEl, currentTextBuffer, 'text');
        } else if (event.type === 'done') {
          finalizeAssistantMessage(currentAssistantEl, currentTextBuffer);
          isAgentRunning = false;
          agentAbortController = null;
          updateComposerState();
          break;
        } else if (event.type === 'error') {
          appendMessage('Agent 错误: ' + event.message, 'assistant');
          addMessageToHistory('assistant', 'Agent 错误: ' + event.message);
          isAgentRunning = false;
          agentAbortController = null;
          updateComposerState();
          break;
        } else if (event.type === 'tool_confirmation_required') {
          handleToolConfirmation(event);
        }
      }
      if (!isAgentRunning) break;
    }

    // Finalize if done event was missed
    if (currentAssistantEl && currentTextBuffer) {
      finalizeAssistantMessage(currentAssistantEl, currentTextBuffer);
    }
  } catch (e) {
    if (e.name === 'AbortError') {
      appendMessage('[已取消]', 'assistant');
      addMessageToHistory('assistant', '[已取消]');
    } else {
      appendMessage('Agent 运行失败: ' + e.message, 'assistant');
      addMessageToHistory('assistant', 'Agent 运行失败: ' + e.message);
    }
  } finally {
    isAgentRunning = false;
    agentAbortController = null;
    updateComposerState();
  }
}

function parseSSE(buffer) {
  const parsed = [];
  let remaining = buffer;
  const parts = remaining.split('\n\n');
  for (let i = 0; i < parts.length - 1; i++) {
    const block = parts[i].trim();
    if (!block) continue;
    let eventType = 'message';
    let data = '';
    for (const line of block.split('\n')) {
      if (line.startsWith('event: ')) {
        eventType = line.substring(7).trim();
      } else if (line.startsWith('data: ')) {
        data = line.substring(6);
      }
    }
    if (data) {
      try {
        parsed.push({ type: eventType, ...JSON.parse(data) });
      } catch (_e) {
        parsed.push({ type: eventType, data: data });
      }
    }
  }
  remaining = parts[parts.length - 1];
  return { parsed, remaining };
}

function getHistoryForApi() {
  if (!currentChatId) return [];
  const chat = chatHistories.find(c => c.id === currentChatId);
  if (!chat) return [];
  return chat.messages.slice(-12).map(m => ({
    role: m.role === 'user' ? 'user' : 'assistant',
    content: m.text,
  }));
}

function createAssistantMessageEl() {
  const div = document.createElement('div');
  div.className = 'chat-message assistant';
  div.innerHTML = '<div class="assistant-content streaming"></div><div class="msg-time"></div>';
  els.chatTranscript.appendChild(div);
  els.chatTranscript.scrollTop = els.chatTranscript.scrollHeight;
  return div;
}

async function appendStreamingText(el, content, kind) {
  const contentEl = el.querySelector('.assistant-content');
  if (!contentEl) return;
  if (kind === 'thinking') {
    contentEl.innerHTML = '<div class="thinking-text">' + escapeHtml(content) + '</div>';
  } else {
    const html = await renderMarkdown(content);
    contentEl.innerHTML = html;
  }
  contentEl.classList.add('streaming');
  els.chatTranscript.scrollTop = els.chatTranscript.scrollHeight;
}

async function finalizeAssistantMessage(el, text) {
  if (!el) return;
  const contentEl = el.querySelector('.assistant-content');
  if (contentEl) {
    contentEl.classList.remove('streaming');
    if (text) {
      const html = await renderMarkdown(text);
      contentEl.innerHTML = html;
    }
  }
  const timeEl = el.querySelector('.msg-time');
  if (timeEl) {
    timeEl.textContent = new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' });
  }
  if (text) addMessageToHistory('assistant', text);
  if (window.SiteUtils && window.SiteUtils.bindCodeBlockInteractions) {
    window.SiteUtils.bindCodeBlockInteractions(el);
  }
  els.chatTranscript.scrollTop = els.chatTranscript.scrollHeight;
}

function renderToolCallCard(event) {
  const card = document.createElement('div');
  card.className = 'tool-call-card';
  card.id = 'tool-call-' + event.call_id;
  const argsPreview = JSON.stringify(event.arguments, null, 2);
  const truncated = argsPreview.length > 300 ? argsPreview.substring(0, 300) + '...' : argsPreview;
  card.innerHTML =
    '<div class="tool-call-header">' +
      '<span class="tool-call-icon">🔧</span>' +
      '<span class="tool-call-name">' + escapeHtml(event.tool_name) + '</span>' +
      '<span class="tool-call-status pending">⏳</span>' +
    '</div>' +
    '<details class="tool-call-args"><summary>参数</summary><pre>' + escapeHtml(truncated) + '</pre></details>' +
    '<div class="tool-call-result"></div>';
  els.chatTranscript.appendChild(card);
  toolCallMap.set(event.call_id, card);
  els.chatTranscript.scrollTop = els.chatTranscript.scrollHeight;
}

function updateToolCallCard(event) {
  const card = toolCallMap.get(event.call_id);
  if (!card) return;
  const statusEl = card.querySelector('.tool-call-status');
  if (statusEl) {
    statusEl.className = 'tool-call-status ' + (event.is_error ? 'error' : 'done');
    statusEl.textContent = event.is_error ? '❌' : '✅';
  }
  const resultEl = card.querySelector('.tool-call-result');
  if (resultEl) {
    const resultText = event.result || '';
    const display = resultText.length > 500 ? resultText.substring(0, 500) + '...' : resultText;
    resultEl.innerHTML =
      '<details><summary>结果' + (event.latency_ms ? ' (' + event.latency_ms + 'ms)' : '') + '</summary>' +
      '<pre class="tool-result-content">' + escapeHtml(display) + '</pre></details>';
  }
  els.chatTranscript.scrollTop = els.chatTranscript.scrollHeight;
}

// ========================================================================
// Tool Permission Confirmation
// ========================================================================

let pendingConfirmation = null;

function getToolPermissions() {
  try {
    return JSON.parse(localStorage.getItem('uses_indexer_tool_permissions') || '{}');
  } catch (_e) {
    return {};
  }
}

function saveToolPermission(toolName, decision) {
  const perms = getToolPermissions();
  if (decision === 'allow_always') {
    perms[toolName] = 'allow';
  } else {
    delete perms[toolName];
  }
  localStorage.setItem('uses_indexer_tool_permissions', JSON.stringify(perms));
}

function handleToolConfirmation(event) {
  // Check localStorage for auto-allow rules
  const perms = getToolPermissions();
  const autoRule = perms[event.tool_name];
  if (autoRule === 'allow') {
    // Auto-confirm without showing dialog
    apiPost('/agent/tool-confirm', {
      call_id: event.call_id,
      decision: 'allow',
      tool_name: event.tool_name,
    }).catch(() => {});
    return;
  }

  // Show the dialog
  pendingConfirmation = event;
  const dialog = document.getElementById('permission-dialog');
  const nameEl = document.getElementById('perm-tool-name');
  const argsEl = document.getElementById('perm-tool-args');
  if (dialog) dialog.classList.remove('hidden');
  if (nameEl) nameEl.textContent = event.tool_name;
  if (argsEl) {
    const argsStr = JSON.stringify(event.arguments, null, 2);
    argsEl.textContent = argsStr.length > 400 ? argsStr.substring(0, 400) + '...' : argsStr;
  }
}

async function resolvePermission(decision) {
  if (!pendingConfirmation) return;
  const event = pendingConfirmation;
  pendingConfirmation = null;

  const dialog = document.getElementById('permission-dialog');
  if (dialog) dialog.classList.add('hidden');

  if (decision === 'allow_always') {
    saveToolPermission(event.tool_name, 'allow_always');
  }

  try {
    await apiPost('/agent/tool-confirm', {
      call_id: event.call_id,
      decision: decision,
      tool_name: event.tool_name,
    });
  } catch (_e) {
    showToast('确认请求发送失败', 'error');
  }
}

// ========================================================================
// MCP Server Management
// ========================================================================

async function loadMcpServers() {
  try {
    const data = await apiGet('/agent/mcp/servers');
    renderMcpServerList(data.servers || []);
  } catch (_e) {
    renderMcpServerList([]);
  }
}

function renderMcpServerList(servers) {
  const container = document.getElementById('mcp-server-list');
  if (!container) return;
  if (!servers.length) {
    container.innerHTML = '<span class="sidebar-hint">暂无外部服务器</span>';
    return;
  }
  container.innerHTML = servers.map(s => {
    const statusColors = { connected: '#4ade80', disconnected: '#94a3b8', error: '#f87171', connecting: '#fbbf24' };
    const dot = statusColors[s.status] || '#94a3b8';
    return '<div class="mcp-server-item" data-name="' + escapeHtml(s.name) + '">' +
      '<span class="mcp-server-dot" style="background:' + dot + '"></span>' +
      '<span class="mcp-server-name">' + escapeHtml(s.name) + '</span>' +
      '<span class="mcp-server-info">' + s.tool_count + ' 工具</span>' +
      '<button class="mcp-server-action" onclick="disconnectMcpServer(\'' + escapeHtml(s.name) + '\')" title="断开">✕</button>' +
    '</div>';
  }).join('');
}

function showMcpConnectDialog() {
  const dialog = document.getElementById('mcp-connect-dialog');
  if (dialog) dialog.classList.remove('hidden');
}

function hideMcpConnectDialog() {
  const dialog = document.getElementById('mcp-connect-dialog');
  if (dialog) dialog.classList.add('hidden');
}

function toggleMcpTransportFields() {
  const transport = document.getElementById('mcp-transport').value;
  const stdioFields = document.getElementById('mcp-stdio-fields');
  const sseFields = document.getElementById('mcp-sse-fields');
  if (stdioFields) stdioFields.classList.toggle('hidden', transport !== 'stdio');
  if (sseFields) sseFields.classList.toggle('hidden', transport !== 'sse');
}

async function submitMcpConnect() {
  const name = document.getElementById('mcp-name').value.trim();
  const transport = document.getElementById('mcp-transport').value;
  if (!name) { showToast('请输入服务器名称', 'error'); return; }

  const payload = { name, transport };
  if (transport === 'stdio') {
    payload.command = document.getElementById('mcp-command').value.trim();
    const argsStr = document.getElementById('mcp-args').value.trim();
    if (argsStr) {
      try { payload.args = JSON.parse(argsStr); } catch (_e) { payload.args = argsStr.split(/\s+/); }
    }
  } else {
    payload.url = document.getElementById('mcp-url').value.trim();
    if (!payload.url) { showToast('请输入 URL', 'error'); return; }
  }

  hideMcpConnectDialog();
  showToast('正在连接 ' + name + '...', 'info');
  try {
    await apiPost('/agent/mcp/connect', payload);
    showToast(name + ' 已连接', 'success');
    loadMcpServers();
    loadMcpTools();
  } catch (e) {
    showToast('连接失败: ' + e.message, 'error');
  }
}

async function disconnectMcpServer(name) {
  try {
    await apiPost('/agent/mcp/disconnect', { name });
    showToast(name + ' 已断开', 'success');
    loadMcpServers();
    loadMcpTools();
  } catch (e) {
    showToast('断开失败: ' + e.message, 'error');
  }
}

// ========================================================================
// System
// ========================================================================

function refreshSystem() {
  loadDbSummary();
  checkHealth();
  showToast('系统概览已刷新');
}

// ========================================================================
// Keyboard shortcuts
// ========================================================================

document.addEventListener('keydown', (e) => {
  // Command dropdown navigation when visible
  if (commandDropdownVisible && document.activeElement === els.chatInput) {
    if (e.key === 'ArrowDown') { e.preventDefault(); navigateCommandDropdown(1); return; }
    if (e.key === 'ArrowUp') { e.preventDefault(); navigateCommandDropdown(-1); return; }
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); selectCurrentCommandItem(); return; }
    if (e.key === 'Escape') { e.preventDefault(); hideCommandDropdown(); return; }
    if (e.key === 'Tab') {
      e.preventDefault();
      if (commandDropdownItems.length === 1) selectCurrentCommandItem();
      else navigateCommandDropdown(1);
      return;
    }
  }

  // Ctrl/Cmd + Enter in search textarea -> run all
  if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
    if (document.activeElement === els.question) {
      e.preventDefault();
      runAll();
    }
  }
  // Enter in chat textarea -> send (only when dropdown not visible)
  if (e.key === 'Enter' && !e.shiftKey) {
    if (document.activeElement === els.chatInput && !commandDropdownVisible) {
      e.preventDefault();
      sendChat();
    }
  }
});

// ========================================================================
// Docs
// ========================================================================

let docFiles = [];
let docPage = 1;
const docPageSize = 8;

async function loadDocs() {
  try {
    const data = await apiGet('/docs');
    docFiles = data.files || [];
    docPage = 1;
    renderDocsList();
  } catch (e) {
    showToast('加载文档列表失败: ' + e.message, 'error');
    els.docsList.innerHTML = '<div class="empty-state">无法加载文档列表</div>';
  }
}

function renderDocsList() {
  if (!docFiles.length) {
    els.docsList.innerHTML = '<div class="empty-state">暂无文档</div>';
    els.docsPagination.innerHTML = '';
    return;
  }
  const total = docFiles.length;
  const totalPages = Math.max(1, Math.ceil(total / docPageSize));
  if (docPage > totalPages) docPage = totalPages;
  const start = (docPage - 1) * docPageSize;
  const pageFiles = docFiles.slice(start, start + docPageSize);

  els.docsList.innerHTML = pageFiles.map((f, i) => `
    <div class="doc-item" onclick="renderDocDetail('${escapeHtml(f.name)}')" style="animation-delay:${i * 0.05}s">
      <div class="doc-meta">
        <span class="doc-category">文档</span>
        <span class="doc-date">${escapeHtml(f.path)}</span>
      </div>
      <h3 class="doc-title">${escapeHtml(f.title)}</h3>
      <p class="doc-excerpt">${escapeHtml(f.name)}</p>
    </div>
  `).join('');
  requestAnimationFrame(function() { window.SiteUtils.installDockEffect(els.docsList); });

  // pagination with jump input
  const hasPrev = docPage > 1;
  const hasNext = docPage < totalPages;
  els.docsPagination.innerHTML = `
    <button class="pagination-btn" ${hasPrev ? '' : 'disabled'} onclick="changeDocPage(-1)">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
      上一页
    </button>
    <div class="pagination-jump">
      <input type="number" class="pagination-input" id="pageInput" value="${docPage}" min="1" max="${totalPages}" oninput="onPageInput()" onkeydown="if(event.key==='Enter'){changeDocPage('jump');}">
      <span class="pagination-total">/ ${totalPages}</span>
    </div>
    <button class="pagination-btn" id="pageNextBtn" ${hasNext ? '' : 'disabled'} onclick="changeDocPage(1)">
      <span id="pageNextText">下一页</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
    </button>
  `;
}

function changeDocPage(delta) {
  const totalPages = Math.max(1, Math.ceil(docFiles.length / docPageSize));
  var newPage;
  if (delta === 'jump') {
    var input = document.getElementById('pageInput');
    newPage = parseInt(input ? input.value : docPage, 10);
    if (isNaN(newPage)) newPage = docPage;
  } else {
    newPage = docPage + delta;
  }
  if (newPage >= 1 && newPage <= totalPages) {
    docPage = newPage;
    renderDocsList();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function onPageInput() {
  var input = document.getElementById('pageInput');
  var btn = document.getElementById('pageNextBtn');
  var text = document.getElementById('pageNextText');
  if (!input || !btn || !text) return;
  var val = parseInt(input.value, 10);
  var totalPages = Math.max(1, Math.ceil(docFiles.length / docPageSize));
  if (isNaN(val)) val = docPage;
  if (val !== docPage) {
    text.textContent = '跳转';
    btn.disabled = false;
    btn.setAttribute('onclick', "changeDocPage('jump')");
  } else {
    text.textContent = '下一页';
    btn.disabled = !(docPage < totalPages);
    btn.setAttribute('onclick', 'changeDocPage(1)');
  }
}

async function renderDocDetail(name) {
  try {
    const data = await apiGet('/docs/' + encodeURIComponent(name));
    els.docDetailTitle.textContent = data.title || data.name;
    els.docDetailEyebrow.textContent = data.name;
    const html = await renderMarkdown(data.content || '');
    els.docDetailBody.innerHTML = html;
    delete els.docDetailBody.__codeBlockBound;
    window.SiteUtils.bindCodeBlockInteractions(els.docDetailBody);
    setView('doc-detail');
  } catch (e) {
    showToast('加载文档失败: ' + e.message, 'error');
  }
}

function backToDocs() {
  setView('docs');
}



// ========================================================================
// Expose globals for HTML onclick handlers
// ========================================================================
window.setView = setView;
window.toggleSettings = toggleSettings;
window.onBgModeClick = onBgModeClick;
window.onBgUpload = onBgUpload;
window.runAll = runAll;
window.runQuery = runQuery;
window.runEvidence = runEvidence;
window.runAnswer = runAnswer;
window.runBundle = runBundle;
window.switchTab = switchTab;
window.sendChat = sendChat;
window.clearChat = clearChat;
window.loadProviders = loadProviders;
window.showCommandHelp = function() {
  const cmds = window.getCommandRegistry ? window.getCommandRegistry() : [];
  if (cmds.length === 0) {
    showToast('暂无可用命令', 'info');
    return;
  }
  const lines = cmds.map(c => `  ${c.name.padEnd(30)} ${c.label || c.description || ''}`);
  appendMessage('可用命令:\n```\n' + lines.join('\n') + '\n```', 'assistant');
};
window.selectCommandItem = selectCommandItem;
window.setContextMode = setContextMode;
window.cancelAgentRun = cancelAgentRun;
window.createNewChat = createNewChat;
window.loadChat = loadChat;
window.renameChat = renameChat;
window.cancelRename = cancelRename;
window.deleteChat = deleteChat;
window.triggerFileUpload = triggerFileUpload;
window.onFileSelected = onFileSelected;
window.removeAttachment = removeAttachment;

window.refreshSystem = refreshSystem;
window.renderDocDetail = renderDocDetail;
window.backToDocs = backToDocs;
window.changeDocPage = changeDocPage;
window.onPageInput = onPageInput;

// ========================================================================
// Init
// ========================================================================

document.addEventListener('DOMContentLoaded', () => {
  initRefs();
  setView('search');
  checkHealth();
  loadDbSummary();
  loadProviders();
  initChatHistory();
  if (window.loadCommands) window.loadCommands();
  loadMcpTools();
  loadMcpServers();

  // Nav scroll detection — 照搬博客
  const navbar = document.getElementById('navbar');
  if (navbar) {
    function onScroll() {
      navbar.classList.toggle('scrolled', window.scrollY > 20);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Periodic health check
  setInterval(checkHealth, 15000);
});

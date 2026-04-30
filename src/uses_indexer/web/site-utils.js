window.SiteUtils = {
  installDockEffect: installDockEffect,
  bindCodeBlockInteractions: bindCodeBlockInteractions
};

function installDockEffect(rootSelector) {
  var root = typeof rootSelector === 'string' ? document.querySelector(rootSelector) : (rootSelector || document.body);
  if (!root) return;

  var MAX_SCALE = 1.11;
  var SIGMA_Y = 120;
  var SIGMA_X = 220;
  var items = [];
  var rects = [];

  function refreshItems() {
    items = Array.from(root.querySelectorAll('.project-item, .writing-item, .resource-card, .doc-item'));
  }

  function cacheRects() {
    refreshItems();
    rects = [];
    for (var i = 0; i < items.length; i++) {
      rects.push(items[i].getBoundingClientRect());
    }
  }

  function applyDock(cx, cy) {
    for (var i = 0; i < items.length; i++) {
      var rect = rects[i];
      if (!rect) continue;
      var scale = 1;
      var centerX = rect.left + rect.width / 2;
      var centerY = rect.top + rect.height / 2;
      var distX = cx - centerX;
      var distY = cy - centerY;
      var influenceX = Math.exp(-(distX * distX) / (2 * SIGMA_X * SIGMA_X));
      var influenceY = Math.exp(-(distY * distY) / (2 * SIGMA_Y * SIGMA_Y));
      var influence = influenceX * influenceY;

      scale = 1 + (MAX_SCALE - 1) * influence;

      items[i].style.transform = 'scale(' + scale + ')';

      if (scale > 1.01) {
        items[i].classList.add('dock-active');
      } else {
        items[i].classList.remove('dock-active');
      }
    }
  }

  function resetDock() {
    for (var i = 0; i < items.length; i++) {
      items[i].style.transform = 'scale(1)';
      items[i].classList.remove('dock-active');
    }
  }

  if (!root.__dockEffectInstalled) {
    root.__dockEffectInstalled = true;
    root.addEventListener('pointerenter', function() {
      cacheRects();
    });
    root.addEventListener('pointermove', function(e) {
      applyDock(e.clientX, e.clientY);
    });
    root.addEventListener('pointerleave', function() {
      resetDock();
    });

    window.addEventListener('scroll', cacheRects, { passive: true });
    window.addEventListener('resize', cacheRects, { passive: true });
  }

  cacheRects();
}

function bindCodeBlockInteractions(container) {
  if (!container || container.__codeBlockBound) return;
  container.__codeBlockBound = true;

  // Per-block gutter width: each block gets its own width based on line count
  function getGutterWidth(count) {
    // 0.85em monospace: each digit ≈ 8px, plus 10px total padding (5px each side)
    if (count >= 1000) return '42px';
    if (count >= 100) return '34px';
    if (count >= 10) return '26px';
    return '18px';
  }
  var figures = container.querySelectorAll("figure.highlight");
  figures.forEach(function(item) {
    var count = parseInt(item.getAttribute('data-line-count'), 10);
    var gutter = item.querySelector('.gutter');
    if (gutter) {
      var w = getGutterWidth(count);
      gutter.style.width = w;
      gutter.style.minWidth = w;
      gutter.style.maxWidth = w;
    }
  });

  // Event delegation for copy / expand / fold
  container.addEventListener("click", function(e) {
    var target = e.target;
    var toolbar = target.closest(".highlight-tools");

    var expandBtn = target.closest(".expand");
    if (expandBtn && toolbar) {
      toolbar.classList.toggle("closed");
      return;
    }

    var copyBtn = target.closest(".copy-button");
    if (copyBtn && toolbar) {
      var figure = toolbar.parentNode;
      if (!figure) return;
      var codePre = figure.querySelector("td.code pre code");
      if (!codePre) return;
      var text = codePre.textContent || codePre.innerText || "";

      function alertInfo(textMsg) {
        var notice = toolbar.querySelector('.copy-notice');
        if (notice) {
          notice.textContent = textMsg;
          notice.style.opacity = 1;
          setTimeout(function() { notice.style.opacity = 0; }, 800);
        }
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function() {
          alertInfo("Copied!");
        }, function() {
          alertInfo("Copy failed");
        });
      } else {
        var textarea = document.createElement("textarea");
        textarea.value = text;
        textarea.style.cssText = "position:fixed;left:-9999px;";
        document.body.appendChild(textarea);
        textarea.select();
        try {
          document.execCommand("copy");
          alertInfo("Copied!");
        } catch (err) {
          alertInfo("Copy failed");
        }
        document.body.removeChild(textarea);
      }
      return;
    }

    var codeExpandBtn = target.closest(".code-expand-btn");
    if (codeExpandBtn) {
      var figure = codeExpandBtn.closest("figure.highlight");
      if (figure) {
        figure.classList.toggle("is-collapsed");
        codeExpandBtn.classList.toggle("expand-done");
      }
      return;
    }
  });

  // Add expand buttons for code blocks with more than 15 lines
  container.querySelectorAll("figure.highlight").forEach(function(item) {
    if (item.querySelector(".code-expand-btn")) return;
    var lineCount = item.querySelectorAll('.gutter .line').length;
    if (lineCount > 15) {
      item.classList.add('is-collapsed');
      var btn = document.createElement("div");
      btn.className = "code-expand-btn";
      btn.innerHTML = '<i>&#9662;</i>';
      item.appendChild(btn);
    }
  });
}

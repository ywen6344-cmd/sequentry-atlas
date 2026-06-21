/* 序引海图 · 事件追踪层 ———————————————————————
   命脉指标：外链点击（哪个工具/分类真被点）+ 海图→官网 跨属性导流。
   「谁在就报给谁」：页面加载了 Umami 就报 Umami，加载了 Clarity 就报 Clarity，
   两个都在就都报；都没有则静默降级。→ 工具选型与埋点解耦，换/加工具不用重写。
   海图所有外链统一为 <a target="_blank">，用事件委托一处全抓，
   不需要逐条改 links.js / build_pages.js 的渲染。 */
(function () {
  function track(name, data) {
    // Umami：原生支持事件 + 结构化属性
    try {
      if (window.umami && typeof window.umami.track === 'function') {
        window.umami.track(name, data);
      }
    } catch (e) { /* 静默 */ }
    // Microsoft Clarity：event 触发自定义事件（不占 20 个 Smart Event 上限），
    // set 打标签，便于在录制/热力图里按 域名/名称 筛选回放。
    try {
      if (typeof window.clarity === 'function') {
        window.clarity('event', name);
        if (data && data.domain) window.clarity('set', name + '_domain', String(data.domain));
        if (data && data.label)  window.clarity('set', name + '_label', String(data.label).slice(0, 200));
      }
    } catch (e) { /* 静默 */ }
  }

  // 取卡片主名（result/ai-card 等都有 <strong>名称</strong>），否则退回纯文本
  function labelOf(a) {
    var s = a.querySelector && a.querySelector('strong');
    var t = (s ? s.textContent : a.textContent) || '';
    return t.trim().replace(/\s+/g, ' ').slice(0, 80);
  }

  function onClick(e) {
    var t = e.target;
    if (!t || !t.closest) return;
    var a = t.closest('a[target="_blank"]');
    if (!a) return;
    var href = a.getAttribute('href') || a.getAttribute('data-url') || '';
    if (!/^https?:\/\//i.test(href)) return;
    var domain = '';
    try { domain = new URL(href, location.href).hostname.replace(/^www\./, ''); } catch (_) {}
    var isSelf = /(^|\.)sequentry\.com$/i.test(domain);
    track('outbound', {
      domain: domain,
      label: labelOf(a),
      url: href.slice(0, 200),
      kind: isSelf ? 'to-sequentry' : 'external'   // 区分「导向官网」与「导向外部工具」
    });
  }

  // click 抓左键；auxclick 抓中键/新标签打开。capture 阶段确保 _blank 跳转前先记录。
  document.addEventListener('click', onClick, true);
  document.addEventListener('auxclick', onClick, true);
})();

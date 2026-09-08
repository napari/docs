// napari-search-widget.js
//
// Drop-in replacement for a site's native search box. Mounts Pagefind's
// stock UI against this site's own Pagefind bundle, and merges in the
// Pagefind bundles of sibling napari.org sub-sites so results span all of
// them from one search box.
//
// Usage (append to a page, once at least one element matching data-mount
// exists and a Pagefind bundle already exists for this site):
//
//   <div class="napari-search"></div>
//   <script
//     src="/_static/napari-search-widget.js"
//     data-bundle-path="/dev/pagefind/"
//     data-merge-paths="/workshops/pagefind/,/island-dispatch/pagefind/"
//     data-mount=".napari-search"
//     defer
//   ></script>
//
// - data-bundle-path: root-relative path to *this* page's own Pagefind
//   bundle directory (the folder containing pagefind-ui.js). Required.
// - data-merge-paths: comma-separated root-relative paths to sibling
//   sites' Pagefind bundle directories to merge into results. Optional.
// - data-mount: CSS selector matching every element to mount a search UI
//   into. Defaults to ".napari-search". Some themes render their navbar
//   more than once per page (e.g. a desktop and a mobile variant), and
//   this script tag may itself be included more than once as a result —
//   every match gets its own independent PagefindUI instance, and each
//   match/script pair is only ever initialized once.

(function () {
  const thisScript = document.currentScript;
  const bundlePath = thisScript.dataset.bundlePath;
  const mergePaths = (thisScript.dataset.mergePaths || '')
    .split(',')
    .map((s) => s.trim())
    .filter(Boolean);
  const mountSelector = thisScript.dataset.mount || '.napari-search';
  // Directory this very <script> was loaded from — used to find its
  // sibling CSS file without assuming any particular site layout/prefix.
  const ownDir = new URL('.', thisScript.src).href;

  if (!bundlePath) {
    console.error('napari-search-widget: data-bundle-path is required');
    return;
  }

  function loadStylesheet(href) {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = href;
    document.head.appendChild(link);
  }

  // Cached across multiple script instances on the same page, so the
  // pagefind-ui bundle is only ever fetched once.
  function loadPagefindUiOnce() {
    if (!window.__napariSearchPagefindUiPromise) {
      loadStylesheet(`${ownDir}napari-search-widget.css`);
      loadStylesheet(`${bundlePath}pagefind-ui.css`);
      window.__napariSearchPagefindUiPromise = new Promise((resolve, reject) => {
        const s = document.createElement('script');
        s.src = `${bundlePath}pagefind-ui.js`;
        s.onload = resolve;
        s.onerror = () => reject(new Error(`Failed to load ${s.src}`));
        document.head.appendChild(s);
      });
    }
    return window.__napariSearchPagefindUiPromise;
  }

  loadPagefindUiOnce().then(() => {
    const mounts = document.querySelectorAll(mountSelector);
    if (!mounts.length) {
      console.error(`napari-search-widget: no element matches ${mountSelector}`);
      return;
    }
    mounts.forEach((mount) => {
      if (mount.dataset.napariSearchMounted) return;
      mount.dataset.napariSearchMounted = 'true';
      new PagefindUI({
        element: mount,
        showSubResults: true,
        showImages: false,
        excerptLength: 15,
        mergeIndex: mergePaths.map((path) => ({ bundlePath: path })),
      });
    });
  });
})();

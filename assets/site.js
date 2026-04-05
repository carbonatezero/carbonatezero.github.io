const siteName = "carbonatezero";

const navItems = [
  { id: "home", href: "/", label: "Home" },
  { id: "about", href: "/about.html", label: "About" },
  { id: "teaching", href: "/teaching.html", label: "Teaching" },
  { id: "projects", href: "/projects.html", label: "Projects" },
  { id: "notes", href: "/notes.html", label: "Notes" },
];

function renderNav(activePage) {
  const links = navItems
    .map(({ id, href, label }) => {
      const current = id === activePage ? ' aria-current="page"' : "";
      return `<a class="global-nav-link" href="${href}"${current}>${label}</a>`;
    })
    .join("");

  return `
    <nav class="global-nav" aria-label="Global site navigation">
      <div class="global-nav-inner">${links}</div>
    </nav>
  `.trim();
}

function renderFooter() {
  const year = new Date().getFullYear();
  return `
    <footer class="site-footer">
      <div class="site-footer-inner">
        <p class="small">&copy; ${year} ${siteName}. All rights reserved.</p>
      </div>
    </footer>
  `.trim();
}

function renderSiteChrome() {
  const activePage = document.body.dataset.page || "";
  const navMount = document.querySelector("[data-site-nav]");
  const footerMount = document.querySelector("[data-site-footer]");

  if (navMount) {
    navMount.outerHTML = renderNav(activePage);
  }

  if (footerMount) {
    footerMount.outerHTML = renderFooter();
  }
}

renderSiteChrome();

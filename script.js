const menuItems = [
  // Special Snacks
  {
    id: 'khaman',
    name: 'Khaman',
    category: 'snacks',
    description: 'Soft, spongy and light. Steamed besan with mustard seeds, curry leaves and green chilli.',
    price: 85,
    unit: '250 gms',
    image: 'images/khaman.jpeg',
    veg: true,
    popular: true
  },
  {
    id: 'white-dhokla',
    name: 'White Dhokla',
    category: 'snacks',
    description: 'Soft white dhokla made from rice and dal. Light on the stomach, with black pepper and coriander.',
    price: 85,
    unit: '250 gms',
    image: 'images/white_dhokla.jpeg',
    veg: true
  },
  {
    id: 'khaman-sev',
    name: 'Khaman & Sev',
    category: 'snacks',
    description: 'Our soft khaman with a thick layer of crunchy nylon sev on top.',
    price: 95,
    unit: '250 gms',
    image: 'images/khaman_sev.webp',
    veg: true
  },
  {
    id: 'sev-khamni',
    name: 'Sev Khamni',
    category: 'snacks',
    description: 'Crumbled khaman mixed with garlic, green chilli and masala. Topped with pomegranate and sev.',
    price: 105,
    unit: '250 gms',
    image: 'images/sev_khamni.jpeg',
    veg: true,
    popular: true
  },
  {
    id: 'khandvi',
    name: 'Khandvi',
    category: 'snacks',
    description: 'Soft besan rolls with a light buttermilk tang, topped with coconut and mustard seeds.',
    price: 100,
    unit: '250 gms',
    image: 'images/khandvi.jpeg',
    veg: true
  },
  {
    id: 'punjabi-samosa',
    name: 'Mini Punjabi Samosa',
    category: 'snacks',
    description: 'Small crispy samosas filled with spiced potato and green peas.',
    price: 90,
    unit: '250 gms',
    image: 'images/punjabi_samosa.jpeg',
    veg: true
  },
  {
    id: 'chinese-samosa',
    name: 'Chinese Samosa',
    category: 'snacks',
    description: 'Crispy samosas filled with spicy noodles and veggies. Kids love these.',
    price: 110,
    unit: '250 gms',
    image: 'images/chinese_samosa.jpeg',
    veg: true
  },
  {
    id: 'coconut-patties',
    name: 'Coconut Patties',
    category: 'snacks',
    description: 'Golden potato patties stuffed with sweet coconut, raisins and herbs.',
    price: 120,
    unit: '250 gms',
    image: 'images/coconut_petis.jpeg',
    veg: true
  },
  {
    id: 'farali-peties',
    name: 'Farali Peties (Upvas)',
    category: 'snacks',
    description: 'Upvas special. Potato balls stuffed with coconut, cashew and raisins.',
    price: 120,
    unit: '250 gms',
    image: 'images/farali_petis.jpeg',
    veg: true
  },
  {
    id: 'sabudana-vada',
    name: 'Sabudana Vada (Farali)',
    category: 'snacks',
    description: 'Crispy sabudana and potato vada with peanuts and cumin. Comes with green chutney.',
    price: 120,
    unit: 'Plate',
    image: 'images/farali_sabudana_wada.jpeg',
    veg: true,
    popular: true
  },

  // Farsan (Dry Snacks)
  {
    id: 'jada-gathiya',
    name: 'Jada Gathiya',
    category: 'farsan',
    description: 'Thick, crunchy besan gathiya. Best with hot tea or pickle.',
    price: 120,
    unit: '250 gms',
    image: 'images/jada_gathiya.jpeg',
    veg: true
  },
  {
    id: 'bhavnagri-gathiya',
    name: 'Bhavnagri Gathiya',
    category: 'farsan',
    description: 'Light, soft gathiya in Bhavnagar style. Mild, not spicy.',
    price: 120,
    unit: '250 gms',
    image: 'images/bhavnagri_gathiya.jpeg',
    veg: true
  },
  {
    id: 'tikha-gathiya',
    name: 'Tikha Gathiya',
    category: 'farsan',
    description: 'Crispy gathiya with red chilli and masala. For those who like it spicy.',
    price: 120,
    unit: '250 gms',
    image: 'images/tikha_gathiya.jpeg',
    veg: true
  },
  // {
  //   id: 'tikhi-sev',
  //   name: 'Tikhi Sev',
  //   category: 'farsan',
  //   description: 'Fine, crispy sev with garlic and red chilli. Nice and hot.',
  //   price: 90,
  //   unit: '250 gms',
  //   image: 'images/nylon_sev.webp',
  //   veg: true
  // },
  {
    id: 'jada-sev',
    name: 'Jadi Sev',
    category: 'farsan',
    description: 'Thick sev with black pepper and ajwain.',
    price: 120,
    unit: '250 gms',
    image: 'images/jadi_sev.jpeg',
    veg: true
  },
  {
    id: 'nylon-sev',
    name: 'Nylon Sev',
    category: 'farsan',
    description: 'Very fine, crispy golden sev. Eat as is or sprinkle on anything.',
    price: 50,
    unit: '100 gms',
    image: 'images/nylon_sev.jpeg',
    veg: true
  },
  // {
  //   id: 'nylon-sev-large',
  //   name: 'Nylon Sev (Big Pack)',
  //   category: 'farsan',
  //   description: 'Our fine nylon sev in a bigger family pack.',
  //   price: 120,
  //   unit: '250 gms',
  //   image: 'images/nylon_sev_large.webp',
  //   veg: true
  // },
  {
    id: 'wheat-chakri',
    name: 'Wheat Chakri',
    category: 'farsan',
    description: 'Crunchy wheat chakri with sesame and spices.',
    price: 120,
    unit: '250 gms',
    image: 'images/chakri.jpeg',
    veg: true
  },
  {
    id: 'dry-kachori',
    name: 'Dry Kachori',
    category: 'farsan',
    description: 'Small flaky kachoris filled with sweet-spicy dal and dry fruit.',
    price: 120,
    unit: '250 gms',
    image: 'images/dry_kachori.jpeg',
    veg: true
  },
  {
    id: 'mini-bhakharwadi',
    name: 'Mini Bhakharwadi',
    category: 'farsan',
    description: 'Small bite-size bhakharwadi with sweet-spicy coconut and sesame masala.',
    price: 240,
    unit: '500 gms',
    image: 'images/mini_bhakharwadi.webp',
    veg: true
  },
  {
    id: 'big-bhakharwadi',
    name: 'Big Bhakharwadi',
    category: 'farsan',
    description: 'Big, crispy bhakharwadi rolls with roasted sweet-spicy masala inside.',
    price: 240,
    unit: '500 gms',
    image: 'images/big_bhakharwadi.webp',
    veg: true
  },
  {
    id: 'sing-bhujiya',
    name: 'Sing Bhujiya',
    category: 'farsan',
    description: 'Crunchy masala-coated peanuts. Perfect with a glass of lassi.',
    price: 120,
    unit: '250 gms',
    image: 'images/shing_bhujia.jpeg',
    veg: true
  },
  {
    id: 'makai-chewda',
    name: 'Makai Chewda',
    category: 'farsan',
    description: 'Sweet and salty cornflake mix with peanuts, cashew, raisins and curry leaves.',
    price: 120,
    unit: '250 gms',
    image: 'images/makai_chevdo.jpeg',
    veg: true
  },

  // Lassi & Drinks
  {
    id: 'punjabi-lassi',
    name: 'Punjabi Lassi',
    category: 'drinks',
    description: 'Thick, chilled sweet lassi with a layer of fresh malai on top.',
    price: 60,
    unit: '200 ml',
    image: 'images/punjabi_lassi.jpeg',
    veg: true,
    popular: true
  },
  {
    id: 'mango-lassi',
    name: 'Mango Lassi',
    category: 'drinks',
    description: 'Thick sweet lassi blended with Alphonso mango.',
    price: 70,
    unit: '200 ml',
    image: 'images/mango_lassi.jpeg',
    veg: true,
    popular: true
  },
  {
    id: 'buttermilk',
    name: 'Masala Chhas (Buttermilk)',
    category: 'drinks',
    description: 'Light masala buttermilk with green chilli, ginger, cumin and coriander.',
    price: 50,
    unit: '650 ml',
    image: 'images/buttermilk.jpeg',
    veg: true
  }
];

/* ==========================================================================
   PAGE BEHAVIOUR
   The page is one continuous read, so the chrome (header tone, step rail,
   progress bar) follows whichever step the reader is currently in.
   ========================================================================== */

const SECTION_IDS = ['top', 'promise', 'craft', 'counter', 'menu', 'nasto', 'corporate', 'newshop', 'heritage', 'visit'];

const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* -------------------------------------------------------------------------
   Menu rendering
   ------------------------------------------------------------------------- */
function renderMenu(itemsToRender) {
  const menuGrid = document.getElementById('menu-grid');
  if (!menuGrid) return;
  menuGrid.innerHTML = '';

  if (itemsToRender.length === 0) {
    menuGrid.innerHTML = `
      <div class="no-results">
        <i class="fas fa-search"></i>
        <p>Nothing matched that. Try another name, or tap "All Items".</p>
      </div>
    `;
    return;
  }

  itemsToRender.forEach(item => {
    const card = document.createElement('div');
    card.className = `menu-card ${item.popular ? 'popular-card' : ''}`;
    card.setAttribute('data-id', item.id);

    card.innerHTML = `
      ${item.popular ? '<span class="badge-popular">Most Loved</span>' : ''}
      <div class="card-img-wrapper">
        <img class="lazy-load" src="${item.image}" alt="${item.name}" loading="lazy">
        <div class="veg-indicator">
          <span class="veg-box"><span class="veg-dot"></span></span>
        </div>
      </div>
      <div class="card-info">
        <div class="card-header-row">
          <h3 class="item-title">${item.name}</h3>
        </div>
        <p class="item-desc">${item.description}</p>
      </div>
    `;
    menuGrid.appendChild(card);
  });
}

/* Step 02 — the three plates that leave the counter first. */
function renderSignatures() {
  const grid = document.getElementById('signature-grid');
  if (!grid) return;

  const picks = [
    { id: 'khaman', flag: 'Made fresh daily' },
    { id: 'sev-khamni', flag: 'Spicy favourite' },
    { id: 'punjabi-lassi', flag: 'Made to order' }
  ];

  grid.innerHTML = picks.map(pick => {
    const item = menuItems.find(m => m.id === pick.id);
    if (!item) return '';
    return `
      <article class="sig-card reveal">
        <div class="sig-img">
          <span class="sig-flag">${pick.flag}</span>
          <img src="${item.image}" alt="${item.name}" loading="lazy">
        </div>
        <div class="sig-body">
          <h3>${item.name}</h3>
          <p>${item.description}</p>
        </div>
      </article>
    `;
  }).join('');
}

/* Step 04 — a sample off the Suko Nasto shelf. */
function renderNastoStrip() {
  const strip = document.getElementById('nasto-strip');
  if (!strip) return;

  const picks = ['jada-gathiya', 'mini-bhakharwadi', 'wheat-chakri', 'makai-chewda'];

  strip.innerHTML = picks.map(id => {
    const item = menuItems.find(m => m.id === id);
    if (!item) return '';
    return `
      <div class="nasto-card reveal">
        <img src="${item.image}" alt="${item.name}" loading="lazy">
        <span>${item.name}</span>
      </div>
    `;
  }).join('');
}

/* -------------------------------------------------------------------------
   Menu filtering & search
   ------------------------------------------------------------------------- */
function setupCategoryFilters() {
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterMenu(btn.getAttribute('data-category'), document.getElementById('search-input').value);
    });
  });
}

function setupSearch() {
  const searchInput = document.getElementById('search-input');
  if (!searchInput) return;
  searchInput.addEventListener('input', (e) => {
    const activeBtn = document.querySelector('.filter-btn.active');
    filterMenu(activeBtn ? activeBtn.getAttribute('data-category') : 'all', e.target.value);
  });
}

function filterMenu(category, query) {
  let filtered = menuItems;

  if (category !== 'all') {
    filtered = filtered.filter(item => item.category === category);
  }

  if (query.trim() !== '') {
    const q = query.toLowerCase().trim();
    filtered = filtered.filter(item =>
      item.name.toLowerCase().includes(q) ||
      item.description.toLowerCase().includes(q)
    );
  }

  renderMenu(filtered);
}

/* -------------------------------------------------------------------------
   Scroll reveals
   ------------------------------------------------------------------------- */
let revealObserver;

function setupReveals() {
  if (prefersReducedMotion) {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('in'));
    return;
  }

  revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      // Stagger siblings so a row unfolds instead of popping all at once
      const siblings = Array.from(entry.target.parentElement.children).filter(c => c.classList.contains('reveal'));
      const delay = Math.min(siblings.indexOf(entry.target), 5) * 85;
      setTimeout(() => entry.target.classList.add('in'), delay);
      revealObserver.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
}

/* -------------------------------------------------------------------------
   Count-up statistics
   ------------------------------------------------------------------------- */
function setupCounters() {
  const nums = document.querySelectorAll('.stat-num');
  if (!nums.length) return;

  const run = (el) => {
    // data-since lets a "years open" figure work itself out from today's date,
    // so it stays correct without anyone editing the page every January.
    const since = parseInt(el.getAttribute('data-since'), 10);
    const target = since
      ? new Date().getFullYear() - since
      : (parseInt(el.getAttribute('data-count'), 10) || 0);
    const suffix = el.getAttribute('data-suffix') || '';
    if (prefersReducedMotion) {
      el.textContent = target + suffix;
      return;
    }
    const duration = 1300;
    const start = performance.now();
    const step = (now) => {
      const p = Math.min((now - start) / duration, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3))) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);

    // requestAnimationFrame is paused in a background tab, which would leave the
    // figure stuck part-way if someone switches away mid-count. Settle it either
    // way once the animation should have finished.
    setTimeout(() => { el.textContent = target + suffix; }, duration + 150);
  };

  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      run(e.target);
      obs.unobserve(e.target);
    });
  }, { threshold: 0.5 });

  nums.forEach(n => obs.observe(n));
}

/* -------------------------------------------------------------------------
   Page chrome that tracks the reader's position
   ------------------------------------------------------------------------- */
function setupScrollChrome() {
  const bar = document.getElementById('read-progress');
  const orb = document.getElementById('bg-orb');
  const header = document.getElementById('site-header');
  const rail = document.getElementById('step-rail');
  const railSteps = Array.from(document.querySelectorAll('.rail-step'));
  const navLinks = Array.from(document.querySelectorAll('.nav-links a'));

  const sections = SECTION_IDS
    .map(id => document.getElementById(id))
    .filter(Boolean);

  if (!sections.length) return;

  let ticking = false;

  function update() {
    ticking = false;

    const scrollY = window.scrollY;
    const viewMid = scrollY + window.innerHeight * 0.4;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPct = docHeight > 0 ? Math.min(scrollY / docHeight, 1) : 0;

    if (bar) bar.style.width = (scrollPct * 100) + '%';

    // A soft warm glow drifts alongside the reader
    if (orb) {
      const x = 8 + scrollPct * 80;
      const y = 14 + Math.sin(scrollPct * Math.PI) * 44;
      orb.style.transform = `translate(${x}vw, ${y}vh)`;
    }

    // Which step are we in?
    let current = sections[0];
    sections.forEach(s => { if (viewMid >= s.offsetTop) current = s; });

    const onDeep = current.getAttribute('data-tone') === 'deep';
    if (header) header.classList.toggle('on-deep', onDeep);
    if (rail) rail.classList.toggle('on-deep', onDeep);

    railSteps.forEach(s => s.classList.toggle('active', s.getAttribute('data-target') === current.id));
    navLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + current.id));
  }

  function onScroll() {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(update);
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  update();
}

/* The invitation to visit follows the reader past the hero. */
function setupVisitFab() {
  const fab = document.getElementById('visit-fab');
  const footer = document.querySelector('footer');
  if (!fab) return;

  window.addEventListener('scroll', () => {
    const past = window.scrollY > window.innerHeight * 0.8;
    const atFooter = footer && footer.getBoundingClientRect().top < window.innerHeight;
    const menuOpen = document.body.classList.contains('menu-open');
    fab.classList.toggle('show', past && !atFooter && !menuOpen);
  }, { passive: true });
}

function setupRail() {
  document.querySelectorAll('.rail-step').forEach(step => {
    step.addEventListener('click', () => scrollToSection(step.getAttribute('data-target')));
  });
}


/* -------------------------------------------------------------------------
   Mobile menu
   ------------------------------------------------------------------------- */
function setupMobileMenu() {
  const toggle = document.getElementById('nav-toggle');
  const menu = document.getElementById('mobile-menu');
  if (!toggle || !menu) return;

  function close() {
    menu.classList.remove('open');
    toggle.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open menu');
    document.body.classList.remove('menu-open');
  }

  function open() {
    menu.classList.add('open');
    toggle.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Close menu');
    document.body.classList.add('menu-open');
  }

  toggle.addEventListener('click', () => {
    menu.classList.contains('open') ? close() : open();
  });

  // Tapping any link jumps to the section and gets out of the way
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', close));

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') close();
  });

  // Rotating the phone into landscape can cross the desktop breakpoint
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 1080) close();
  });

  window.closeMobileMenu = close;
}

/* -------------------------------------------------------------------------
   Modals
   ------------------------------------------------------------------------- */
function setupReopeningModal() {
  const modal = document.getElementById('reopening-modal');
  if (!modal) return;

  setTimeout(() => modal.classList.add('active'), 1200);

  window.dismissReopening = function () {
    modal.classList.remove('active');
  };
}

function setupModalDismiss() {
  document.querySelectorAll('.modal-backdrop').forEach(backdrop => {
    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) backdrop.classList.remove('active');
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-backdrop.active').forEach(m => m.classList.remove('active'));
    }
  });
}

/* -------------------------------------------------------------------------
   Navigation helper
   ------------------------------------------------------------------------- */
window.scrollToSection = function (id) {
  const section = document.getElementById(id);
  if (!section) return;

  if (window.closeMobileMenu) window.closeMobileMenu();

  // Measure the sticky header rather than assuming a fixed height, since it
  // is shorter on a phone than on desktop.
  const header = document.getElementById('site-header');
  const headerOffset = header ? header.offsetHeight + 8 : 74;

  // Let the menu finish closing so the measurement is against the real layout
  requestAnimationFrame(() => {
    const offsetPosition = section.getBoundingClientRect().top + window.pageYOffset - headerOffset;
    window.scrollTo({
      top: id === 'top' ? 0 : offsetPosition,
      behavior: prefersReducedMotion ? 'auto' : 'smooth'
    });
  });
};

/* -------------------------------------------------------------------------
   Boot
   ------------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', () => {
  renderMenu(menuItems);
  renderSignatures();
  renderNastoStrip();

  setupMobileMenu();
  setupCategoryFilters();
  setupSearch();
  setupReopeningModal();
  setupModalDismiss();

  setupReveals();
  setupCounters();
  setupScrollChrome();
  setupVisitFab();
  setupRail();
});

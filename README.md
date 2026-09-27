# Raghuvanshi Khaman House & Lassi Centre

Single-page website for the shop at Kilavni Naka, Silvassa.
Current counter: 13, Perin Complex. New shop opening at 18 & 19, Perin Complex.

Plain HTML, CSS and JavaScript — **no build step, no framework, no server code.**
Whatever is in this folder is exactly what gets served.

## Files that make up the site

| File | What it is |
|---|---|
| `index.html` | The whole page |
| `style.css` | All styling (mobile-first) |
| `script.js` | Menu data, search/filter, mobile menu, scroll effects |
| `images/` | Logo and food photos, all WebP |
| `CREDITS.md` | Photo licences, linked from the footer. **Out of date, see the note at the top of it** |
| `images/logo.webp` | The shop emblem, 512x512, used in the header, hero, footer and 404 page |
| `images/share-preview.jpg` | 1200x630 image for WhatsApp and Facebook link previews |
| `images/favicon.png` | Browser tab icon, 96x96 |
| `images/apple-touch-icon.png` | Home-screen icon for iPhones, 180x180 |
| `documents/` | The downloadable PDF menu |
| `404.html` | Shown if someone opens a wrong link |
| `sitemap.xml`, `robots.txt` | What search engines read |
| `.nojekyll`, `vercel.json` | Hosting config |

`serve.js` is only for previewing on your own computer. It is not needed once the
site is hosted. `generate_pdf.py`, `items/` and `images/previous/` are working
files. Nothing on the site links to them, but they **are** committed and do get
uploaded to the host. `.gitignore` is a stock Next.js template and does not
exclude them. Harmless, just untidy.

## Preview it on your computer

```bash
node serve.js       # then open http://localhost:3000
```

Any static server works — for example `python3 -m http.server 3000`.

## Publish on GitHub Pages

1. Create a repository and push this folder to it.
2. Repository → **Settings** → **Pages**.
3. Under *Build and deployment*, set **Source: Deploy from a branch**,
   **Branch: `main`**, **Folder: `/ (root)`**, then **Save**.
4. The site appears at `https://<username>.github.io/<repository>/` in a minute or two.

All paths in the site are relative, so it works from a sub-folder URL like that
without any changes.

## Publish on Vercel

1. Go to [vercel.com/new](https://vercel.com/new) and import the repository.
2. Framework Preset: **Other**. Leave the build command and output directory blank.
3. **Deploy**.

`vercel.json` sets long cache times on the images so repeat visits load instantly.

To use your own domain, add it under **Settings → Domains** on Vercel, or
**Settings → Pages → Custom domain** on GitHub.

## Editing the menu

Every item lives in one list at the top of `script.js`:

```js
{
  id: 'khaman',                    // unique, lowercase, no spaces
  name: 'Khaman',                  // shown on the card
  category: 'snacks',              // 'snacks' | 'farsan' | 'drinks'
  description: 'Soft, spongy...',  // shown under the name
  price: 85,                       // not displayed on the site right now
  unit: '250 gms',
  image: 'images/khaman.webp',
  veg: true,
  popular: true                    // adds the orange "Most Loved" tag
}
```

Add, remove or edit entries in that list and the menu, the search and the
category filters all update on their own. Put any new photo in `images/`.

The three cards under **Most Loved** and the four under **Suko Nasto** are chosen
by id further down in `script.js`, in `renderSignatures()` and `renderNastoStrip()`.

## Things worth updating later

- **Opening date** — set to **Sunday, 11 October 2026**, the first day of
  Navratri. It appears in five places in `index.html`: the two `teaser-badge`
  labels and the `visit-address` line in the New Shop section, the last item of
  the About Us timeline, the "Opening 11 October 2026" row in the Visit Us card,
  and the `announce-info` line in the pop-up. The `og:`/`twitter:` descriptions
  in `<head>` mention it too.
- **Shop photos** — `images/shop_interior_1.webp` and `_2.webp` are deliberately
  blurred by CSS. Replace them with the real photos after the opening and remove
  the `filter: blur(...)` rule on `.teaser-img` in `style.css`.
- **After the move** — once 18 & 19 is open, swap the "Open now / Opening
  11 October 2026" address lines in the New Shop section and the Visit Us card
  over to the new number, drop the two `teaser-badge` labels, and update the
  Google Maps links.
- **Social links** — the shop has no Facebook or Instagram page, so the footer
  carries only Call, WhatsApp and Google Maps. If a page is ever made, add the
  icon back next to those three in the `footer-socials` block.
- **Share preview** — the `og:`/`twitter:`/`canonical` URLs in `<head>` are
  absolute and hard-coded to `https://hackmeet.github.io/raghuvanshi/`. They must
  be absolute or WhatsApp and Facebook will not show the preview image, so if the
  site moves to a custom domain, update those five URLs.
- **"Years in Silvassa" counter** — this works itself out from `data-since="1999"`
  on the stat in `index.html`, so it will read 28 in 2027 without anyone editing it.
  The year 1999 also appears in the page title, the hero, the About Us heading and
  the footer if it ever needs correcting.
- **24 photos with no menu entry** — `images/` still holds photos for items that
  are not in the menu list in `script.js`, so they never appear on the site:
  banana wafer, chana chor, chana dal masala, dalmoth, farali chevdo, farsi puri,
  fresh mango pickle, jira puri, khasta puri, khatta-mitha mix, methi puri (big
  and small), methi sakarpara, petis, potato wafer, ratlami sev, sakarpara,
  spendiyadi mix, sweet lassi curd, tikha mix namkeen, tikhi papdi, tikhi sev,
  veg cutlet and yellow banana wafer. That is 3.1 MB uploaded on every deploy for
  nothing. Either add them to the menu list or delete the files.

  `images/main-logo.jpeg` and `images/logo-trans.svg` are also unreferenced, but
  keep the first: it is the master the three logo files are generated from.
- **Two photos are used twice** — `coconut_petis.webp` is also Farali Peties, and
  `punjabi_samosa.webp` is also Chinese Samosa. Both pairs were byte-identical
  from the first commit. Rather than source new pictures, the menu order in
  `script.js` keeps each pair apart so they never land next to each other:

  | | position | 1 col | 2 col | 3 col |
  |---|---|---|---|---|
  | Coconut Patties / Farali Peties | 6 and 10 | 4 apart | 2 rows | 2 rows |
  | Mini Punjabi Samosa / Chinese Samosa | 3 and 8 | 5 apart | 2 rows | 2 rows |

  A gap of four is not on its own enough: positions 4 and 8 in a three-column
  grid land diagonally touching. **If you reorder the snacks, re-check that each
  pair is at least two rows apart in all three layouts**, diagonals included.
  Search results are the one place they can still appear together, because
  "samosa" matches both.
- **Menu photos** — every photo on the site is WebP at 720px wide, which is the
  widest any of them is ever displayed. They are served from `images/`, nothing
  is hot-linked. Where they came from is no longer certain: see the note at the
  top of `CREDITS.md`. The best fix is to photograph the real items, save them
  over these files using the same names, and then delete `CREDITS.md` and its
  footer link.
- **Logo** — the master artwork is `images/main-logo.jpeg` (873x681). The three
  files the site actually loads are generated from it, padded to a square on
  white so the round CSS crop lands the same way:

  | File | Size | Used for |
  |---|---|---|
  | `images/logo.webp` | 512x512 | header, hero, footer, 404 page |
  | `images/favicon.png` | 96x96 | browser tab |
  | `images/apple-touch-icon.png` | 180x180 | iPhone home screen |

  If the artwork ever changes, regenerate all three from the new master rather
  than editing them one by one.

  There used to be an `images/logo.svg`: an auto-trace of the same artwork,
  2531 paths and 1.15 MB, which every visitor downloaded just to draw a 48px
  header icon. It has been deleted.
- The old logo is kept at `images/previous/logo-old.svg`, and the earlier artwork
  and original `.png` files are in `images/previous/`. Nothing was deleted.
- **Icons** — there is no icon font and no CDN. Every icon is an
  `<i class="icon">` wrapping `<svg><use href="#i-name"></svg>`, pointing at the
  sprite near the top of `<body>` in `index.html`. The `<i>` wrapper is what
  `style.css` already styled, so `color` and `font-size` still control the icons
  exactly as they did with the webfont. To add one, drop a new `<symbol>` into
  the sprite and reference its id. The glyphs are Font Awesome Free 6.4.0
  (CC BY 4.0), which is why the sprite carries a licence comment. Loading these
  22 icons as a webfont from cdnjs used to cost 272 KB.
- **The announcement pop-up** — shows 1.2 seconds after **every** page load, on
  purpose. Dismissing it is not remembered, so a returning visitor sees it again.
  The close button, the backdrop and the Escape key all dismiss it for that visit.
  To make it appear only once per visitor instead, write a flag to `localStorage`
  in `closeModal()` and check it in `setupReopeningModal()` before the
  `setTimeout`. Key it on the opening date so changing the date shows it again.
- **The menu appears twice in the source** — once as the `menuItems` list in
  `script.js`, which draws the cards, and once as a plain `.menu-static` list
  inside `#menu-grid` in `index.html`. The static copy is thrown away the instant
  the cards render, so nobody sees both. It exists because the cards are built by
  JavaScript, and without it the item names are not in the HTML that search
  engines read first: "dhokla" and "khandvi" did not appear on the page at all.
  **Add an item in both places.** `script.js` compares the counts on every render
  and logs a console warning if they drift apart.
- **Search engines** — `sitemap.xml` lists the one page and `robots.txt` points
  at it. Neither does anything until the site is submitted to Google Search
  Console, which is the step that actually gets it crawled.

  For "khaman silvassa" and anything else local, the website is not the main
  lever: those searches are answered by the Google Maps pack above the web
  results, and that comes from a **Google Business Profile**, which is free and
  has to be claimed for the shop separately. Without it the shop does not appear
  in Maps at all.
- **Structured data** — the `application/ld+json` block at the end of `<head>`
  is what lets Google show the address, hours and a call button in search
  results. Keep it in step with the address and hours in the page. It carries no
  rating, price range or map coordinates, because those were not known; add them
  only from real data.

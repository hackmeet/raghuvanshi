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
| `images/` | Logo (SVG) and food photos (WebP) |
| `CREDITS.md` | Photo licences — linked from the footer, please keep it |
| `images/logo.webp` | The shop emblem, 512x512 — header, hero, footer and 404 page |
| `images/favicon.png` | Browser tab icon, 96x96 |
| `images/apple-touch-icon.png` | Home-screen icon for iPhones, 180x180 |
| `documents/` | The downloadable PDF menu |
| `404.html` | Shown if someone opens a wrong link |
| `.nojekyll`, `vercel.json`, `robots.txt` | Hosting config |

`serve.js` is only for previewing on your own computer. It is not needed once the
site is hosted. `generate_pdf.py`, `items/` and `images/previous/` are working
files. Nothing on the site links to them, but they **are** committed and do get
uploaded to the host — `.gitignore` is a stock Next.js template and does not
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
- **23 photos with no menu entry** — `images/` still holds photos for items that
  are not in the menu list in `script.js`, so they never appear on the site:
  banana wafer, chana chor, chana dal masala, dalmoth, farali chevdo, farsi puri,
  fresh mango pickle, jira puri, khasta puri, khatta-mitha mix, methi puri (big
  and small), methi sakarpara, potato wafer, ratlami sev, sakarpara, spendiyadi
  mix, sweet lassi curd, tikha mix namkeen, tikhi papdi, tikhi sev, veg cutlet
  and yellow banana wafer. Either add them to the menu list or delete the files.
- **Menu photos** — the 27 item photos are free-licence stock from Wikimedia
  Commons and Openverse, downloaded into `images/` (nothing is hot-linked).
  17 of them ask for a credit, which is why `CREDITS.md` is linked in the footer.
  The best fix is to photograph the real items and save them over these files
  using the same names — then you can delete `CREDITS.md` and its footer link.
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

  `images/logo.svg` is an old auto-trace of the same artwork — 2531 paths and
  **1.15 MB**, which every visitor was downloading just to draw a 48px header
  icon. Nothing links to it any more; it can be deleted.
- The old logo is kept at `images/previous/logo-old.svg`, and the earlier artwork
  and original `.png` files are in `images/previous/`. Nothing was deleted.

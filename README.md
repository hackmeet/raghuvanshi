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
| `images/logo.svg` | The shop emblem (vector, scales to any size) |
| `images/apple-touch-icon.png` | Home-screen icon for iPhones, made from the logo |
| `documents/` | The downloadable PDF menu |
| `404.html` | Shown if someone opens a wrong link |
| `.nojekyll`, `vercel.json`, `robots.txt` | Hosting config |

`serve.js` is only for previewing on your own computer. It is not needed once the
site is hosted. `generate_pdf.py`, `lijjat_menu.*` and `items/` are working files
and are excluded from the deployment by `.gitignore`.

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

- **Opening date** — currently "will be announced very soon", in the pop-up near
  the bottom of `index.html` and in the last item of the About Us timeline.
- **Shop photos** — `images/shop_interior_1.webp` and `_2.webp` are deliberately
  blurred by CSS. Replace them with the real photos after the opening and remove
  the `filter: blur(...)` rule on `.teaser-img` in `style.css`.
- **After the move** — once 18 & 19 is open, swap the "Open now / Opening soon"
  address lines in the New Shop section and the Visit Us card over to the new
  number, and update the Google Maps links.
- **Facebook link** — the icon in the footer currently points to `#`.
- **"Years in Silvassa" counter** — this works itself out from `data-since="1999"`
  on the stat in `index.html`, so it will read 28 in 2027 without anyone editing it.
  The year 1999 also appears in the page title, the hero, the About Us heading and
  the footer if it ever needs correcting.
- **Menu photos** — the 27 item photos are free-licence stock from Wikimedia
  Commons and Openverse, downloaded into `images/` (nothing is hot-linked).
  17 of them ask for a credit, which is why `CREDITS.md` is linked in the footer.
  The best fix is to photograph the real items and save them over these files
  using the same names — then you can delete `CREDITS.md` and its footer link.
- **Logo** — redrawn as a square badge so it stays sharp from a 38px header icon
  up to any size, and so the header stops squashing it (the old one was 3:2 being
  forced into a square). It is plain SVG, about 3 KB, and edits are just numbers
  and colours in `images/logo.svg`. If you change it, regenerate the iPhone icon
  by opening the logo at 180x180 on a cream background and saving a PNG.
- The old logo is kept at `images/previous/logo-old.svg`.
- The earlier artwork and the original `.png` files are in `images/previous/`.
  Nothing was deleted; that folder is excluded from the deployment by `.gitignore`.

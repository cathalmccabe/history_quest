# History Quest

An offline-first, installable iPhone flashcard web app for Irish Junior Cycle History. **No Apple Developer account is needed.**

## Included in this build

- 105 starter historical date cards across 9 topic groups, with a mix of year-only and exact-date questions.
- Three attempts with 100 / 50 / 25 points, progressive hints, and mandatory correct-date re-entry after three misses.
- Touch-friendly day/month/year selectors, or year-only entry; BCE dates supported.
- Weighted question selection, review intervals, progress and mastery tracking.
- Sessions of 5, 10, 20, 50 or all available cards; optional session timer.
- Study mode, daily challenge, category timeline, personal progress, three themes.
- Multiple local profiles, custom cards, topic filters, exam countdown, JSON backup/restore.
- Standalone PWA with service worker caching and offline use after first successful load.

## Important limitations

This is a **functional first build**, not the complete production version of the original specification. The question bank has **105 curated starter cards**, not 200–300 fully source-verified curriculum-mapped cards. Dates and event wording should be checked against your daughter's class materials before exam use. Some items are useful background rather than prescribed facts for every school. Built-in cards are not yet individually editable in the UI. Backup import replaces local data rather than merging it. The app uses localStorage rather than IndexedDB. There is no backend or cloud sync.

## Test locally

Python 3 is sufficient. In this directory run:

```bash
python -m http.server 8000
```

Open `http://localhost:8000` in your browser. Opening `index.html` directly from disk is not sufficient for service worker testing.

## Install on an iPhone

The iPhone must load the app over **HTTPS** (or localhost for development). Upload the contents of this directory to any HTTPS static web host such as GitHub Pages or Cloudflare Pages. In iPhone Safari:

1. Visit the hosted app URL and wait for it to load fully.
2. Tap **Share**.
3. Select **Add to Home Screen** (sometimes under **More**).
4. Tap **Add**.
5. Launch **History Quest** from the home screen.

You do **not** need an Apple Developer account or the App Store. Internet access is needed for the first load and for app updates, but previously cached app files work offline. For offline testing, load the app once online and then open it again with airplane mode on.

## Deploy to GitHub Pages

1. Create a new GitHub repository.
2. Upload all the files, including `icons/`.
3. Open **Settings → Pages**.
4. Select **Deploy from a branch**, choose `main` and `/ (root)`.
5. Wait for the published HTTPS URL and open it in Safari.

The manifest and asset paths are relative, so hosting in a project subdirectory is supported.

## Data and privacy

Progress is stored only in the browser on the current device. Clearing Safari website data, removing app storage, or changing devices can remove it. Use **Settings → Export JSON** regularly and store backups somewhere safe. Import replaces the current local data after confirmation.

## Content format

The built-in question bank lives in `questions.js`. Each card contains an ID, category, question, event title, date components, precision, explanation and revision tier. `make_questions.py` is the source generator for this starter set.

## Next recommended iteration

1. Verify and expand content to 200–300 dates, with citations per card and curriculum mapping.
2. Migrate localStorage to IndexedDB with schema migrations.
3. Add automated browser tests on Safari/WebKit, including background timer handling.
4. Add built-in question overrides, safer data import validation and backup merge.
5. Improve mastery scheduling with a full spaced-repetition model and clear review-due counts.

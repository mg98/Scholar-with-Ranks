# Scholar with Ranks publishing checklist

Release 2.2.0 is prepared locally. The upload package is `release/GSVR.zip`; store materials are in `release/store-assets/`. The privacy policy source is `docs/privacy.html`, and dashboard copy is in `docs/chrome-web-store-listing.md`.

The ZIP is approximately 4.4 MiB and the unpacked extension is 17.7 MiB. Unit/regression, scoring, venue catalog, SJR smoke, all 2,180 accuracy fixtures, and worker parity for 292 venues passed. ZIP integrity, manifest references, JavaScript syntax, store image dimensions, and the 40 MiB bundle budget also passed. Detailed results are in `release/validation/preflight.json`; benchmark reports are preserved in the same directory. `release/GSVR.zip.sha256` records the package checksum.

## Choose the correct listing

The README links to an existing listing with ID `egohghgpljdhkmcmllhncfndmkeilpfb`. Check whether your publisher account owns it. If you own it, upload an update to that item and confirm 2.2.0 exceeds the latest uploaded version. Otherwise, obtain a transfer if this is the same product, or create a distinct listing for your authorized distribution. Do not submit a duplicate of an existing listing you own.

The README credits Naveed Bhatti, and this checkout's remote is `mg98/Scholar-with-Ranks`. Confirm the publisher identity, author attribution, feedback form ownership, and redistribution rights for the extension and bundled datasets. The README has an MIT badge but this checkout has no root LICENSE file; a badge alone does not establish the licensing terms. Keep existing attributions and do not claim ownership of upstream code or datasets.

## Steps for the publisher

1. Register or sign in to the [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole). Complete the registration fee, two-step verification, contact verification, and any account or trader declarations shown by Google.
2. The privacy policy is live at https://mg98.github.io/Scholar-with-Ranks/privacy.html, hosted by GitHub Pages from `main` and `/docs` and verified without authentication. The Web Store privacy form draft includes this URL. Review the policy and ensure the support issue tracker and optional feedback form are destinations you maintain.
3. Load the generated `dist/` folder using `chrome://extensions` → Developer mode → Load unpacked. Manually verify a small and large profile, pagination/completeness, unmatched venues, rank filtering, date-range controls, popup rescanning, and settings. Check Chrome's extension Errors panel. A live smoke check of the source extension rendered 52 ranked publications on a public profile; check the packaged build too.
4. Use `release/store-assets/screenshot-candidate.png`, a current 1280×800 RGB PNG showing Geoffrey Hinton's public Scholar profile with the installed version 2.2.0 extension. It displays real inline badges, citation graph markers, and the complete CORE/SJR breakdown after the scan completed. The source image and capture metadata are in `docs/images/screenshot-candidate.png` and `docs/images/screenshot-candidate.json`.
5. Upload `release/GSVR.zip` to the existing item or Add new item as appropriate. Use the prepared listing copy, `icon128.png`, `promo-440x280.png`, a current screenshot, and the live privacy URL. Complete the permission and data usage fields from the listing document.
6. Choose distribution visibility and countries. Select Public for general availability. Review the complete listing, then Submit for Review. You can disable automatic publication after approval if you want to choose the launch date yourself.

## Rebuild commands

```sh
npm test
npm run test:score
npm run test:dblp
node GSVR/tests/sjr_smoke_test.js
npm run benchmark:accuracy -- --suite all --fail-on-regression
npm run test:worker-parity
npm run zip
node scripts/check_size_budget.mjs
python3 scripts/prepare_store_assets.py
```

The build regenerates the bundled rankings index before copying the release files. Do not ZIP the whole repository or the source directory with raw datasets and tests. Keep `manifest.json` at the ZIP root. Store images and privacy documents are separate from the extension upload.

## Permission review

The explicit `host_permissions` list (192 origins, including `scholar.googleusercontent.com`) was removed. Static content-script matches are narrowed to `/citations*` on the 191 previously supported Scholar domains. Same-origin pagination remains available; the popup identifies supported tabs through content-script messaging without reading tab URLs. The domain generator preserves this scope and no longer reintroduces DBLP or PDF-host permissions. Chrome may still flag content-script site access for review. Upload the rebuilt ZIP to apply these changes to the store draft.

## Current release scope

The current summary panel exposes rank breakdowns, filters, and date-range controls. Older score, export, comparison, and feedback overlay code remains in the source but is not exposed by this panel. The release description therefore omits those features, and the unused downloads permission and download service worker registration were removed. Restore and test a feature's UI before advertising it or requesting its permissions again. The older README feature descriptions and screenshot should not be copied into the store listing.

## Official requirements

- [Prepare the extension](https://developer.chrome.com/docs/webstore/prepare)
- [Listing images](https://developer.chrome.com/docs/webstore/images)
- [Privacy fields](https://developer.chrome.com/docs/webstore/cws-dashboard-privacy)
- [User data FAQ](https://developer.chrome.com/docs/webstore/program-policies/user-data-faq)
- [Upload and submit](https://developer.chrome.com/docs/webstore/publish)

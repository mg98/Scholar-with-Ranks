# Scholar with Ranks store listing

Copy the following fields into the Chrome Web Store dashboard for version 2.2.0. The privacy policy is published on GitHub Pages; its URL is listed below.

## Name

Scholar with Ranks

## Short description

Adds CORE conference ranks, SJR journal quartiles, rank filters, and timeline summaries to Google Scholar profiles.

## Detailed description

Understand the publication venues behind a Google Scholar author profile.

Scholar with Ranks adds CORE conference ranks and SCImago Journal Rank (SJR) quartiles to Scholar publication lists, using venue text from the profile and ranking datasets bundled with the extension.

- View venue rank badges next to publications.
- Explore CORE and SJR rank breakdowns.
- Filter publications by venue rank.
- Switch statistics between the full publication timeline and the last 10 years.
- See venue rank markers on Scholar's citation graph where available.
- Adjust the display and automatic scanning through the extension settings.

Processing and ranking calculations run in your browser. The extension requests additional Google Scholar publication-list pages and stores preferences and cached results locally. It does not include advertising or analytics and does not automatically upload profile results to a developer-operated server.

Venue matches are estimates based on the available profile text and bundled datasets. Editable or ambiguous venue names, missing information, and historical dataset coverage can affect the results. A venue rank is not a direct measure of an individual paper's quality. Review the source data before relying on a result.

Scholar with Ranks is an independent project and is not affiliated with or endorsed by Google, CORE, SCImago, or DBLP.

## Single purpose

Help users understand publication venues on Google Scholar author profiles through venue rankings, filters, and summary statistics.

## Permission justifications

### storage

Stores user preferences, cached profile and publication ranking results, and ranking data freshness state locally so users can restore settings and previously computed results.

### Content-script access to Scholar citations pages

Runs only on Google Scholar citations pages to read profile and publication information, insert venue rank badges and summary panels, and request additional publication-list pages on the same origin. Country-specific Scholar domains support localized profiles. No explicit host_permissions are requested; the popup communicates with the content script using the active tab ID without reading its URL. The extension does not request access to unrelated websites.

## Remote code

Select "No, I am not using remote code." Extension JavaScript, workers, the PDF generation library, and ranking data are bundled in the package. Scholar responses are parsed as page content rather than executed as code.

## Data usage disclosures

Declare the locally handled data as well as transmitted data. Suggested categories based on version 2.2.0:

- Personally identifiable information: public profile and author names, profile identifiers, and URLs handled for ranking and reports.
- Website content: Scholar profile and publication content parsed for the features.
- Web history: limited to Scholar profile/publication URLs handled to scan profiles and restore saved results; no general browsing history is collected.

The extension does not extract passwords, authentication tokens, or cookie values. Same-origin requests may carry session cookies through the browser's normal handling.

Certify the three dashboard statements only after reviewing that they describe your intended operation: no sale or transfer outside permitted uses, no unrelated uses, and no use for creditworthiness or lending. Keep these answers consistent with the published privacy policy.

## Support and policy URLs

- Homepage: https://github.com/mg98/Scholar-with-Ranks
- Support: https://github.com/mg98/Scholar-with-Ranks/issues
- Privacy policy: https://mg98.github.io/Scholar-with-Ranks/privacy.html (published from `main` and `/docs`, publicly verified).

## Reviewer instructions

1. Install the extension and open a public Google Scholar author profile with publications. No extension-specific account or paid service is required.
2. Wait for the automatic scan, or use the extension popup's rescan control. Check that the profile gains venue badges and summary results.
3. Open the venue breakdown and timeline controls. Ambiguous or unmatched venues may appear as unranked or require review.
4. Open the extension settings, change a display preference, and return to the profile to confirm the change.
5. Select a rank in the summary panel and confirm matching publications are highlighted. Switch between Full Timeline and Last 10 Years and confirm the summary updates.

Google Scholar can return a CAPTCHA or temporarily rate-limit pagination. Complete any Scholar challenge manually or retry later; do not interpret a partial scan as complete profile coverage.

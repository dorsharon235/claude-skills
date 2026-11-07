# Israeli law checklist for digital projects

Use only the sections that apply to the project. Every number, deadline and amount here MUST be re-checked against an official source before you present it (laws are amended often). Mark each finding: גבוה / בינוני / נמוך, and "לבדיקת עורך דין".

Good official sources to search: gov.il (הרשות להגנת הפרטיות, נציבות שוויון זכויות לאנשים עם מוגבלות, הרשות להגנת הצרכן), nevo.co.il, knesset.gov.il, the Israeli Standards Institute (ת"י 5568).

---

## 1. פרטיות — חוק הגנת הפרטיות, התשמ"א-1981 (כולל תיקון 13)
Applies when the project collects or stores ANY personal data (forms, sign-up, newsletter, analytics with identifiers, cookies tied to a user, uploads).

Check:
- **חובת יידוע** (סעיף 11): at the point of collection the user is told: whether giving the data is required by law or voluntary, the purpose, who gets the data. Look at every form.
- **מדיניות פרטיות** exists, is linked from every page (footer) and from every form, in Hebrew, matches what the code really collects (compare to the data list from phase 1, analytics, pixels, third-party scripts).
- **מאגר מידע**: after amendment 13 the registration duty changed and new duties apply (e.g. notifying the Authority for certain databases, appointing a privacy protection officer for some organizations). Verify the current thresholds before stating them.
- **אבטחת מידע** — תקנות הגנת הפרטיות (אבטחת מידע), התשע"ז-2017: HTTPS everywhere, no secrets in client code, access control, minimal data, retention, logging, breach handling. Check the code for keys in the front end, open admin pages, data in URLs, unencrypted storage.
- **העברת מידע לחו"ל**: data sent to foreign services (analytics, email, cloud). Note where it goes.
- **עוגיות ומעקב**: no specific Israeli cookie law, but tracking must be disclosed in the privacy policy; if EU users are targeted, GDPR consent rules apply too. Check what scripts load before any consent.
- **קטינים**: if users may be children (games, Roblox), flag heightened risk: collecting children's data, chat, purchases. Recommend parental consent and minimum data.
- **זכות עיון ותיקון** (סעיפים 13–14): there is a way to ask to see / fix / delete data (contact address in the policy).

## 2. נגישות — חוק שוויון זכויות לאנשים עם מוגבלות + תקנות התאמות נגישות לשירות, התשע"ג-2013
Applies to websites and apps that give a service to the public (almost every business site).

Check:
- The site meets **ת"י 5568** (the Israeli standard based on WCAG; verify which WCAG version/level the current standard references — at least AA). Test: keyboard only, visible focus, contrast, alt text, form labels, headings order, language/dir attributes, zoom 200%, captions for video, no content that flashes.
- **הצהרת נגישות** page exists and is linked from every page, with: what was made accessible, what is not yet, the date of the last check, and a named accessibility contact (name, phone, email).
- Accessibility "overlay" widgets do NOT make a site compliant by themselves. If the site relies on one, say so.
- Exposure: the law allows compensation without proof of damage in some cases — verify the current amount before quoting it.

## 3. צרכנות — חוק הגנת הצרכן, התשמ"א-1981
Applies when the project sells products or services, or takes payments / subscriptions.

Check:
- **עסקת מכר מרחוק** (סעיף 14ג): before the deal the customer sees: business name, ID number (ח.פ / ע.מ), address, phone, full description, full price, delivery dates and costs, cancellation terms. After the deal: a written confirmation.
- **ביטול עסקה**: the right to cancel and how (the law requires accepting cancellation in the ways the business uses to sell, e.g. online if sold online). Verify current cancellation window and the cap on cancellation fees before quoting.
- **עסקה מתמשכת / מנוי** (סעיף 13ד and related): clear renewal terms, easy cancellation, notices before price changes or end of a promo.
- **הצגת מחירים**: prices shown to consumers include VAT; no hidden fees revealed only at checkout.
- **פרסום מטעה** (סעיף 2): claims like "הכי זול", "מבצע", fake countdown timers, fake reviews, "רק 2 נשארו" that are not true.
- **החוזים האחידים**: terms of use that are one-sided (unlimited liability waivers, unilateral changes, far jurisdiction) may be void — flag them.

## 4. דיוור ופרסום — חוק התקשורת (בזק ושידורים), סעיף 30א ("חוק הספאם")
Applies to marketing emails, SMS, WhatsApp, push notifications.

Check:
- Opt-in: marketing messages only with prior explicit consent (a checkbox that is NOT pre-ticked, separate from accepting terms).
- Every message says it is an ad ("פרסומת" at the start of the subject/message) and has an easy unsubscribe.
- Sender identity and contact details are in the message.
- Exposure: per-message compensation without proof of damage — verify current amount.

## 5. תוכן וזכויות — חוק זכות יוצרים, התשס"ח-2007
Applies to every project with images, fonts, music, video, icons, code from others.

Check:
- Every image, font, music track, sound effect, icon and code library has a license that allows this use (commercial?). List anything with unknown source.
- AI-generated assets: note the tool and its terms.
- Photos of people: consent to use their image (privacy + right of publicity).
- Credits / attribution where the license requires it.
- Trademarks: no use of other brands' names/logos in a misleading way.

## 6. פרטי עסק וחובות כלליות
- Business details visible (name, ח.פ/ע.מ, contact) — required for distance selling and builds trust.
- Terms of use exist if users create accounts, post content, or buy.
- Invoices/receipts for payments (tax rules) — flag only, don't advise on tax.
- Regulated fields (finance, investments, health, insurance, legal, gambling, alcohol, tobacco, children): flag that sector-specific regulation exists and needs a professional. For financial data about public companies, check that public-source data is labeled and that nothing looks like investment advice.

## 7. Payments
- Card data never touches the project's own server unless it is PCI compliant — use the payment provider's hosted fields/page.
- Clear refund policy linked at checkout.

---

## How to write a legal finding
```
⚖️ [גבוה] חסרה הצהרת נגישות
מה ראיתי: אין קישור להצהרת נגישות בשום עמוד (צילום: step-03.png).
החוק: תקנות שוויון זכויות (התאמות נגישות לשירות), תקנה 35 — מקור: <link>
למה זה חשוב: חשיפה לתביעה גם בלי הוכחת נזק; לקוחות עם מוגבלות לא יודעים למי לפנות.
מה לעשות: להוסיף עמוד הצהרה (טיוטה מצורפת — לבדיקת עורך דין) וקישור בפוטר.
```

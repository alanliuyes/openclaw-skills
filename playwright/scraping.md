# Web Scraping with Playwright

## Basic Scraping

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  
  const data = await page.evaluate(() => {
    return document.title;
  });
  
  await browser.close();
})();
```

## Handling Dynamic Content

```javascript
// Wait for element
await page.waitForSelector('.loaded');

// Wait for network idle
await page.waitForLoadState('networkidle');
```
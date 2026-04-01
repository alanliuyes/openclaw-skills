# Debugging with Playwright

## Launching Inspector

```bash
npx playwright test --debug
```

## Trace Viewer

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch();
const context = await browser.newContext({
  recordVideo: { dir: 'videos/' }
});
```

## Console Logs

```javascript
page.on('console', msg => console.log(msg.text()));
```
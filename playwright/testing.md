# Testing with Playwright

## Writing Tests

```javascript
const { test, expect } = require('@playwright/test');

test('homepage has title', async ({ page }) => {
  await page.goto('https://playwright.dev');
  await expect(page).toHaveTitle(/Playwright/);
});
```

## Fixtures

```javascript
test('user can login', async ({ page, context }) => {
  // Test with authenticated state
});
```

## Assertions

- `toHaveText()` - Check text content
- `toHaveClass()` - Check CSS classes
- `toBeVisible()` - Check visibility
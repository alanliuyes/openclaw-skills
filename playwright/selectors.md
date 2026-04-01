# Selectors in Playwright

## Recommended Selectors

1. **User-facing selectors** - Text, label, placeholder
2. **Semantic selectors** - Role, title, alt text
3. **Test IDs** - data-testid attribute

## Examples

```javascript
// Text selector
await page.click('text=Submit');

// Role selector
await page.click('role=button[name="Submit"]');

// Test ID
await page.click('[data-testid="submit"]');
```

## Avoid

- XPath when possible
- CSS selectors based on styling
- Positional selectors
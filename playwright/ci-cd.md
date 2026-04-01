# CI/CD Best Practices

## GitHub Actions

```yaml
name: Test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npm test
```

## Deployment

- Use environment protection rules
- Require reviews for production
- Use secrets for sensitive data
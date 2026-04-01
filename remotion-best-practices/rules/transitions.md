# Transitions in Remotion

## Types

- Fade transitions
- Slide transitions
- Scale transitions
- Custom transitions

## Implementation

```tsx
const transition = interpolate(
  frame,
  [0, 30],
  [0, 1],
  { extrapolateRight: 'clamp' }
);
```
# Animations in Remotion

## Principles

- Use spring animations for natural feel
- Interpolate values smoothly
- Consider timing and easing

## Techniques

### Basic Animation
```tsx
const frame = useCurrentFrame();
const { interpolate } = require('remotion');

const opacity = interpolate(frame, [0, 30], [0, 1]);
```

### Spring Animation
```tsx
const { spring } = require('remotion');

const scale = spring({
  frame,
  fps,
  config: { damping: 10 }
});
```
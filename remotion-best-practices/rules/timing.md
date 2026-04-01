# Timing in Remotion

## FPS and Duration

- Standard: 30fps
- High quality: 60fps
- Calculate duration carefully

## Sequences

```tsx
<Sequence from={0} durationInFrames={30}>
  {<Title />}
</Sequence>
<Sequence from={30} durationInFrames={60}>
  {<Content />}
</Sequence>
```
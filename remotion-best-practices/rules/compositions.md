# Compositions in Remotion

## Best Practices

- Keep compositions focused
- Use props for customization
- Split complex scenes into components

## Example

```tsx
export const MyVideo: React.FC = () => {
  return (
    <Composition
      id="MyVideo"
      component={VideoComponent}
      durationInFrames={150}
      fps={30}
      width={1920}
      height={1080}
    />
  );
};
```
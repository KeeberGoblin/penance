# Godray Effect - Archived 2025-10-13

**Reason for archival**: Performance issues causing lag on the main page

**Visual Effect**: Volumetric light beams (godrays) emanating from top of page with cathedral-like atmosphere

## JavaScript Code

```javascript
// Animated individual godrays with varied widths
const godrayPositions = [
    { left: '5%', width: 40, delay: 0 },
    { left: '12%', width: 95, delay: 3 },
    { left: '19%', width: 55, delay: 7 },
    { left: '27%', width: 120, delay: 2 },
    { left: '35%', width: 70, delay: 5 },
    { left: '43%', width: 110, delay: 1 },
    { left: '52%', width: 60, delay: 8 },
    { left: '60%', width: 85, delay: 4 },
    { left: '68%', width: 130, delay: 6 },
    { left: '76%', width: 75, delay: 9 },
    { left: '84%', width: 50, delay: 2.5 },
    { left: '91%', width: 100, delay: 7.5 },
    { left: '97%', width: 65, delay: 4.5 }
];

godrayPositions.forEach((godray, index) => {
    const godrayEl = document.createElement('div');
    godrayEl.className = 'animated-drip';
    godrayEl.style.left = godray.left;
    godrayEl.style.width = `${godray.width}px`;
    godrayEl.style.animationDuration = `${10 + Math.random() * 8}s`;
    godrayEl.style.animationDelay = `${godray.delay}s`;
    // Add random blur variation for more organic feel
    godrayEl.style.filter = `blur(${6 + Math.random() * 6}px)`;
    document.body.appendChild(godrayEl);
});
```

## CSS Styles

```css
/* Animated godray class - volumetric light beams */
.animated-drip {
    position: fixed;
    top: 0;
    width: 80px;
    height: 0;
    background:
        /* Center bright core */
        radial-gradient(ellipse at center top,
            rgba(184, 149, 106, 0.7) 0%,
            rgba(184, 149, 106, 0.5) 30%,
            transparent 100%),
        /* Main vertical gradient */
        linear-gradient(to bottom,
            rgba(184, 149, 106, 0.6) 0%,
            rgba(184, 149, 106, 0.4) 10%,
            rgba(184, 149, 106, 0.25) 25%,
            rgba(184, 149, 106, 0.15) 40%,
            rgba(184, 149, 106, 0.08) 55%,
            rgba(184, 149, 106, 0.04) 70%,
            rgba(184, 149, 106, 0.02) 80%,
            rgba(184, 149, 106, 0.01) 90%,
            transparent 100%);
    pointer-events: none;
    z-index: 999;
    transform-origin: top center;
    animation: godrayPulse 12s ease-in-out infinite;
    box-shadow:
        0 0 30px rgba(184, 149, 106, 0.4),
        0 0 60px rgba(184, 149, 106, 0.25),
        0 0 100px rgba(184, 149, 106, 0.15),
        inset 0 0 40px rgba(255, 255, 255, 0.15);
    mix-blend-mode: screen;
    /* Enhanced edge fade with radial component */
    mask-image:
        radial-gradient(ellipse at 50% 0%,
            black 0%,
            rgba(0, 0, 0, 0.9) 20%,
            rgba(0, 0, 0, 0.7) 50%,
            rgba(0, 0, 0, 0.5) 70%,
            transparent 100%),
        linear-gradient(to bottom,
            black 0%,
            black 50%,
            rgba(0, 0, 0, 0.8) 70%,
            rgba(0, 0, 0, 0.5) 82%,
            rgba(0, 0, 0, 0.25) 90%,
            rgba(0, 0, 0, 0.1) 95%,
            transparent 100%);
    -webkit-mask-image:
        radial-gradient(ellipse at 50% 0%,
            black 0%,
            rgba(0, 0, 0, 0.9) 20%,
            rgba(0, 0, 0, 0.7) 50%,
            rgba(0, 0, 0, 0.5) 70%,
            transparent 100%),
        linear-gradient(to bottom,
            black 0%,
            black 50%,
            rgba(0, 0, 0, 0.8) 70%,
            rgba(0, 0, 0, 0.5) 82%,
            rgba(0, 0, 0, 0.25) 90%,
            rgba(0, 0, 0, 0.1) 95%,
            transparent 100%);
    mask-composite: intersect;
    -webkit-mask-composite: source-in;
}

@keyframes godrayPulse {
    0%, 100% {
        height: 300px;
        opacity: 0.3;
        transform: scaleX(1);
    }
    25% {
        height: 450px;
        opacity: 0.6;
        transform: scaleX(1.1);
    }
    50% {
        height: 600px;
        opacity: 0.5;
        transform: scaleX(0.95);
    }
    75% {
        height: 500px;
        opacity: 0.55;
        transform: scaleX(1.05);
    }
}
```

## Features

- **Varied beam widths**: 40px - 130px (13 unique sizes)
- **Random blur per beam**: 6-12px for organic variety
- **Animation timing**: 10-18 second cycles with 0-9s delays
- **Dual gradient system**: Radial core + linear vertical fade
- **Dual mask system**: Radial edge fade + linear bottom fade
- **Triple-layer glow**: 30px/60px/100px halos
- **Screen blend mode**: Authentic light compositing
- **Ultra-smooth edges**: Soft fade on all sides (top/bottom/left/right)

## Performance Impact

- 13 DOM elements dynamically created
- Each with complex CSS animations (opacity, height, scale)
- Multiple gradient layers per element
- Blur filters (6-12px per beam)
- Box-shadow effects (multiple layers)
- Screen blend mode compositing

**Result**: Caused page lag, removed from production

## Usage

To re-enable this effect in the future:
1. Add the CSS styles to your stylesheet
2. Add the JavaScript code to create the godray elements
3. Ensure the `.animated-drip` class selector is present

## Evolution History

1. **Dripping tears** - Thin 4px vertical drips growing from top
2. **Godrays v1** - 80px uniform beams with basic gradient
3. **Godrays v2** - Enhanced bottom fade for seamless looping
4. **Godrays v3** - Varied widths (40-130px), random blur, radial edge gradients
5. **Archived** - Performance issues on main page

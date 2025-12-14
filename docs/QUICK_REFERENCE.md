# Quick Reference Guide - Modern UI

## 🎨 CSS Variables

Quick access to customize colors anywhere in your CSS:

```css
:root {
  /* Gradients */
  --primary-gradient: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #d946ef 100%);
  --secondary-gradient: linear-gradient(135deg, #06b6d4 0%, #8b5cf6 50%, #ec4899 100%);
  
  /* Glass & Transparency */
  --glass-bg: rgba(255, 255, 255, 0.1);
  --glass-border: rgba(255, 255, 255, 0.2);
  
  /* Colors */
  --dark-bg: #0f172a;
  --card-bg: rgba(15, 23, 42, 0.8);
  --text-primary: #f1f5f9;
  --text-secondary: #cbd5e1;
  --accent-cyan: #06b6d4;
  --accent-purple: #a78bfa;
  --accent-pink: #f472b6;
}
```

## 🎬 Animation Snippets

### Add Header Fade-In
```css
.your-element {
  animation: fadeInDown 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### Add Card Entrance with Stagger
```css
.your-card {
  animation: fadeInUp 0.8s ease-out both;
}

.your-card:nth-child(1) { animation-delay: 0.3s; }
.your-card:nth-child(2) { animation-delay: 0.4s; }
.your-card:nth-child(3) { animation-delay: 0.5s; }
```

### Add Hover Lift
```css
.your-element:hover {
  transform: translateY(-8px);
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## 🎨 Glassmorphism Card

Copy-paste template for new cards:

```css
.glass-card {
  background: rgba(15, 23, 42, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 20px;
  padding: 32px;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.1),
    inset 0 1px 1px rgba(255, 255, 255, 0.1);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.glass-card:hover {
  background: rgba(15, 23, 42, 0.7);
  border-color: rgba(255, 255, 255, 0.25);
  transform: translateY(-8px);
  box-shadow: 
    0 16px 48px rgba(167, 139, 250, 0.2),
    inset 0 1px 1px rgba(255, 255, 255, 0.15);
}
```

## 🌈 Gradient Text

Apply gradient to any text:

```css
.gradient-text {
  background: linear-gradient(135deg, #fff 0%, #a78bfa 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

## ✨ Shimmer Button Effect

Add shimmer animation to buttons:

```css
.shimmer-button {
  position: relative;
  overflow: hidden;
}

.shimmer-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.5s;
}

.shimmer-button:hover::before {
  left: 100%;
}
```

## 🎯 Common Patterns

### Metric Card
```css
.metric {
  background: rgba(255, 255, 255, 0.05);
  padding: 16px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.metric:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}
```

### Badge/Badge Number
```css
.badge {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, var(--accent-purple) 0%, var(--accent-cyan) 100%);
  border-radius: 12px;
  font-weight: 700;
  color: white;
  box-shadow: 
    0 8px 24px rgba(167, 139, 250, 0.3),
    0 0 1px rgba(255, 255, 255, 0.3) inset;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.badge:hover {
  transform: scale(1.1) rotateY(10deg);
  box-shadow: 
    0 12px 32px rgba(167, 139, 250, 0.4),
    0 0 1px rgba(255, 255, 255, 0.5) inset;
}
```

### Progress Bar
```css
.progress-container {
  width: 100%;
  height: 8px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  overflow: hidden;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.2);
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, var(--accent-purple) 0%, var(--accent-cyan) 100%);
  border-radius: 4px;
  box-shadow: 0 0 12px rgba(167, 139, 250, 0.4);
  transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## 📱 Responsive Breakpoints

```css
/* Desktop - No media query needed, base styles */

/* Tablet */
@media (max-width: 768px) {
  /* Reduce padding, font sizes, adjust grid */
}

/* Mobile */
@media (max-width: 480px) {
  /* Minimal layout, single column, reduced sizes */
}
```

## 🎨 Color Combinations

### Text on Dark Background
```css
/* High contrast */
color: var(--text-primary); /* #f1f5f9 */

/* Secondary text */
color: var(--text-secondary); /* #cbd5e1 */

/* Accent highlight */
color: var(--accent-cyan); /* #06b6d4 */
```

### Button Gradients
```css
/* Purple to Cyan */
background: linear-gradient(135deg, var(--accent-purple) 0%, var(--accent-cyan) 100%);

/* Custom */
background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #d946ef 100%);
```

### Box Shadows

**Soft (Default Cards)**
```css
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1), inset 0 1px 1px rgba(255, 255, 255, 0.1);
```

**Hover (Enhanced)**
```css
box-shadow: 0 16px 48px rgba(167, 139, 250, 0.2), inset 0 1px 1px rgba(255, 255, 255, 0.15);
```

**Glow (Gradients)**
```css
box-shadow: 0 0 12px rgba(167, 139, 250, 0.4);
```

## ⚡ Performance Tips

### Best Practices
- ✅ Use `transform` instead of `position` changes
- ✅ Use `opacity` for fade effects
- ✅ Keep animations under 1 second for UI interactions
- ✅ Use `cubic-bezier(0.34, 1.56, 0.64, 1)` for smooth easing
- ✅ Limit backdrop-filter use to important elements

### Avoid
- ❌ Animating `width` or `height` directly
- ❌ Animating `left`, `right`, `top`, `bottom`
- ❌ Overusing blur effects (performance impact)
- ❌ Animations over 2 seconds for interactions

## 🔄 How to Extend

### Add New Gradient
```css
:root {
  --custom-gradient: linear-gradient(135deg, #color1 0%, #color2 100%);
}
```

### Create New Animation
```css
@keyframes myAnimation {
  from {
    /* Starting state */
  }
  to {
    /* Ending state */
  }
}

.my-element {
  animation: myAnimation 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### Add New Color
```css
:root {
  --my-custom-color: #hexcode;
}

.my-element {
  color: var(--my-custom-color);
}
```

## 🛠️ Debugging

### Check Glassmorphism Not Working?
```css
/* Ensure these are present */
backdrop-filter: blur(Xpx);
-webkit-backdrop-filter: blur(Xpx);
background: rgba(...);
```

### Animation Not Smooth?
```css
/* Use GPU-accelerated properties only */
transform: translateY(-8px);
opacity: 1;
/* Avoid animating: width, height, left, right, etc. */
```

### Color Variables Not Working?
```css
/* Make sure they're defined in :root */
:root {
  --my-var: value;
}

/* Then use with var() */
color: var(--my-var);
```

## 📊 File Structure

```
frontend/
├── src/
│   ├── styles/
│   │   ├── index.css          ← Global styles & variables
│   │   ├── App.css            ← App container
│   │   ├── ResultsPage.css    ← Main page
│   │   ├── SearchBar.css      ← Search input
│   │   └── ResultCard.css     ← Result cards
│   ├── components/
│   ├── pages/
│   └── services/
└── package.json
```

## 🚀 Quick Start

1. **View the changes**: Open `http://localhost:5174`
2. **Customize colors**: Edit CSS variables in `index.css`
3. **Adjust animations**: Modify duration/easing in respective CSS files
4. **Add new components**: Use the patterns above as templates

## 📞 Need Help?

Refer to these documentation files:
- `docs/MODERN_UI_DESIGN.md` - Comprehensive design guide
- `docs/UI_COMPONENTS_GUIDE.md` - Component specifications
- `MODERN_UI_IMPLEMENTATION.md` - Implementation details

---

**Happy styling! 🎨**

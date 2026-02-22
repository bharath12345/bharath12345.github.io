# Website Optimization Plan

## Summary
Current analysis shows **3.7MB of unused JavaScript libraries** that can be removed immediately, plus opportunities for additional optimizations.

---

## 1. Remove Unused JavaScript Libraries ⚡ HIGH PRIORITY

### jQuery (87KB) - **UNUSED**
- Currently loaded from CDN: `jquery-3.7.0.min.js`
- **Finding**: No jQuery usage found in any template
- **Action**: Remove from `base.html` line 100-101

### Local Library Directory (1.1MB) - **UNUSED**
All files in `themes/custom/static/lib/` are unused:

**jquery.toc/** (~50KB)
- Replaced by Python Markdown TOC extension
- No longer needed

**d3/** (500KB) - d3-3.3.2.js + minified
- Was used for interactive graphs
- Not functional in current site (noted in content)
- Only mentioned in blog text, not actively used

**jsPlumb/** (500KB) - jquery.jsPlumb-1.5.2.js + minified
- Was used for interactive graphs
- Not functional in current site
- Only mentioned in blog text, not actively used

**Action**: Delete entire `themes/custom/static/lib/` directory

---

## 2. Remove Unused Fonts (2.6MB) ⚡ HIGH PRIORITY

### Hermit Font (~500KB)
- Files: hermit.ttf, hermit.otf
- **Not referenced** in any CSS or template

### Roboto Font (~2.1MB)
- Multiple weight files
- **Not referenced** in any CSS or template
- Using Google Fonts (Open Sans) instead

**Action**: Delete entire `themes/custom/static/fonts/` directory

**Total Savings: 3.7MB of unused static assets**

---

## 3. Optimize Images 🎨 MEDIUM PRIORITY

### Current State
- Total: 14MB of images
- Some large images: appdynamics.jpg (540KB), optier.jpg (683KB), me.jpg (205KB)

### Recommended Actions:
1. **Convert to WebP format** (50-80% smaller than JPEG/PNG)
   - Use tools like `cwebp` or online converters
   - Maintain JPEG fallback for old browsers

2. **Compress existing images**
   - Use tools like `imageoptim`, `jpegoptim`, or `pngquant`
   - Target: 30-50% reduction without visible quality loss

3. **Lazy loading**
   - Add `loading="lazy"` attribute to images
   - Especially important for movie posters page

**Estimated Savings: 5-8MB**

---

## 4. Minify and Optimize CSS 📝 LOW PRIORITY

### Current State
- Custom CSS: `themes/custom/static/css/custom.css`
- Not minified

### Action:
- Minify custom.css (save ~30-40%)
- Consider critical CSS inlining for above-the-fold content

**Estimated Savings: ~5KB**

---

## 5. Optimize External Resources ⚡ MEDIUM PRIORITY

### Bootstrap 5
- Currently: Full Bootstrap bundle (75KB gzipped)
- **Consideration**: Build custom Bootstrap with only needed components
  - Keep: navbar, grid, utilities, forms
  - Remove: carousel, modals, tooltips, popovers, etc.
- **Estimated Savings**: 30-40KB

### Font Awesome
- Currently: Full Font Awesome (1MB+, though CDN cached)
- Only using: 4 icons (user, github, linkedin, youtube)
- **Action**: Use Font Awesome Kit with only needed icons OR use inline SVG
- **Estimated Savings**: Eliminate 1MB+ request

### Google Fonts
- Currently: Open Sans (300, 400, 600 weights)
- **Consideration**: Use `&display=swap` for better performance
- Already using preconnect - good!

---

## 6. Enable Compression 📦 HIGH PRIORITY

### For GitHub Pages deployment:
- GitHub Pages automatically serves gzip/brotli
- Verify with browser dev tools
- Ensure `.html`, `.css`, `.js` files are compressed

---

## 7. Add Cache Headers 🔄 INFORMATIONAL

### GitHub Pages Default:
- Static assets: 10 minute cache
- HTML: No cache by default

### Recommendation:
- Add cache-busting for CSS/JS (filename hashing)
- Consider service worker for offline capability

---

## 8. Performance Budget Targets 🎯

### After Optimization:
- Initial page load: < 500KB
- Time to Interactive: < 3s on 3G
- Lighthouse Performance Score: > 90

### Current Estimated Size:
- HTML: ~20KB
- CSS (Bootstrap + Custom): ~50KB
- JS (Bootstrap): ~60KB
- Fonts: ~30KB (Google Fonts)
- **Remove**: 3.7MB unused assets ✅

---

## Implementation Priority

### Phase 1 - Quick Wins (< 30 min)
1. ✅ Remove jQuery from base.html
2. ✅ Delete themes/custom/static/lib/
3. ✅ Delete themes/custom/static/fonts/

### Phase 2 - Font Awesome (1 hour)
4. Replace Font Awesome CDN with inline SVG icons

### Phase 3 - Images (2-3 hours)
5. Compress existing images
6. Add lazy loading to images

### Phase 4 - Advanced (Optional)
7. Convert images to WebP
8. Create custom Bootstrap build
9. Implement service worker

---

## Testing Checklist

After each change:
- [ ] Test local build: `pelican content`
- [ ] Check all pages render correctly
- [ ] Verify navigation works
- [ ] Test search functionality
- [ ] Run Lighthouse audit
- [ ] Test on mobile device

---

## Tools Needed

- **Image optimization**: imageoptim, jpegoptim, cwebp
- **Performance testing**: Chrome DevTools, Lighthouse
- **Build tools**: Already have Pelican


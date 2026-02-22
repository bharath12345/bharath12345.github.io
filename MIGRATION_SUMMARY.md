# Blog Migration Summary - Bharadwaj's Blog

## Overview
Successfully migrated Bharadwaj's blog from Jekyll (Ruby/npm) to Pelican (Python).

## What Was Migrated

### ✅ Content
- **27 published blog posts** - All posts converted from Jekyll to Pelican format
- **6 draft posts** - Migrated to `content/drafts/` directory
- **18 static pages** - Including all about pages, tags, categories, and index pages

### ✅ Assets
- **Images** - All blog images and assets (14MB total)
- **Resources** - Presentations, spreadsheets, and other resources
- **Docs** - JavaScript documentation files
- **JavaScript Libraries**:
  - D3.js (for data visualizations)
  - jsPlumb (for topology diagrams)
  - jQuery TOC plugin (for table of contents)
  - Custom fonts (Hermit, Roboto)

### ✅ Theme
- **Modern Bootstrap 5 theme** - Upgraded from Bootstrap 2.3.2
- **Same visual structure** - Dark purple (#483d8b) navbar, textile background, same layout
- **Responsive design** - Better mobile support with modern CSS
- **All custom styling preserved** - TOC boxes, bylines, listing styles, etc.

### ✅ Features Removed (as requested)
- ❌ Disqus comments
- ❌ Google Analytics
- ❌ Gauges analytics
- ❌ Twitter/Facebook share buttons

## Technology Stack

### Before (Jekyll)
- Ruby + Jekyll
- npm + Grunt (for minification)
- Bootstrap 2.3.2
- RVM for Ruby version management

### After (Pelican)
- **Python 3** + Pelican
- **Python-based minification** (pelican-minify)
- **Bootstrap 5** (modern, responsive)
- Virtual environment for Python dependencies

## Directory Structure

```
bharath12345.github.io-pelican/
├── content/              # Your content
│   ├── *.md             # Blog posts (27 files)
│   ├── drafts/          # Draft posts (6 files)
│   ├── pages/           # Static pages (18 files)
│   ├── images/          # All images
│   ├── resources/       # Resources
│   └── extra/           # Extra files (CNAME, docs)
├── themes/
│   └── custom/          # Custom Bootstrap 5 theme
│       ├── templates/   # Jinja2 templates
│       └── static/      # CSS, JS, fonts
├── output/              # Generated site (not committed)
├── venv/                # Python virtual environment
├── pelicanconf.py       # Main configuration
├── publishconf.py       # Production configuration
├── requirements.txt     # Python dependencies
├── Makefile            # Build commands
├── deploy.sh           # Deployment helper
└── deploy_to_github.sh # GitHub Pages deployment
```

## How to Use

### Development

1. **Activate virtual environment:**
   ```bash
   cd /Users/bharadwaj/Work/Code/mine/bharath12345.github.io-pelican
   source venv/bin/activate
   ```

2. **Start development server:**
   ```bash
   make serve
   # or for auto-reload:
   make devserver
   ```
   Visit http://localhost:8000

3. **Build the site:**
   ```bash
   make html
   ```

### Creating New Posts

Create a new file in `content/` with this format:

```markdown
Title: Your Post Title
Date: 2026-02-22
Category: posts
Tags: python, pelican, migration
Slug: your-post-slug

Your post content here in Markdown...
```

For drafts, save in `content/drafts/` or add `Status: draft` to the metadata.

### Deployment to GitHub Pages

1. **Build for production:**
   ```bash
   make publish
   ```
   This builds with minification enabled.

2. **Deploy to GitHub Pages:**
   ```bash
   ./deploy_to_github.sh
   ```
   This script:
   - Builds the site with production settings
   - Copies output to `../bharath12345.github.io/`
   - Preserves `.git`, `CNAME`, etc.

3. **Commit and push:**
   ```bash
   cd ../bharath12345.github.io
   git status
   git add .
   git commit -m "Deploy Pelican site"
   git push origin master
   ```

### Useful Commands

```bash
make html          # Generate site
make clean         # Remove generated files
make regenerate    # Regenerate on file changes
make serve         # Serve at http://localhost:8000
make devserver     # Serve and auto-regenerate
make publish       # Build for production (with minification)
```

## Configuration Files

### pelicanconf.py
Main configuration for development. Key settings:
- Site name, author, description
- URL structure (matches Jekyll: `/posts/{slug}/`)
- Timezone, language
- Theme location
- Markdown extensions
- Static paths

### publishconf.py
Production configuration that:
- Sets the production URL (https://bharath12345.github.io)
- Enables RSS/Atom feeds
- Enables minification (pelican-minify plugin)
- Removes comments and whitespace from HTML

## Metadata Mapping

### Jekyll → Pelican

| Jekyll | Pelican |
|--------|---------|
| `title: "Post Title"` | `Title: Post Title` |
| `date: 2024-01-01` | `Date: 2024-01-01` |
| `category: posts` | `Category: posts` |
| `tags: [tag1, tag2]` | `Tags: tag1, tag2` |
| `published: false` | `Status: draft` |
| `layout: about` | `Template: about` |

### Custom Metadata Supported

- `Toc: true` - Enable table of contents
- `Subheading: true` + `Subhead: text` - Add subheading
- `Slug: custom-url` - Custom URL slug

## Known Issues & Notes

1. **Docs HTML files** - JSDoc HTML files in `content/extra/docs/` generate warnings but are copied correctly as static files.

2. **Jekyll syntax in content** - Some posts may contain Jekyll-specific syntax like `{{ category }}` or `{{ tag }}`. These generate warnings but don't break the site. You may want to clean them up manually.

3. **URL structure** - The URL structure matches Jekyll (`/posts/{slug}/`) to preserve existing links.

4. **Images paths** - Image paths should work as-is since they're in `/images/`.

## Next Steps

1. **Test the site locally** thoroughly by visiting http://localhost:8000
2. **Review all posts** to ensure formatting is correct
3. **Check special pages** like About, Movies, etc. that may have custom HTML
4. **Deploy to GitHub Pages** when satisfied
5. **Archive the Jekyll repository** or keep it as backup

## Benefits of Pelican

1. **Pure Python** - No Ruby/RVM needed
2. **Simpler dependencies** - Just `pip install -r requirements.txt`
3. **Modern theme** - Bootstrap 5 with better mobile support
4. **Cleaner workflow** - Python virtual environment
5. **Extensible** - Easy to add Python-based plugins
6. **Faster builds** - Pelican is generally faster than Jekyll

## Troubleshooting

If you encounter issues:

1. **Rebuild from scratch:**
   ```bash
   make clean
   make html
   ```

2. **Check for syntax errors:**
   ```bash
   pelican -D content -o output -s pelicanconf.py
   ```

3. **Verify Python environment:**
   ```bash
   source venv/bin/activate
   pip list | grep pelican
   ```

## Support Files

- `requirements.txt` - Python dependencies
- `Makefile` - Build automation
- `migrate_posts.py` - Script used for migration (can be rerun)
- `migrate_pages.py` - Script used for pages migration
- `.gitignore` - Ignores output/, venv/, etc.

---

Migration completed on: 2026-02-22
Total time: ~15 minutes

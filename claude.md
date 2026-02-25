# Website Documentation - bharath12345.github.io

## Overview

This is a personal blog and portfolio website built with Pelican static site generator and deployed to GitHub Pages. The site features technical blog posts, poetry translations, and various personal content pages.

**Live Site**: https://bharath12345.github.io

## Technology Stack

- **Static Site Generator**: Pelican 4.x (Python-based)
- **Template Engine**: Jinja2
- **CSS Framework**: Bootstrap 5
- **Languages**: Python 3, HTML5, CSS3, JavaScript
- **Version Control**: Git
- **Hosting**: GitHub Pages
- **Domain**: Custom CNAME configured

## Repository Structure

```
bharath12345.github.io/
├── content/              # Source content (Markdown files)
│   ├── posts/           # Blog articles
│   ├── pages/           # Static pages
│   │   └── about/       # About section pages
│   │       ├── movies.md
│   │       ├── travel.md
│   │       ├── slideshare.md
│   │       ├── philosophy.md
│   │       └── ಕಗ್ಗ.md   # Kannada poetry with translations
│   └── extra/           # Static assets (images, docs)
├── themes/              # Custom theme
│   └── custom/
│       ├── templates/   # Jinja2 templates
│       │   ├── base.html
│       │   ├── index.html
│       │   ├── article.html
│       │   ├── about.html
│       │   ├── category.html
│       │   └── tag.html
│       └── static/
│           └── css/
│               └── custom.css
├── output/              # Generated static site (not committed)
├── venv/                # Python virtual environment
├── pelicanconf.py       # Development configuration
├── publishconf.py       # Production configuration
├── add_kagga_translations.py  # Script for poetry translations
└── Makefile            # Build automation
```

## Git Workflow

This repository uses a **two-branch workflow**:

### Main Branch (`main`)
- Contains source code (content, themes, configs)
- Where all development happens
- Pelican source files
- Configuration and scripts

### Master Branch (`master`)
- Contains generated static HTML/CSS/JS
- Deployed to GitHub Pages
- Only the `output/` directory contents
- Automatically served at bharath12345.github.io

## Content Management

### Blog Posts

Location: `content/posts/`
Format: Markdown with front matter

```markdown
Title: Post Title
Date: 2024-01-01 10:00
Category: Posts
Tags: tag1, tag2
Slug: post-slug
Author: Bharadwaj
Summary: Brief description

Content here...
```

### Pages

Location: `content/pages/`
Special pages use custom templates via `Template:` metadata.

### About Section

The About section has a secondary navigation bar with these pages:
- **Movies**: Favorite films with images and descriptions
- **Travel**: Travel experiences and photos
- **Slideshare**: Presentation links and embeds
- **Philosophy**: Philosophical content
- **ಕಗ್ಗ (Kagga)**: Mankuthimmana Kagga poetry with English translations

## Special Features

### Mankuthimmana Kagga Poetry Page

**File**: `content/pages/about/ಕಗ್ಗ.md`
**URL**: https://bharath12345.github.io/pages/about/resources/

Features:
- 217 stanzas with English translations
- Two-column layout: Kannada (left) + English (right)
- Uses CSS Grid for responsive columns
- Custom styling for poetry display

**Translation Management**:
- Translations stored in: `add_kagga_translations.py`
- Script processes markdown and wraps stanzas in HTML divs
- Format:
  ```html
  <div class="poetry-stanza">
    <div class="poetry-kannada">
      [Kannada text]
    </div>
    <div class="poetry-english">
      [English translation]
    </div>
  </div>
  ```

To update translations:
1. Edit `add_kagga_translations.py` dictionary
2. Run: `python3 add_kagga_translations.py`
3. Replace: `mv content/pages/about/ಕಗ್ಗ_new.md content/pages/about/ಕಗ್ಗ.md`
4. Rebuild site

### CSS Styling

**File**: `themes/custom/static/css/custom.css`

Key customizations:
- Purple color scheme (`#483d8b` - Dark Slate Blue)
- Reduced heading sizes (h1: 1.8rem → h6: 0.9rem)
- Pagination: 5 articles per page
- Secondary navigation bar for About section
- Poetry-specific styles:
  - `.poetry-stanza`: Grid container
  - `.poetry-kannada`: Bold, larger (1.1rem)
  - `.poetry-english`: Italic, smaller (0.95rem)
- Adjusted spacing throughout
- Fixed pagination visibility (white text on purple)

## Configuration Files

### pelicanconf.py (Development)

Key settings:
```python
SITENAME = 'Thoughts, Notes & Collections'
SITEURL = ''  # Empty for development
AUTHOR = 'Bharadwaj'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

# Pagination
DEFAULT_PAGINATION = 5  # Shows 5 articles per page

# Paths
PATH = 'content'
OUTPUT_PATH = 'output'
THEME = 'themes/custom'

# URLs
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Static files
STATIC_PATHS = ['extra', 'images']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/docs': {'path': 'docs'},
}
```

### publishconf.py (Production)

Extends `pelicanconf.py` with production settings:
```python
SITEURL = 'https://bharath12345.github.io'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
```

## Build and Deployment Process

### Setup

1. Clone repository:
   ```bash
   git clone https://github.com/bharath12345/bharath12345.github.io.git
   cd bharath12345.github.io
   ```

2. Switch to main branch:
   ```bash
   git checkout main
   ```

3. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install pelican markdown
   ```

### Development Workflow

1. Activate virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Make content changes in `content/` directory

3. Preview locally:
   ```bash
   pelican content
   # Optionally serve locally:
   python -m http.server --directory output 8000
   # Visit: http://localhost:8000
   ```

4. Commit changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```

### Production Deployment

1. Build production site:
   ```bash
   source venv/bin/activate
   pelican content -s publishconf.py
   ```

2. Switch to master branch:
   ```bash
   git checkout master
   ```

3. Sync output to master:
   ```bash
   rsync -av --delete --exclude='.git' --exclude='output' --exclude='content' \
         --exclude='themes' --exclude='venv' --exclude='*.py' \
         --exclude='pelicanconf.py' --exclude='publishconf.py' \
         --exclude='Makefile' output/ .
   ```

4. Commit and deploy:
   ```bash
   git add -A
   git commit -m "Deploy: [description]"
   git push origin master
   ```

5. Return to main branch:
   ```bash
   git checkout main
   ```

GitHub Pages will automatically serve the master branch at https://bharath12345.github.io

## Template Structure

### base.html
Master template with:
- HTML head (meta tags, CSS)
- Navigation bar
- `{% block extra_nav %}` for secondary navigation
- `{% block content %}` for page content
- Footer
- JavaScript includes

### about.html
Used for About section pages:
- Extends `base.html`
- Implements secondary navigation in `extra_nav` block
- Special styling for poetry content

### index.html
Homepage listing:
- Shows article summaries (with `|striptags` filter)
- Pagination (5 articles per page)
- Category and tag links

### article.html
Individual blog post display:
- Full article content
- Metadata (date, category, tags, author)
- Navigation to other posts

## Key Features and Settings

### Pagination
- 5 articles per page (configurable in `pelicanconf.py`)
- Visible page numbers with proper contrast
- Active page highlighted in purple with white text

### Blog Summaries
- HTML tags stripped from summaries using `|striptags` filter
- Prevents headings from appearing in listing pages
- Clean, consistent presentation

### Navigation
- Primary: Main menu in top bar
- Secondary: About section submenu (Movies, Travel, etc.)
- Increased spacing between menu items (15px margin)

### Responsive Design
- Bootstrap 5 grid system
- Mobile-friendly navigation
- Responsive poetry columns

## Maintenance Tasks

### Adding a New Blog Post

1. Create file: `content/posts/my-new-post.md`
2. Add front matter and content
3. Build and preview: `pelican content`
4. Commit and deploy (see workflow above)

### Updating Poetry Translations

1. Edit `add_kagga_translations.py`
2. Add/update entries in `translations` dictionary
3. Run script: `python3 add_kagga_translations.py`
4. Review: Check `content/pages/about/ಕಗ್ಗ_new.md`
5. Replace: `mv content/pages/about/ಕಗ್ಗ_new.md content/pages/about/ಕಗ್ಗ.md`
6. Rebuild and deploy

### Modifying Styles

1. Edit: `themes/custom/static/css/custom.css`
2. Rebuild: `pelican content`
3. Preview changes
4. Commit and deploy

### Adding New Pages

1. Create markdown file in `content/pages/`
2. Add appropriate front matter (Title, Slug, Template)
3. If using custom template, create in `themes/custom/templates/`
4. Update navigation in `base.html` or `about.html` if needed
5. Rebuild and deploy

## Troubleshooting

### Virtual Environment Issues
If `source venv/bin/activate` fails, recreate:
```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install pelican markdown
```

### Build Errors
Common warnings (can be ignored):
- `Cannot load plugin 'pelican.plugins.webassets'`
- `Cannot load plugin 'pelican_minify'`
- Meta tag warnings for docs HTML files

### Git Issues
If branches get out of sync:
```bash
# On main branch
git fetch origin
git reset --hard origin/main

# On master branch
git checkout master
git fetch origin
git reset --hard origin/master
```

### Content Not Updating
1. Clear output: `rm -rf output`
2. Rebuild: `pelican content`
3. Check SITEURL in config matches your deployment

## File Encoding

- All files use UTF-8 encoding
- Kannada text properly encoded in markdown
- Python scripts handle Unicode correctly

## Dependencies

Required Python packages:
- pelican (4.x)
- markdown
- jinja2 (comes with Pelican)

Optional but recommended:
- pelican-minify (for CSS/JS minification)
- pelican.plugins.webassets (for asset management)

## Migration History

Originally a Jekyll blog, migrated to Pelican in February 2024:
- Converted Jekyll posts to Pelican format
- Restructured pages and navigation
- Updated theme to Bootstrap 5
- Added custom features (poetry translations, secondary nav)
- Improved styling and spacing

## Contact and Attribution

**Author**: Bharadwaj
**Site**: https://bharath12345.github.io
**GitHub**: https://github.com/bharath12345

Content generation assisted by Claude Code.

---

Last updated: February 2024

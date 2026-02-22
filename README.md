# Bharadwaj's Blog (Pelican)

This is the Pelican-based version of Bharadwaj's blog, migrated from Jekyll.

## Technology Stack

- **Static Site Generator**: Pelican (Python)
- **Theme**: Custom Bootstrap 5 theme
- **Hosting**: GitHub Pages
- **Build Tools**: Python-based minification (pelican-minify)

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Development

- `make html` - Generate the site
- `make serve` - Serve locally at http://localhost:8000
- `make devserver` - Auto-regenerate and serve
- `make publish` - Build for production with minification
- `make github` - Deploy to GitHub Pages

## Structure

- `content/` - Blog posts and pages (Markdown)
- `content/drafts/` - Draft posts
- `themes/custom/` - Custom theme files
- `static/` - Static assets (CSS, JS, images)
- `output/` - Generated site (not committed)

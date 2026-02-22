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

## Publishing Workflow

This repository uses a dual-branch strategy:
- **main branch**: Pelican source code (content, themes, configuration)
- **master branch**: Generated HTML (served by GitHub Pages)

### To Publish New Posts

1. **Activate virtual environment**:
```bash
cd /Users/bharadwaj/Work/Code/mine/bharath12345.github.io
source venv/bin/activate
```

2. **Write content** in `content/` directory:
```bash
# Create new post
vim content/YYYY-MM-DD-your-post-title.md
```

3. **Build and test locally**:
```bash
pelican content
pelican --listen
# Visit http://localhost:8000
```

4. **Commit to main branch** (source):
```bash
git checkout main
git add .
git commit -m "New post: Your Title"
git push
```

5. **Build for production and deploy**:
```bash
# Build with production settings
pelican content -s publishconf.py

# Switch to master branch
git checkout master

# Clean master branch
rm -rf * .gitignore

# Copy generated output
cp -r output/* .
rm -rf output __pycache__

# Commit and push
git add -A
git commit -m "Deploy: Your Title"
git push
```

6. **Site updates automatically**: GitHub Pages will update within a few minutes

### Quick Deploy Script

For convenience, you can create a `deploy.sh` script:
```bash
#!/bin/bash
source venv/bin/activate
pelican content -s publishconf.py
git checkout master
rm -rf * .gitignore
cp -r output/* .
rm -rf output __pycache__
git add -A
git commit -m "Deploy: $(date '+%Y-%m-%d %H:%M')"
git push
git checkout main
echo "Deployed to master branch!"
```

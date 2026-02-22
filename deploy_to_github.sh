#!/bin/bash
#
# Deploy Pelican blog output to the GitHub Pages repository
#

set -e

PELICAN_DIR="$(pwd)"
JEKYLL_DIR="../bharath12345.github.io"
OUTPUT_DIR="output"

echo "========================================"
echo "Deploying to GitHub Pages"
echo "========================================"
echo ""

# Build the site
echo "Building site with production settings..."
make publish

echo ""
echo "Copying files to GitHub Pages repository..."

# Create a list of files/dirs to preserve in the Jekyll repo
# (things that shouldn't be deleted)
PRESERVE=(".git" ".gitignore" "CNAME" "README.md")

# Remove old content except preserved files
cd "$JEKYLL_DIR"
for item in *; do
    preserve=false
    for keep in "${PRESERVE[@]}"; do
        if [ "$item" == "$keep" ]; then
            preserve=true
            break
        fi
    done

    if [ "$preserve" = false ]; then
        echo "  Removing: $item"
        rm -rf "$item"
    fi
done

# Copy new content
echo ""
echo "Copying new content..."
cd "$PELICAN_DIR"
cp -r $OUTPUT_DIR/* "$JEKYLL_DIR/"

echo ""
echo "========================================"
echo "Files copied successfully!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. cd $JEKYLL_DIR"
echo "2. git status (review changes)"
echo "3. git add ."
echo "4. git commit -m 'Deploy Pelican site'"
echo "5. git push origin master"
echo ""

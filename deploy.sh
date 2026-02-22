#!/bin/bash
#
# Deploy script for Pelican blog to GitHub Pages
#

set -e

echo "Building site with production settings..."
make publish

echo ""
echo "Site built successfully!"
echo ""
echo "To deploy to GitHub Pages:"
echo "1. Copy the contents of 'output/' directory to '../bharath12345.github.io/'"
echo "2. Commit and push from the Jekyll repository"
echo ""
echo "Or run: ./deploy_to_github.sh"

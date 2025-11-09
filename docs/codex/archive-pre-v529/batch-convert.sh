#!/bin/bash
# Simple batch conversion script using direct sed

count=0
for file in *.html; do
  if grep -q '<div class="content">\|<div class="manuscript-page">' "$file"; then
    # Step 1: Convert opening tags
    sed -i 's|<div class="content">|<main class="content" role="main">|g' "$file"
    sed -i 's|<div class="manuscript-page">|<main class="manuscript-page" role="main">|g' "$file"
    sed -i 's|<div class="breadcrumb">|<nav class="breadcrumb" aria-label="Breadcrumb">|g' "$file"
    
    # Step 2: Find and replace breadcrumb closing (first </div> after <nav class="breadcrumb")
    breadcrumb_line=$(grep -n '<nav class="breadcrumb"' "$file" | cut -d: -f1 | head -1)
    if [ -n "$breadcrumb_line" ]; then
      closing_line=$(tail -n +$((breadcrumb_line + 1)) "$file" | grep -n '</div>' | head -1 | cut -d: -f1)
      if [ -n "$closing_line" ]; then
        actual_line=$((breadcrumb_line + closing_line))
        sed -i "${actual_line}s|</div>|</nav>|" "$file"
      fi
    fi
    
    # Step 3: Replace last </div> before script with </main>
    script_line=$(grep -n '<script src="codex-common.js"></script>' "$file" | cut -d: -f1)
    if [ -n "$script_line" ]; then
      closing_line=$(head -n $((script_line - 1)) "$file" | grep -n '</div>' | tail -1 | cut -d: -f1)
      if [ -n "$closing_line" ]; then
        sed -i "${closing_line}s|</div>|</main>|" "$file"
      fi
    fi
    
    count=$((count + 1))
    echo "Converted: $file"
  fi
done

echo "Total files converted: $count"

/**
 * Penance Codex - Common JavaScript
 * Ensures all internal links open in parent frame and applies accessibility enhancements
 */

(function() {
    'use strict';

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCodex);
    } else {
        initCodex();
    }

    function initCodex() {
        // Fix all internal HTML links to target parent frame
        fixInternalLinks();

        // Apply accessibility enhancements
        enhanceAccessibility();
    }

    function fixInternalLinks() {
        // Get all links on the page
        const links = document.querySelectorAll('a[href]');

        links.forEach(link => {
            const href = link.getAttribute('href');

            // Check if it's an internal HTML link (relative path ending in .html)
            if (href && href.match(/^[^:\/]*\.html/)) {
                // Only set target if not already set
                if (!link.hasAttribute('target')) {
                    link.setAttribute('target', '_parent');
                }
            }
        });
    }

    function enhanceAccessibility() {
        // 1. Mark decorative Unicode symbols as aria-hidden
        markDecorativeSymbols();

        // 2. Add ARIA landmarks to content areas
        addARIALandmarks();

        // 3. Enhance breadcrumb navigation
        enhanceBreadcrumbs();

        // 4. Mark particles as decorative
        markDecorativeParticles();

        // 5. Add table captions for accessibility
        addTableCaptions();

        // 6. Ensure headings have proper hierarchy
        checkHeadingHierarchy();

        // 7. Enhance form accessibility
        enhanceFormAccessibility();

        // 8. Add live regions for dynamic content
        addLiveRegions();
    }

    function markDecorativeSymbols() {
        // Common decorative symbols used in the codex
        const decorativePatterns = [
            /^[⸸❈◆⬥✦✧⚔⚙§¶†‡※]$/,  // Single decorative symbols
            /^[═─]+$/,                   // Horizontal lines
            /^[\s⸸❈◆]+$/                 // Multiple decorative symbols with spaces
        ];

        // Find all span and div elements that might contain decorative symbols
        document.querySelectorAll('span, div').forEach(element => {
            const text = element.textContent.trim();

            // Check if element contains only decorative symbols
            const isDecorative = decorativePatterns.some(pattern => pattern.test(text));

            if (isDecorative && !element.hasAttribute('aria-hidden')) {
                element.setAttribute('aria-hidden', 'true');
            }
        });

        // Also mark elements with class "divider" as decorative
        document.querySelectorAll('.divider').forEach(element => {
            if (!element.hasAttribute('aria-hidden')) {
                element.setAttribute('aria-hidden', 'true');
            }
        });
    }

    function addARIALandmarks() {
        // Semantic HTML5 tags are now used directly in the HTML files
        // No dynamic role assignment needed - <main> and <nav> tags are in the source
        // This function is kept for backwards compatibility but does nothing
    }

    function enhanceBreadcrumbs() {
        const breadcrumb = document.querySelector('.breadcrumb');
        if (breadcrumb) {
            // Ensure breadcrumb navigation is properly labeled
            if (!breadcrumb.hasAttribute('aria-label')) {
                breadcrumb.setAttribute('aria-label', 'Breadcrumb navigation');
            }
        }
    }

    function markDecorativeParticles() {
        // Mark particle containers as decorative
        const particlesContainer = document.querySelector('.particles');
        if (particlesContainer) {
            particlesContainer.setAttribute('aria-hidden', 'true');
        }

        // Mark individual particles
        document.querySelectorAll('.particle').forEach(particle => {
            particle.setAttribute('aria-hidden', 'true');
        });
    }

    function addTableCaptions() {
        // Find all tables without captions
        document.querySelectorAll('table').forEach(table => {
            // Skip if table already has a caption
            if (table.querySelector('caption')) return;

            // Try to infer caption from context
            let caption = inferTableCaption(table);

            if (caption) {
                const captionElement = document.createElement('caption');
                captionElement.textContent = caption;
                captionElement.className = 'sr-only'; // Visually hidden but screen-reader accessible
                table.insertBefore(captionElement, table.firstChild);
            }
        });
    }

    function inferTableCaption(table) {
        // Strategy 1: Look for heading immediately before table
        let previousElement = table.previousElementSibling;
        while (previousElement && previousElement.textContent.trim() === '') {
            previousElement = previousElement.previousElementSibling;
        }

        if (previousElement && /^H[2-6]$/.test(previousElement.tagName)) {
            return previousElement.textContent.trim();
        }

        // Strategy 2: Check first header cell
        const firstTh = table.querySelector('th');
        if (firstTh) {
            const headerText = firstTh.textContent.trim();
            if (headerText.length > 0 && headerText.length < 100) {
                return `Table: ${headerText} and related data`;
            }
        }

        // Strategy 3: Look at parent section heading
        const parentSection = table.closest('section, article, div');
        if (parentSection) {
            const sectionHeading = parentSection.querySelector('h1, h2, h3, h4');
            if (sectionHeading) {
                return `Table from ${sectionHeading.textContent.trim()}`;
            }
        }

        // Strategy 4: Generic caption based on page title
        const pageTitle = document.querySelector('h1');
        if (pageTitle) {
            return `Data table from ${pageTitle.textContent.trim()}`;
        }

        // Fallback
        return 'Data table';
    }

    function checkHeadingHierarchy() {
        // Warn in console if heading hierarchy is incorrect (skip h1 check for iframes)
        const headings = document.querySelectorAll('h2, h3, h4, h5, h6');
        let previousLevel = 1; // Assume h1 exists

        headings.forEach((heading, index) => {
            const currentLevel = parseInt(heading.tagName.charAt(1));

            // Check if we skipped a level
            if (currentLevel > previousLevel + 1) {
                console.warn(
                    `Accessibility Warning: Heading hierarchy skip detected. ` +
                    `Found <${heading.tagName}> after <h${previousLevel}>. ` +
                    `Text: "${heading.textContent.trim().substring(0, 50)}..."`
                );
            }

            previousLevel = currentLevel;
        });
    }

    function enhanceFormAccessibility() {
        // Add ARIA attributes to form elements
        document.querySelectorAll('select, input[type="text"], input[type="number"], textarea').forEach(element => {
            const id = element.id;
            if (!id) return;

            // Add aria-required for required fields
            if (element.hasAttribute('required') && !element.hasAttribute('aria-required')) {
                element.setAttribute('aria-required', 'true');
            }
        });

        // Enhance buttons with better labels
        document.querySelectorAll('button').forEach(button => {
            if (!button.hasAttribute('aria-label')) {
                const text = button.textContent.trim();
                // Remove emojis and decorative symbols and clean up
                const cleanText = text.replace(/[⚔✦⚙🎲📜]/g, '').trim();
                if (cleanText) {
                    button.setAttribute('aria-label', cleanText);
                }
            }

            // Ensure button type is set only for buttons not inside a form
            if (!button.hasAttribute('type') && !button.closest('form')) {
                button.setAttribute('type', 'button');
            }
        });
    }

    function addLiveRegions() {
        // Mark result boxes as live regions for dynamic content announcements
        document.querySelectorAll('.result-box, #loot-result, #event-result, #npc-result, #encounter-result, #settlement-result, #env-result').forEach(resultBox => {
            if (!resultBox.hasAttribute('aria-live')) {
                resultBox.setAttribute('aria-live', 'polite');
                resultBox.setAttribute('aria-atomic', 'true');
            }
        });


    }
})();

/**
 * Penance Codex - Common JavaScript
 * Ensures all internal links open in parent frame to maintain navigation
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
})();

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
                element.setAttribute('role', 'presentation');
            }
        });

        // Also mark elements with class "divider" as decorative
        document.querySelectorAll('.divider').forEach(element => {
            if (!element.hasAttribute('aria-hidden')) {
                element.setAttribute('aria-hidden', 'true');
                element.setAttribute('role', 'presentation');
            }
        });
    }

    function addARIALandmarks() {
        // Wrap .content div in <main> if not already wrapped
        const contentDiv = document.querySelector('.content');
        if (contentDiv && !contentDiv.closest('main')) {
            contentDiv.setAttribute('role', 'main');
        }

        // Add navigation role to breadcrumbs
        const breadcrumb = document.querySelector('.breadcrumb');
        if (breadcrumb && breadcrumb.tagName !== 'NAV') {
            breadcrumb.setAttribute('role', 'navigation');
            breadcrumb.setAttribute('aria-label', 'Breadcrumb');
        }
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
            particlesContainer.setAttribute('role', 'presentation');
        }

        // Mark individual particles
        document.querySelectorAll('.particle').forEach(particle => {
            particle.setAttribute('aria-hidden', 'true');
            particle.setAttribute('role', 'presentation');
        });
    }
})();
